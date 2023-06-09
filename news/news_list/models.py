from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.utils.safestring import mark_safe

class News(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок',
                            help_text='Введите название')
    text = tinymce_models.HTMLField(verbose_name='ТЕКСТ НОВОСТИ',
                            help_text='Введите текст')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='ДАТА',
                                    help_text='дата опубликования'
                                    )

    image = models.ImageField(upload_to='news_images', null=True, blank=True)

    author = models.ForeignKey(to=User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                            )

    def __str__(self):
        return mark_safe(self.text[:100])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        ordering = ['-pub_date']

