from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='list'),
    path('base/', views.student_list, name='base'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
]
