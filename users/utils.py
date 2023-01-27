from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.template.loader import get_template
from django.contrib import messages

from smtplib import SMTPServerDisconnected


# email address to send emails from
EMAIL_HOST_USER = settings.EMAIL_HOST_USER


def send_password_reset_email(request, user):
    token = user.get_jwt_token(expires_in=600)
    domain = request.build_absolute_uri('/')[:-1]
    link = domain + reverse('reset_password', args=[token])
    context = {
        'user': user,
        'link': link
    }

    msg_text = get_template("users/email/request_password_reset.txt")
    print("from ", EMAIL_HOST_USER)
    print(msg_text.render(context))
    try:
        send_mail(
            'Password reset request',
            msg_text.render(context),
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        messages.add_message(
            request, messages.INFO,
            message=(
                f"Please check your email '{user.email}' to "
                "confirm your account and set your password"
                ),
            extra_tags="info"
        )
        print("email sent !")
    except SMTPServerDisconnected as e:
        messages.add_message(
            request,
            messages.ERROR,
            message=(
                "An error occured while sending the email, "
                "but your account has been created. "
                "Please use login / 'forgot password' "
                "to recieve a new email."
            ),
            extra_tags="danger")
        print("SMTPServerDisconnected: ", e)


def send_confirm_email(request, user):
    token = user.get_jwt_token(expires_in=600)
    domain = request.build_absolute_uri('/')[:-1]
    link = domain + reverse('confirm_email', args=[token])
    context = {
        'user': user,
        'link': link
    }

    msg_text = get_template("users/email/confirm_email.txt")
    send_mail(
        'Confirm your new email',
        msg_text.render(context),
        EMAIL_HOST_USER,
        [user.unconfirmed_email],
        fail_silently=False,
    )
