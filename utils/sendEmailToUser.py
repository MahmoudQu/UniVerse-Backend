from django.core.mail import send_mail

def send_email_to_user(user_email, title, content):
    send_mail(
        f'{title}',
        f'{content}',
        'jouniversejo@gmail.com',
        [user_email],
        fail_silently=False,
    )
