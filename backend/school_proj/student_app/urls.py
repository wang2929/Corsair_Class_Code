from django.urls import path, register_converter
from .views import AllStudents, AllSubjects, AllGrades, AStudent, ASubject
from .converter import IntOrStrConverter

register_converter(IntOrStrConverter, "int_or_str")

urlpatterns = [
    # Currently only takes GET requests
    path('students/', AllStudents.as_view(), name='all_students'),
    path('students/<int_or_str:val>', AStudent.as_view(), name='a_student'),
    path('subjects/', AllSubjects.as_view(), name='all_subjects'),
    path('subjects/<int_or_str:val>', ASubject.as_view(), name='a_subject'),
    path('grades/', AllGrades.as_view(), name='all_grades')
]