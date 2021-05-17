from django.urls import path 
from . import views
app_name = 'app'
urlpatterns=[
    path("", views.index, name ='home'),
    path('getintouch/', views.register, name ='getintouch'),
    path('work/', views.work, name = 'work'),
    path('privacy/', views.privacy , name = 'privacy'),
    path('about/', views.about, name = 'about'),
]