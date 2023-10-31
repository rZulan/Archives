from django.urls import path

from . import views

urlpatterns = [
    path('', views.Documents.as_view(), name='index'),
    path('<int:pk>', views.Document.as_view(), name='document')
]
