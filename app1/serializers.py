from app1.models import Book, School, Student
from rest_framework import serializers

class SchoolSerializers(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class StudentInfoSerializers(serializers.ModelSerializer):
    student_book = BookSerializers(many=True)

    def create(self, validated_data):
        book_data = self.context["book_data"]
        if "student_book" in validated_data:
            validated_data.pop("student_book")
        student_instance = Student.objects.create(**validated_data)
        serializer = BookSerializers(data=book_data,many=True,partial=True)
        if serializer.is_valid():
            serializer.save(student=student_instance)
        else:
            serializer.errors

        return student_instance

    def to_representation(self, instance):
        res = super().to_representation(instance)
        if instance is None:
            res["school"] = ""
            res["school_contact_no"] = str("")
        else:
            res["school"] = instance.school.name
            res["school_contact_no"] = str(instance.school.contact_no)
        return res 

    class Meta:
        model = Student
        fields = "__all__"
        