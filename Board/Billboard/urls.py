from django.urls import path
from .views import ArticlesList, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete, CommentCreate, CommentsList, PrivateCommentsList


urlpatterns = [
   path('', ArticlesList.as_view(), name='article_list'),
   path('<int:pk>', ArticleDetail.as_view(), name='article_detail',),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'),
   path('<int:pk>/allcommnets/', CommentsList.as_view(), name='all_comments'),
   path('private/', PrivateCommentsList.as_view(), name='private_comments'),
]
