from django.contrib import admin
from news_list.models import News


@admin.register(News)
class NewsListAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    def preview(self, obj):
        return 'Hello!!'


