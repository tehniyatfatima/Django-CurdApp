from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single-emp/<int:emp_id>', views.singleEmpData, name='single-emp-data'),
    path('update/<int:emp_id>', views.updateEmp, name='update'),
    path('delete/<int:emp_id>', views.deleteEmp, name='delete'),
]