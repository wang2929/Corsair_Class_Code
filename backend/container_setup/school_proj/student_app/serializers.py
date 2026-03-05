from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    """
    fields =
      1. list of str where each str represents an attribute
      2. dunder str stating all to return all attributes
    """
    class Meta:
        model = Student     # specify which model the serializer is for
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']    # can use exclude to not include one field
                            # Have to provide either feilds or exclude but not both