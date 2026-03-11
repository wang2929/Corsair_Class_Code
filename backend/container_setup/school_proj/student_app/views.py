from django.shortcuts import render
from .models import Student, Subject, Grade
from .serializers import StudentAllSerializer, SubjectAllSerializer, GradeSerializer, StudentSerializer, SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

# Create your views here.
class AllStudents(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.objects.all(), many=True)
        return Response(students.data)

class AllSubjects(APIView):
    def get(self, request):
        subjects = SubjectAllSerializer(Subject.objects.all(), many=True)
        return Response(subjects.data)

class AllGrades(APIView):
    def get(self, request):
        grades = GradeSerializer(Grade.objects.order_by('a_subject'), many=True)
        return Response(grades.data)

class AStudent(APIView):
    def single_student(self, val):
        try:
            if isinstance(val, int):
                return Student.objects.get(id=val)
            return Student.objects.get(name__icontains=val)
        except:
            return { 'errors':"Error - many students found"} 
        
    def get(self, request, val):
        student = StudentSerializer(self.single_student(val))
        try:
            return Response(student.data)
        except:
            return Response(student, status=HTTP_400_BAD_REQUEST)
    
    def put(self, request, val):
        # using locker_number for now for lookup, but should change to ID later
        student = StudentSerializer(self.single_student(val), data=request.data, partial=True)
        if student.is_valid():
            student.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return Response(student.error, status=HTTP_400_BAD_REQUEST)

class ASubject(APIView):
    def single_subject(self, val):
        try:
            if isinstance(val, int):
                return Subject.objects.get(id=val)
            return Subject.objects.get(subject_name__icontains=val)
        except:
            return { 'errors':"Error - many students found"} 
        
    def get(self, request, val):
        subject = SubjectSerializer(self.single_subject(val))
        try:
            return Response(subject.data, status=HTTP_200_OK) 
        except:
            return Response(subject.errors, status=HTTP_400_BAD_REQUEST)