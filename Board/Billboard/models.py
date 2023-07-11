from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    TYPE = (
        ('tank', 'танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('quest', 'Гилдмастеры'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='static/uploads/')


    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} – {self.datetime}'



