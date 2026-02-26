from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('cats/', views.cat_index, name='cat-index'),
    path('cats/', views.CatList.as_view(), name='cat-index'),
    path('cats/create', views.CatCreate.as_view(), name='cat-create' ),
    path('cats/<int:pk>', views.cat_detail, name='cat-detail'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:cat_id>/associate-toy/<int:toy_id>', views.associate_toy, name='associate-toy'),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete', views.CatDelete.as_view(), name='cat-delete'),
    path('toys/create', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name='toy-delete'),
    path('toys/', views.ToyList.as_view(), name='toy_list'),
]