from django.views.decorators.cache import cache_page
from django.urls import path
from .class_views import *
from .views import *

urlpatterns = [
    path('', HomeNewsView.as_view(), name='news'),
    path('category/<int:category_id>/',
         ByCategoryNewsView.as_view(),
         name='news_by_category'
         ),
    path('news/<int:pk>/', FullNewsView.as_view(), name='full_news'),
    path('news/add-news/', AddNewsView.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
]
