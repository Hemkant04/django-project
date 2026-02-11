
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('project/',views.project, name = 'project'),
    path('employee/',views.employee, name = 'employee'),
    path('add_employee/',views.add_employee, name = 'add_employee'),
    path('portfolio/',views.portfolio, name='portfolio')

]