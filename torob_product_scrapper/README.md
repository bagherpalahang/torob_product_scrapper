# torob_product_scrapper
This is a project that checks your product situation in torob edgham page 

Url : add_link/
POST REQUEST : adding an endgham page to your account
Auth : TokenAuth
Body : page_link : pageLink
ex : 
{
    "page_link" : "https://torob.com/p/d0503a15-a485-46fd-ad70-0736cb1d6b6e/%D8%B4%D8%A7%D9%85%D9%BE%D9%88-%D8%AE%D8%B4%DA%A9-%D8%A7%D9%88%D8%AC%DB%8C-%D8%A7%DB%8C%DA%A9%D8%B3-%D8%AD%D8%A7%D9%88%DB%8C-%D8%A8%DB%8C%D9%88%D8%AA%DB%8C%D9%86-%DA%A9%D9%84%D8%A7%DA%98%D9%86-165%D9%85%DB%8C%D9%84/"
}
-----------------------------------------------------------------------------
URL : check_products/
POST REQUEST : Refresh all product situations
GET REQUEST : Get product data
Auth : TokenAuth
Body : No Body
-----------------------------------------------------------------------------
URL : changed_detail/
GET REQUEST : Returns datas that changed
AUTH : TokenAuth
Body : No Body
-----------------------------------------------------------------------------

