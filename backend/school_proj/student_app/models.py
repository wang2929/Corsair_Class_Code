from django.db import models
from .validator import (validate_name_format, 
                        validate_school_email, 
                        validate_combination, 
                        validate_locker_number_high, 
                        validate_locker_number_low, 
                        validate_subject_name, 
                        validate_professor_name, 
                        validate_high_grade, 
                        validate_low_grade)

# Create your models here.
class Subject(models.Model):
    subject_name:str = models.CharField(
        null=False,
        blank=False,
        default=None,
        unique=True,
        validators=[validate_subject_name]
    )
    professor:str = models.CharField(
        blank=False,
        null=False,
        default="Professor Cahan",
        unique=False,
        validators=[validate_professor_name]
    )
    
    def add_a_student(self, val):
        if len(self.student_set.all()) < 31:
            self.student_set.add(val)
        else:
            raise Exception("This subject is full!")
    
    def drop_a_student(self, val):
        if len(self.student_set.all()) == 0:
            raise Exception("This subject is empty!")
        else:
            self.student_set.remove(val)
    
    def __str__(self):
        return f"{self.subject_name}-{self.professor}-{len(self.student_set.all())}"
    

class Student(models.Model):
    name:str = models.CharField(
        max_length=255, 
        null=False, 
        blank=False, 
        default=None, 
        unique=False, 
        validators=[validate_name_format])
    student_email:str = models.EmailField(
        null=False, 
        blank=False, 
        default=None, 
        unique=True, 
        validators=[validate_school_email])
    personal_email:str = models.EmailField(
        default=None, 
        unique=True)
    locker_number:int = models.PositiveSmallIntegerField(
        null=False, 
        blank=False, 
        default=110, 
        unique=True, 
        validators=[validate_locker_number_low, validate_locker_number_high])
    locker_combination:str = models.CharField(
        max_length=9, 
        null=False, 
        blank=False, 
        default="12-12-12", 
        unique=False, 
        validators=[validate_combination])
    good_student:bool = models.BooleanField(
        null=False, 
        blank=False, 
        default=True, 
        unique=False)
    subjects = models.ManyToManyField(
        Subject, 
        through="Grade")
    
    def locker_reassignment(self, value):
        self.locker_number = value
        self.save()
        
    def student_status(self, value):
        self.good_student = value
        self.save()
    
    def add_subject(self, subject):
        if len(self.subjects.all()) >= 8:
            raise Exception("This students class schedule is full!")
        else:
            self.subjects.add(subject)
    
    def remove_subject(self, subject):
        if len(self.subjects.all()) == 0:
            raise Exception("This students class schedule is empty!")
        else:
            self.subjects.remove(subject)
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

class Grade(models.Model):
    grade = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=100,
        blank=False,
        null=False,
        validators=[validate_low_grade, validate_high_grade])
    a_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["a_subject", "student"], name="unique_student_subject"
    #         )
    #     ]
    
    def __str__(self):
        return f"{self.student.name}-{self.a_subject.subject_name}-{self.grade}"