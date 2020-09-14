from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    #int will capture any intergers and send it to the views.blog method
    #with the int value be accessed in blog_id variable
    path('<int:blog_id>', views.blog, name = 'detail'),
]
