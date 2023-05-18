from django.shortcuts import render

from news_list.models import News


def index(request):
    news = News.objects.all()
    template = 'news_list/index.html'
    title = 'NEWS'
    return render(request, template, context={'news': news,
                                                  'title': title, }

                  )

# class OrderCreateView(TitleMixin, CreateView):
#     template_name = 'news_list/news_page.html'
#     form_class = NewsForm
#     title = 'Новость'
#     success_url = reverse_lazy('news_list:index')
