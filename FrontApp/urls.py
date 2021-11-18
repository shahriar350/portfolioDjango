from . import views
from django.urls import path

app_name = 'page'

urlpatterns = [
    path('',views.indexPage,name='index'),
    path('blog/',views.BlogPage.as_view(),name='blog'),
    path('blog/<int:id>',views.blog_single,name='single.blog'),
]