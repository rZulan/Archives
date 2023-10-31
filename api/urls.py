from django.urls import path

from . import views

urlpatterns = [
    path('', views.documents, name='index'),
    path('create', views.document_create, name='create_document'),
    path('<int:pk>', views.document, name='document')
]
