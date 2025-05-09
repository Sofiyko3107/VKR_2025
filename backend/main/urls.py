from django.urls import path
from . import views
from .views import RegisterAPIView, VerifyEmailAPIView, ProductViewSet, EmailVerificationAPIView, check_confirmation

urlpatterns = [
    path('product/<int:product_id>/', views.ProductAPIView.as_view(), name='product-by-id'),
    path('product/all/', views.ProductViewSet.as_view({'get': 'list'}), name='all-products'),
    path('product/category/<int:category_id>/', views.ProductViewSet.as_view({'get': 'get_products_by_category'}),
         name='products-by-category'),
    path('category/all/', views.CategoryViewSet.as_view({'get': 'list'}), name='all-category'),
    path('category/<int:category_id>', views.CategoryAPIView.as_view(), name='category'),
    path('register', RegisterAPIView.as_view(), name='api_register'),
    path('verify-email/<str:token>/', VerifyEmailAPIView.as_view(), name='api_verify_email'),
    path('send-confirmation-message', EmailVerificationAPIView.as_view(), name='api_verify_email'),
    path('check-confirmation', check_confirmation, name='api_check_confirmation'),
    path('login', views.login_view, name='login'),
    path('profile', views.current_user, name='profile'),
    path('logout', views.logout_view, name='logout'),
]