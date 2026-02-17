
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('project/',views.project, name = 'project'),
    path('employee/',views.employee, name = 'employee'),
    path('add_employee/',views.add_employee, name = 'add_employee'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('portfolio2/',views.portfolio2, name='portfolio2'),
    path('portfolio2/resume/',views.resume, name='resume')

]