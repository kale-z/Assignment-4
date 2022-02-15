from django.shortcuts import render
from mysite.forms import *
from mysite.models import *
from django.http import HttpResponseRedirect

def addastudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
        return render(request, 'addastudent.html', {'form': form, 'title': 'StudentForm'})


def all_students(request):
    return render(request, 'studentslist.html',{'student_list': Student.objects.all(), 'title': 'Students'})


def addateacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office=form.cleaned_data["office"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = TeacherForm()
        return render(request, 'addateacher.html', {'form': form, 'title': 'TeacherForm'})


def all_teachers(request):
    return render(request, 'teacherslist.html',{'teacher_list': Teacher.objects.all(), 'title': 'Teacher'})

def addacourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],
                        code=form.cleaned_data["code"],
                        classroom=form.cleaned_data["classroom"],
                        time=form.cleaned_data["time"],
                        teacher=form.cleaned_data["teacher"])
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = CourseForm()
        return render(request, 'addacourse.html', {'form': form, 'title': 'CourseForm'})


def all_courses(request):
    return render(request, 'courseslist.html',{'course_list': Course.objects.all(), 'title': 'Course'})


def enrollstudents(request):
    if request.method == 'POST':
        form = EnrollStudents(request.POST)
        if form.is_valid():
            form.cleaned_data["course"].students.add(form.cleaned_data["student"])

            return HttpResponseRedirect('/enrolledstudents/'+str(form.cleaned_data["course"].id))
    else:
        form = EnrollStudents()
        return render(request, 'enrollstudents.html', {'form': form, 'title': 'EnrollStudentForm'})


def enrolledstudents(request,id):
    return render(request, 'enrolledstudents.html',{'course': Course.objects.all().filter(id=id)[0], "students": Student.objects.all(), 'title': 'EnrolledStudents'})
