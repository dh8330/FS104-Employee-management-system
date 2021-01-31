from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'Roles', views.RolesAPIView.as_view(), name='Roles-list'),
    path(r'Department', views.DepartmentAPIView.as_view(), name='Department-list'),
    path(r'Manager', views.ManagerAPIView.as_view(), name='Manager-list'),
    path(r'Employee', views.EmployeeAPIView.as_view(), name='Employee-list'),
    path(r'Rating', views.RatingAPIView.as_view(), name='Rating-list'),
    path(r'Appraisal', views.AppraisalAPIView.as_view(), name='Appraisal-list')
]