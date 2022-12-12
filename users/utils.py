from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.template.loader import get_template



def send_password_reset_email(request, user):
    token = user.get_jwt_token(600)
    domain = request.build_absolute_uri('/')[:-1]
    link = domain + reverse('reset_password', args=[token])
    context = {
        'user': user,
        'link': link
    }

    msg_text = get_template("users/email/request_password_reset.txt")
    send_mail(
        'Password reset request',
        msg_text.render(context),
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )


# def send_email_confirmation_email(user):
#     token = user.get_reset_password_token()
#     context = {
#         'user': user,
#         'token': token
#     }

#     send_mail(
#         'Email confirmation',
#         sender=ConfigApp.ADMINS[0],
#         recipients=[user.email],
#         text_body=render_template("auth/email/email_confirmation_email.txt", **context),
#         html_body=render_template("auth/email/email_confirmation_email.html", **context),
#     )