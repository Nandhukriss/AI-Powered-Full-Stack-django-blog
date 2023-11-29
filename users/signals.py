# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User

# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string


# @receiver(post_save, sender=User)
# def send_registration_email(sender, instance, created, **kwargs):
#     if created:
#         email_template = 'account_created.html'
#         email_body = render_to_string(
#             email_template, {'customer': instance.username})
#         subject = 'Welcome to Your E-commerce App'
#         from_email = 'nandhu.r.s.krishna@gmail.com'
#         recipient_list = [instance.email]
#         email = EmailMessage(subject, email_body, from_email, recipient_list)
#         email.content_subtype = 'html'
#         email.send()
