from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.utils import timezone
from .serializers import UserRegistrationSerializer

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    @extend_schema(
        description="Регистрация нового пользователя",
        request=UserRegistrationSerializer,
        responses={
            201: UserRegistrationSerializer,
            400: {
                "type": "object",
                "properties": {
                    "error": {"type": "string"},
                    "email": {"type": "array", "items": {"type": "string"}},
                    "username": {"type": "array", "items": {"type": "string"}},
                }
            }
        },
        examples=[
            OpenApiExample(
                "Пример успешного запроса",
                value={
                    "username": "newuser",
                    "email": "user@example.com",
                    "password": "securepassword123",
                    "password2": "securepassword123"
                },
                request_only=True
            ),
            OpenApiExample(
                "Пример ответа",
                value={
                    "username": "newuser",
                    "email": "user@example.com"
                },
                response_only=True
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class VerifyEmailAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @extend_schema(
        description="Подтверждение email пользователя по токену",
        parameters=[
            OpenApiParameter(
                name='token',
                description='Токен подтверждения из email',
                required=True,
                type=str,
                location=OpenApiParameter.PATH
            )
        ],
        responses={
            200: {
                "type": "object",
                "properties": {
                    "message": {"type": "string"}
                }
            },
            400: {
                "type": "object",
                "properties": {
                    "error": {"type": "string"}
                }
            }
        },
        examples=[
            OpenApiExample(
                "Пример успешного ответа",
                value={"message": "Email успешно подтвержден!"},
                status_codes=['200']
            ),
            OpenApiExample(
                "Пример ошибки",
                value={"error": "Срок действия ссылки истек"},
                status_codes=['400']
            )
        ]
    )
    def get(self, request, token):
        try:
            user = User.objects.get(verification_token=token)

            if (timezone.now() - user.token_created_at).days > 1:
                return Response(
                    {'error': 'Срок действия ссылки истек'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.is_verified = True
            user.is_active = True
            user.verification_token = None
            user.save()

            return Response(
                {'message': 'Email успешно подтвержден!'},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {'error': 'Неверная ссылка подтверждения'},
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryViewSet(viewsets.ModelViewSet):
    @extend_schema(description="Получение всех категорий",
                   responses={200: CategorySerializer}
                   )
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryAPIView(APIView):
    @extend_schema(
        description="Получение категории по id",
        responses={200: CategorySerializer}
    )
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class ProductAPIView(APIView):
    @extend_schema(
        description="Получение первого продукта",
        responses={200: ProductSerializer}
    )
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    @extend_schema(
        description="Получение всех продуктов",
        responses={200: ProductSerializer}
    )
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @extend_schema(
        description="Получение списка продуктов по категории",
        responses={200: ProductSerializer(many=True)}
    )
    def get_products_by_category(self, request, category_id):
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
