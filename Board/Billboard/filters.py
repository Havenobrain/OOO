from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import UserResponse, Article


class CommentFilter(FilterSet):
       model = UserResponse
       article = ModelChoiceFilter(
           field_name='article__title',
           queryset=Article.objects.all(),
           label='Title',
       )
