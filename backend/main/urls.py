from django.urls import path
from . import views
from .views import RegisterAPIView, VerifyEmailAPIView

urlpatterns = [
    path('product/<int:product_id>/', views.ProductAPIView.as_view(), name='product-by-id'),
    path('product/all/', views.ProductViewSet.as_view({'get': 'list'}), name='all-products'),
    path('category/all/', views.CategoryViewSet.as_view({'get': 'list'}), name='all-category'),
    path('category/<int:category_id>', views.CategoryAPIView.as_view(), name='category'),
    path('product/category/<int:category_id>/', views.ProductViewSet.as_view({'get': 'get_products_by_category'}), name='products-by-category'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/verify-email/<str:token>/', VerifyEmailAPIView.as_view(), name='api_verify_email'),

]