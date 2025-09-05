from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('categories/', views.categories,name='categories'),
    path('catView/<str:slug>', views.catView,name='catView'),
    path('blog/<str:cat_slug>/<str:post_slug>', views.blog_view,name='blog_view'),
]
