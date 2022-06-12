from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import *
from .serializers import BookSerializers, SchoolSerializers, StudentInfoSerializers, StudentSerializers

# Create your views here.

class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentInfoViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'first_name']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if "student_book" in self.request.data:
            context.update({"book_data":self.request.data["student_book"]})
            print(context)
        return context 

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers 
