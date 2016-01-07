from django import forms
from mysite.models import *



class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.first_name, obj.last_name)


class CustomModelChoiceFieldCourse(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.code, obj.name)


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    office = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=13)
    email = forms.EmailField()


class CourseForm(forms.Form):
    name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=10)
    classroom = forms.CharField(max_length=25)
    time = forms.CharField(max_length=100,label='Time (Mon 9:00-12:00 - Wed 13:00-15:00):')
    teacher = CustomModelChoiceField(queryset=Teacher.objects.all())


class EnrollStudents(forms.Form):
    student = CustomModelChoiceField(queryset=Student.objects.all())
    course = CustomModelChoiceFieldCourse(queryset=Course.objects.all())