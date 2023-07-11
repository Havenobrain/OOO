from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
from celery import shared_task


@shared_task
def letter_with_news_for_the_week():
    for user in Article.user.objects.all():
        article = Article.object.all
        msg = EmailMultiAlternatives(
            subject=f'Все объявления за неделю {article}',
            from_email='georgij.sergeev98@yandex.ru',
            to=[User.email],)
        html_content = render_to_string(
            'weekly_articles.html',
            {
                'article': article,
                'user': user
            }
                                        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()