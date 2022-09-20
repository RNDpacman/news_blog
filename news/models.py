from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Новость')

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created',
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        verbose_name='Фото',
    )

    is_published = models.BooleanField(
        default=False, verbose_name='Опубликовано')

    category = models.ForeignKey(
        'Categories',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Категория',
        related_name='get_news',
    )

    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-created_at',)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
        }
        return reverse('full_news', kwargs=kwargs)

    def increment_views_counter(self):
        self.views_count += 1
        self.save()


class Categories(models.Model):
    name = models.CharField(
        max_length=150, db_index=True, verbose_name='Category')
    description = models.TextField(
        max_length=1024, blank=True, verbose_name='Description')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'category_id': self.pk,
        }
        return reverse('news_by_category', kwargs=kwargs)
