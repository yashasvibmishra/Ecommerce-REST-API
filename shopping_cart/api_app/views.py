from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.views import View
from django.http import JsonResponse
import json
from .models import CartItem,Users,Sellers,Warehouses


@method_decorator(csrf_exempt, name='dispatch')
 

class ShoppingCart(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity,
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)


    def get(self, request):
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'product_price': item.product_price,
                'product_quantity': item.product_quantity,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCartUpdate(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = CartItem.objects.get(id=item_id)
        
        

        if 'product_quantity' in data:
            item.product_quantity = data['product_quantity']
        if 'product_name' in data:
            item.product_name = data['product_name']
        if 'product_price' in data:
            item.product_price = data['product_price']

            
        
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, item_id):
        item = CartItem.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }

        return JsonResponse(data)        





@method_decorator(csrf_exempt, name='dispatch')
class UserDetails(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        user_data = {
            'name': name,
            'email': email,
            'password': password,
        }

        user = Users.objects.create(**user_data)

        data = {
            "message": f"New user added to Cart with id: {user.id}"
        }
        return JsonResponse(data, status=201)


    def get(self, request):
        users_count = Users.objects.count()
        users = Users.objects.all()

        users_data = []
        for user in users:
            users_data.append({
                'name': user.name,
                'email': user.email,
                'password': user.password,
            })

        data = {
            'users': users_data,
            'count': users_count,
        }

        return JsonResponse(data)



@method_decorator(csrf_exempt, name='dispatch')
class UserDetailsUpdate(View):
    def patch(self, request, user_id):
        data = json.loads(request.body.decode("utf-8"))
        user = Users.objects.get(id=user_id)

        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']

        user.save()

        data = {
            'message': f'User {user_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, user_id):
        user = Users.objects.get(id=user_id)
        user.delete()

        data = {
            'message': f'User {user_id} has been deleted'
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class SellerDetails(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        phone = data.get('phone')
        zipcode = data.get('zipcode')
        company_name = data.get('company_name')

        seller_data = {
            'phone': phone,
            'zipcode': zipcode,
            'company_name': company_name,
        }

        seller = Sellers.objects.create(**seller_data)

        data = {
            "message": f"New seller added to Cart with id: {seller.id}"
        }
        return JsonResponse(data, status=201)


    def get(self, request):
        sellers_count = Sellers.objects.count()
        sellers = Sellers.objects.all()

        sellers_data = []
        for seller in sellers:
            sellers_data.append({
                'phone': seller.phone,
                'zipcode': seller.zipcode,
                'company_name': seller.company_name,
            })

        data = {
            'sellers': sellers_data,
            'count': sellers_count,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class SellerDetailsUpdate(View):
    def patch(self, request, seller_id):
        data = json.loads(request.body.decode("utf-8"))
        seller = Sellers.objects.get(id=seller_id)

        if 'phone' in data:
            seller.phone = data['phone']
        if 'zipcode' in data:
            seller.zipcode = data['zipcode']
        if 'company_name' in data:
            seller.company_name = data['company_name']
            
        seller.save()

        data = {
            'message': f'Seller {seller_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, seller_id):
        seller = Sellers.objects.get(id=seller_id)
        seller.delete()

        data = {
            'message': f'Seller {seller_id} has been deleted'
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class WarehouseDetails(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        city = data.get('city')
        number = data.get('number')

        warehouse_data = {
            'city': city,
            'number': number,
        }

        warehouse = Warehouses.objects.create(**warehouse_data)

        data = {
            "message": f"New warehouse added to Cart with id: {warehouse.id}"
        }
        return JsonResponse(data, status=201)


    def get(self, request):

        warehouses_count = Warehouses.objects.count()
        warehouses = Warehouses.objects.all()

        warehouses_data = []
        for warehouse in warehouses:
            warehouses_data.append({
                'city': warehouse.city,
                'number': warehouse.number,
            })
        
        data = {
            'warehouses': warehouses_data,
            'count': warehouses_count,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class WarehouseDetailsUpdate(View):

    def patch(self, request, warehouse_id):
        data = json.loads(request.body.decode("utf-8"))
        warehouse = Warehouses.objects.get(id=warehouse_id)

        if 'city' in data:
            warehouse.city = data['city']
        if 'number' in data:
            warehouse.number = data['number']

        warehouse.save()

        data = {
            'message': f'Warehouse {warehouse_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, warehouse_id):
        warehouse = Warehouses.objects.get(id=warehouse_id)
        warehouse.delete()

        data = {
            'message': f'Warehouse {warehouse_id} has been deleted'
        }

        return JsonResponse(data)


