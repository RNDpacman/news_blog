from django.contrib import admin
from .models import News, Categories
from django.utils.safestring import mark_safe
from news.forms import CkeditorAdminForm


class NewsAdmin(admin.ModelAdmin):
    form = CkeditorAdminForm
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'updated_at',
        'is_published',
        'get_photo',
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)
    save_on_top = True
    save_as = True

    fields = (
        'title',
        'content',
        'category',
        'created_at',
        'is_published',
        'updated_at',
        'views_count',
        'photo',
        'get_photo',
    )
    readonly_fields = (
        'updated_at',
        'created_at',
        'views_count',
        'get_photo',
    )

    @admin.display(empty_value='Пусто', description='Картинка')
    def get_photo(self, obj):
        if obj.photo:
            photo_html = f'<img src="{obj.photo.url}" width="100">'
            return mark_safe(photo_html)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.site_title = 'Администрирование Новостей'
admin.site.site_header = 'Администрирование Новостей'
