from django.urls import path
from . import views


app_name = 'data'
urlpatterns = [
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('add_new_person/', views.add_new_person, name='add_new_person')
]