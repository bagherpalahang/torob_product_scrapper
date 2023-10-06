import json
import requests
from bs4 import BeautifulSoup

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import EdghamPage
from .serializers import EdghamPageSerializer

# Create your views here.

class AddLinkView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        json_data = json.loads(request.body)
        page_link = json_data['page_link']

        if not page_link.startswith("https://torob.com/p/") and '/' in page_link[19:]:
            return Response({'message' : 'You entered wrong URL'}, status=400)

        page, is_created = EdghamPage.objects.get_or_create(store=request.user ,page_link=page_link)

        if not is_created:
            return Response({'message' : 'This URL already exists'}, status=400)

        return Response({"message" : "link added successfully","page_link" : page_link},status=201)
    
class CheckProductSituationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def _check_product_detail(self, edgham_page, store_name):
        headers = {'User-Agent': 'Liara Webservice (https://www.liara1.ir)'}
        page = requests.get(edgham_page.page_link, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        script = soup.find("script", type="application/ld+json")
        products = json.loads(script.string)
    
        edgham_page.product_name = products['name']
        lowest_price = products['offers']['lowPrice']
        edgham_page.is_your_product_on_this_page = False
        products_list = sorted([item for item in products['offers']['offers'] if int(item['price']) != 0], key=lambda x: x['price'])
        second_price = products_list[1]['price'] if len(products_list) >= 2 else 0

        for index, item in enumerate(products_list):
            if item['name'] == store_name:
                edgham_page.is_your_product_on_this_page = True

                edgham_page.prev_fisrt_product_price = edgham_page.fisrt_product_price
                edgham_page.fisrt_product_price = lowest_price

                edgham_page.prev_second_product_price = edgham_page.second_product_price
                edgham_page.second_product_price = second_price

                edgham_page.prev_my_product_price = edgham_page.my_product_price
                edgham_page.my_product_price = item['price']

                edgham_page.prev_my_product_rank = edgham_page.my_product_rank
                edgham_page.my_product_rank = index + 1

                break
        edgham_page.save()
    
    def post(self, request):
        store = request.user
        store_records = store.store_edghamPage.all()

        for item in store_records:
            self._check_product_detail(item, store.username)

        return Response({'message' : 'data has been refreshed'}, status=200)

    def get(self, request):
        store = request.user
        filtered_records = store.store_edghamPage.filter(is_your_product_on_this_page=True)
        serializer = EdghamPageSerializer(filtered_records, many=True)
        return Response(serializer.data, status=200)
     
class AlertView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def _check_changed_detail(self, records):
        changed_detail = []

        for item in records:
            if item.prev_fisrt_product_price != item.fisrt_product_price or item.prev_second_product_price != item.second_product_price or item.prev_my_product_price != item.my_product_price or item.prev_my_product_rank != item.my_product_rank:
                changed_detail.append(item)

        return changed_detail

    def get(self, request):
        store = request.user
        filtered_records = store.store_edghamPage.filter(is_your_product_on_this_page=True)
        changed_detail = self._check_changed_detail(filtered_records)
        serializer = EdghamPageSerializer(changed_detail, many=True)

        return Response(serializer.data, status=200)