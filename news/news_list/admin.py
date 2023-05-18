from django.contrib import admin
from news_list.models import News
from django.utils.safestring import mark_safe




@admin.register(News)
class NewsListAdmin(admin.ModelAdmin):

    readonly_fields = ('preview', 'pub_date')

    def preview(self,obj):

        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
    preview.short_description = 'Превью'




