from django.shortcuts import render
from mysite.forms import *
from mysite.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

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
        return render_to_response('addastudent.html', {'form': form}, RequestContext(request))


def all_students(request):
    return render_to_response('studentslist.html',{'student_list': Student.objects.all()})


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
        return render_to_response('addateacher.html', {'form': form}, RequestContext(request))


def all_teachers(request):
    return render_to_response('teacherslist.html',{'teacher_list': Teacher.objects.all()})

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
        return render_to_response('addacourse.html', {'form': form}, RequestContext(request))


def all_courses(request):
    return render_to_response('courseslist.html',{'course_list': Course.objects.all()})


def enrollstudents(request):
    if request.method == 'POST':
        form = EnrollStudents(request.POST)
        if form.is_valid():
            form.cleaned_data["course"].students.add(form.cleaned_data["student"])

            return HttpResponseRedirect('/enrolledstudents/'+str(form.cleaned_data["course"].id))
    else:
        form = EnrollStudents()
        return render_to_response('enrollstudents.html', {'form': form}, RequestContext(request))


def enrolledstudents(request,id):
    return render_to_response('enrolledstudents.html',{'course': Course.objects.all().filter(id=id)[0], "students": Student.objects.all()})
