from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, UserResponse
from .forms import ArticleForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import CommentFilter

class ArticlesList(ListView):
    model = Article
    ordering = 'category'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'pk'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('Billboard.add_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('Billboard.change_article',)
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('Billboard.delete_article',)
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class CommentsList(ListView):
    model = UserResponse
    template_name = 'comments.html'
    context_object_name = 'comments'


class CommentDetail(DetailView):
    model = UserResponse
    template_name = 'comment.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'pk'


class CommentCreate(CreateView):
    model = UserResponse
    fields = '__all__'
    template_name = 'comment_create.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        user = request.user
        article_id = kwargs['pk']

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.article = Article.objects.get(pk=article_id)
        return redirect('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.kwargs['pk'])
        return context


class PrivateCommentsList(LoginRequiredMixin,ListView):
    model = UserResponse
    template_name = 'private_comments.html'
    context_object_name = 'private_page'


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


