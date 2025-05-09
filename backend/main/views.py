from .models import Product, Category, EmailVerification
from .serializers import ProductSerializer, CategorySerializer, EmailVerificationSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils import timezone
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .utils import send_confirmation_email

User = get_user_model()


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'success'})


@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email
        })
    return Response({'detail': 'Not authenticated'}, status=401)


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user_model = get_user_model()
    user_data = user_model.objects.get(email=email)
    print(user_data)
    user = authenticate(request, username=user_data.username, password=password)
    if user:
        login(request, user)  # Создаёт сессию
        return Response({'status': 'success'})
    return Response({'status': 'error'}, status=401)


@extend_schema(
    description='Проверка подтверждения почты',
    parameters=[
        OpenApiParameter(
            name='email',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Email адрес для проверки подтверждения',
            required=True,
            examples=[
                OpenApiExample(
                    'Пример email',
                    value='some@mail.ru'
                ),
            ],
        ),
    ],
    responses={
        200: {
            'type': 'object',
            'properties': {
                'status': {
                    'type': 'string',
                    'enum': ['confirmed', 'pending'],
                    'description': 'Статус подтверждения email',
                }
            },
            'example': {
                'status': 'confirmed'
            }
        },
        404: {
            'description': 'Email не найден'
        }
    },
    methods=["GET"]
)
@api_view(['GET'])
def check_confirmation(request):
    print(request.query_params)
    email = request.GET.get('email')
    print(email)
    emailVerification = get_object_or_404(EmailVerification, email=email)

    return Response({
        'status': 'confirmed' if emailVerification.is_verified else 'pending'
    })


class EmailVerificationAPIView(APIView):
    @extend_schema(description="Получение всех категорий",
                   request=EmailVerificationSerializer,
                   responses={200: EmailVerificationSerializer}
                   )
    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        emailVerification = serializer.save()

        send_confirmation_email(emailVerification)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
                }
            }
        },
        examples=[
            OpenApiExample(
                "Пример успешного запроса",
                value={
                    "email": "user@example.com",
                    "password": "securepassword123",
                    "password2": "securepassword123"
                },
                request_only=True
            ),
            OpenApiExample(
                "Пример ответа",
                value={
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
            emailVerification = EmailVerification.objects.get(verification_token=token)
            if (timezone.now() - emailVerification.token_created_at).days > 1:
                return Response(
                    {'error': 'Срок действия ссылки истек'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            emailVerification.is_verified = True
            emailVerification.verification_token = None
            emailVerification.save()

            return Response(
                {'message': 'Email успешно подтвержден!'},
                status=status.HTTP_200_OK
            )
        except EmailVerification.DoesNotExist:
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
