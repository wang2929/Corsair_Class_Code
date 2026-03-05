from django.db import models
from .validator import validate_name_format, validate_school_email, validate_combination, validate_locker_number_high, validate_locker_number_low

# Create your models here.
class Student(models.Model):
    name:str = models.CharField(max_length=255, null=False, blank=False, default=None, unique=False, validators=[validate_name_format])
    student_email:str = models.EmailField(null=False, blank=False, default=None, unique=True, validators=[validate_school_email])
    personal_email:str = models.EmailField(default=None, unique=True)
    locker_number:int = models.PositiveSmallIntegerField(null=False, blank=False, default=110, unique=True, validators=[validate_locker_number_low, validate_locker_number_high])
    locker_combination:str = models.CharField(max_length=9, null=False, blank=False, default="12-12-12", unique=False, validators=[validate_combination])
    good_student:bool = models.BooleanField(null=False, blank=False, default=True, unique=False)
    
    def locker_reassignment(self, value):
        self.locker_number = value
        self.save()
        
    def student_status(self, value):
        self.good_student = value
        self.save()
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"