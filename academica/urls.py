from django.urls import path

from . import views

urlpatterns = [
    path('nivel/list', views.nivel_list, name='nivel-list'),
    path('nivel/add', views.nivel_create, name='nivel-add'),
    path('matricula/add',views.matricula_create, name='matricula-add')

]
