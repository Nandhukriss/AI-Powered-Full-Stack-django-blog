
from django.urls import path

from .import views
urlpatterns = [
    
    path('',views.post,name="home" ),
    path('view',views.view_post,name='view_post'),
    path('delete/<int:id>',views.delete_post,name='delete'),

    path('edit/<int:id>',views.edit_post,name='edit'),
    
    
]
