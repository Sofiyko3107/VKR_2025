# utils.py
from django.core.mail import send_mail
from secrets import token_urlsafe
from django.conf import settings


def generate_confirmation_token():
    return token_urlsafe(32)


def send_confirmation_email(emailVerification):
    token = generate_confirmation_token()
    emailVerification.verification_token = token
    emailVerification.save()

    confirmation_link = f"{settings.FRONTEND_URL}/confirm-email?token={token}"

    send_mail(
        'Подтвердите ваш email',
        f'Перейдите по ссылке для подтверждения: {confirmation_link}',
        settings.EMAIL_HOST_USER,
        [emailVerification.email],
        fail_silently=False,
    )
