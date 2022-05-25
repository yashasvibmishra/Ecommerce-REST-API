from django.urls import path
from .views import ShoppingCart,ShoppingCartUpdate,UserDetails,UserDetailsUpdate,SellerDetails,SellerDetailsUpdate,WarehouseDetails,WarehouseDetailsUpdate

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    path('update-item/<int:item_id>', ShoppingCartUpdate.as_view()),
    path('user-details/', UserDetails.as_view()),
    path('update-user-details/<int:user_id>', UserDetailsUpdate.as_view()),
    path('seller-details/', SellerDetails.as_view()),
    path('update-seller-details/<int:seller_id>', SellerDetailsUpdate.as_view()),
    path('warehouse-details/', WarehouseDetails.as_view()),
    path('update-warehouse-details/<int:warehouse_id>', WarehouseDetailsUpdate.as_view()),
    
]


