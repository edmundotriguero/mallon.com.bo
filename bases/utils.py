
from django.core.mail import send_mail
from mallon.settings import EMAIL_HOST_USER


def send_email_generic(request, email, title, body_html ):
    send_mail(
                title,
                 body_html,
                EMAIL_HOST_USER,
                 [email],
                  fail_silently=False,
             )
    send_mail.send()

    #return True