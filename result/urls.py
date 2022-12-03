from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.GetData, name='GetData'),
    path('download/', views.DownloadPDF, name='DownloadPDF'),
]