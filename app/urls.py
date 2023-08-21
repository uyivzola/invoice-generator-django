from django.urls import path
from .views import pdf,index,buy


urlpatterns = [
    path('', index, name='index'),
    path('buy/<int:pk>/', buy, name='buy'),
    path('pdf/', pdf, name='pdf'),
]

