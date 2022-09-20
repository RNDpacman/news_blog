from .models import News, Categories
from .forms import AddNewsForm
from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from antiblog import settings


class AddNewsView(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AddNewsForm
    template_name = 'news/add_news.html'


class FullNewsView(DetailView):
    model = News
    template_name = 'news/full_news.html'

    def get_object(self, queryset=None):
        '''
        Increment views counter
        '''
        item = super().get_object(queryset)
        item.increment_views_counter()
        return item


class HomeNewsView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'all_news'
    queryset = News.objects.filter(
        is_published=True
    ).select_related('category')
    paginate_by = settings.PAGINATE_BY
    extra_context = {'title': 'Главная'}


class ByCategoryNewsView(ListView):
    model = News
    context_object_name = 'all_news_by_category'
    template_name = 'news/news_by_category.html'
    paginate_by = settings.PAGINATE_BY

    def get_category(self):
        category_id = self.kwargs['category_id']
        category = Categories.objects.get(pk=category_id)
        return category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context

    def get_queryset(self):
        categories = self.model.objects.filter(
            category_id=self.kwargs['category_id'],
            is_published=True,
        ).select_related('category')

        return get_list_or_404(categories)
