from django.urls import path
from .views import emp, show, edit, update, destroy  

urlpatterns = [
    path('', emp, name='emp'), 
    path('show/', show, name='show'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', destroy, name='delete'),
]
