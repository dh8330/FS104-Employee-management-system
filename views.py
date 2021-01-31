from rest_framework import generics
from .models import Roles, Department, Manager, Employee, Rating, Appraisal
from .serializers import RolesSerializer, DepartmentSerializer, ManagerSerializer, EmployeeSerializer, RatingSerializer, AppraisalSerializer

class RolesAPIView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class DepartmentAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ManagerAPIView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class AppraisalAPIView(generics.ListCreateAPIView):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer