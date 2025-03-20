from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Post
from django.utils.timezone import now

@shared_task
def send_welcome_email(user_id):
    user = get_user_model().objects.get(id=user_id)
    send_mail(
        'Welcome to the Blog Platform!',
        f'Hi {user.username}, thank you for registering.',
        'from@example.com',
        [user.email]
    )

@shared_task
def generate_daily_post_stats():
    today = now().date()
    posts = Post.objects.filter(created_at__date=today)
    for post in posts:
        print(f"Post '{post.title}' got {post.views} views today.")
