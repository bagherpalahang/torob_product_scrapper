from django.urls import path
from .views import AddLinkView, CheckProductSituationView, AlertView

app_name = 'edgham_page'

urlpatterns = [
    path('add_link/', AddLinkView.as_view(), name='add_link'),
    path('check_products/', CheckProductSituationView.as_view(), name='add_link'),
    path('changed_detail/', AlertView.as_view(), name='changed_detail'),
]
