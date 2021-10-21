from django.shortcuts import render
from ninja import Router
from .models import Category, Product , Merchant ,Vendor, Label , Address , City

shop_controller=Router()

@shop_controller.get('product')
def get_product(request):
    products = Product.objects.all()
    productinfo = []
    for product in products:
     vendor = Vendor.objects.get(id = product.vendor.id)
     merchant = Merchant.objects.get(id = product.merchant.id)
     category = Category.objects.get(id = product.category.id)
     label = Label.objects.get(id = product.label.id)
     productinfo.append({'productName' : product.name, 'productDiscription' : product.description , "productQty" : product.qty , "productCost" : product.cost , "productPrice" : product.price , "productweight" : product.weight , "productheight" : product.height ,  "productwidth" : product.width , "productlength" : product.length , "discounted_price" : product.discounted_price ,"productVendor" : vendor.name , "productMerchant" : merchant.name , "categoryName" : category.name , "labelName" : label.name})
    return productinfo

@shop_controller.get('address')
def get_address(request):
    addresses = Address.objects.all()
    addressinfo = []
    for address in addresses:
     city = City.objects.get(id = address.city_id)
     addressinfo.append({'userFirstName' :address.user.first_name ,'address1' : address.address1, 'address2' : address.address2 , 'phoneNo.' : address.phone , 'city' : city.name })
    return addressinfo