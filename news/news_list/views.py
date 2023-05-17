from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from news_list.forms import NewsForm


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'news_list/index.html'
    title = 'NEWS'



class OrderCreateView(TitleMixin, CreateView):
    template_name = 'news_list/news_page.html'
    form_class = NewsForm
    title = 'Новость'
    success_url = reverse_lazy('news_list:index')