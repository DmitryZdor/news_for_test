from django.contrib import admin
from news_list.models import News
from django.utils.safestring import mark_safe




@admin.register(News)
class NewsListAdmin(admin.ModelAdmin):
    list_display = ( 'title','preview', 'text',  'image','author', 'pub_date' )
    fields = ( ('title','preview'), 'text',  'image','author', 'pub_date' )

    readonly_fields = ('preview', 'pub_date')


    def preview(self,obj):
        if obj.image:
            # return obj.image.width
            if obj.image.width > obj.image.height:
                return mark_safe(f'<img src="{obj.image.url}" style="max-width: 200px;">')
            else:
                return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
        else:
            return 'Загрузите изображение'
    preview.short_description = 'Превью'




