from rest_framework import serializers as s
from .models import Student, Subject, Grade
from django.db.models import Avg

"""
fields =
    1. list of str where each str represents an attribute
    2. dunder str stating all to return all attributes
"""
class SubjectSerializer(s.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor']

class SubjectAllSerializer(s.ModelSerializer):
    grade_average = s.SerializerMethodField()
    students = s.SerializerMethodField()
    #student_set = StudentSerializer(many=True)
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']
    
    def get_grade_average(self, obj):
        average = obj.grade_set.aggregate(Avg('grade', default=0))['grade__avg']
        return round(average, 2)
    
    def get_students(self, obj):
        return obj.student_set.count()

class StudentSerializer(s.ModelSerializer):
    class Meta:
        model = Student     # specify which model the serializer is for
        fields = ['name', 'student_email', 'locker_number']

class GradeSerializer(s.ModelSerializer):
    student = StudentSerializer()
    a_subject = s.StringRelatedField()
    class Meta:
        model = Grade
        fields = ['grade', 'student', 'a_subject']

class StudentAllSerializer(s.ModelSerializer):
    subjects = SubjectAllSerializer(many=True)
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email', 'locker_number',
                  'locker_combination', 'good_student', 'subjects']