
from django.urls import path

from .import views
urlpatterns = [
    
    path('post',views.post,name="home" ),
    path('',views.view_post,name='view_post'),
    path('post_detail/<int:id>',views.post_detail,name='post_detail'),
    path('delete/<int:id>',views.delete_post,name='delete'),

    path('edit/<int:id>',views.edit_post,name='edit'),
    
    
]
