from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [

    path('admin/', admin.site.urls, name='admen'),
    path('', views.main1, name='hello'),
    path('Home', views.index, name='home'),
    path('Education', views.me, name='education'),
    path('Projects', views.projects, name='projects'),
    path('Game', views.game, name='game'),
    path('Reviews', views.reviews, name='reviews'),
    path('Add Reviews', views.btnrev, name='bd')

]