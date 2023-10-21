from django.urls import path
from pet import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bichos", views.bichos, name="bichos"),
    path('pets/new', views.cad_pets, name='cad_pets'),
    path('pets/save', views.save_pets, name='save_pets'),
    #path('pets/edit/<int:pk>', views.edit_pets, name="edit_pets"),
    path('pets/update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>', views.deletar_animal, name="deletar_animal"),
]