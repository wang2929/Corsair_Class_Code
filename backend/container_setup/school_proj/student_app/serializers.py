from rest_framework import serializers as s
from .models import Student, Subject, Grade
from django.db.models import Avg
from .utilities import NounProjectAPI

"""
fields =
    1. list of str where each str represents an attribute
    2. dunder str stating all to return all attributes
"""
class SubjectSerializer(s.ModelSerializer):
    img = s.SerializerMethodField()
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'img']
    
    def get_img(self, obj):
        subject = obj.subject_name
        np_api = NounProjectAPI()
        return np_api(subject)

class SubjectAllSerializer(s.ModelSerializer):
    grade_average = s.SerializerMethodField()
    students = s.SerializerMethodField()
    img = s.SerializerMethodField()
    #student_set = StudentSerializer(many=True)
    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average', 'img']
    
    def get_grade_average(self, obj):
        average = obj.grade_set.aggregate(Avg('grade', default=0))['grade__avg']
        return round(average, 2)
    
    def get_students(self, obj):
        return obj.student_set.count()
    
    def get_img(self, obj):
        subject = obj.subject_name
        np_api = NounProjectAPI()
        return np_api(subject)

class StudentSerializer(s.ModelSerializer):
    img = s.SerializerMethodField()
    class Meta:
        model = Student     # specify which model the serializer is for
        fields = ['name', 'student_email', 'locker_number', 'img']
    
    def get_img(self, obj):
        np_api = NounProjectAPI()
        return np_api("student")

class GradeSerializer(s.ModelSerializer):
    student = StudentSerializer()
    a_subject = s.StringRelatedField()
    img = s.SerializerMethodField()
    class Meta:
        model = Grade
        fields = ['grade', 'student', 'a_subject', 'img']
        
    def get_img(self, obj):
        np_api = NounProjectAPI()
        return np_api("grade")

class StudentAllSerializer(s.ModelSerializer):
    subjects = SubjectAllSerializer(many=True)
    img = s.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email', 'locker_number',
                  'locker_combination', 'good_student', 'subjects', 'img']
    
    def get_img(self, obj):
        np_api = NounProjectAPI()
        return np_api("student")