from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_activation_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    activation_path = f"/accounts/activate/{uid}/{token}/"
    activation_url = request.build_absolute_uri(activation_path)

    context = {
        "user": user,
        "activation_url": activation_url,
        "site_name": "Football Chants",
    }
    subject = render_to_string("registration/activation_email_subject.txt", context).strip()
    message = render_to_string("registration/activation_email.txt", context)

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
