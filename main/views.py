from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Publications, Student, Teacher
from .forms import (
    BookForm,
    AuthorForm,
    PublicationForm,
    StudentForm,
    TeacherForm,
    UserSignUpForm,
)
from django.contrib.auth.models import User

# Create your views here.


def stu(request):
    if request.method == "POST":
        uform = UserSignUpForm(request.POST)
        sform = StudentForm(request.POST)
        if uform.is_valid() and sform.is_valid():
            user = uform.save()
            user.first_name = uform.cleaned_data["first_name"]
            user.last_name = uform.cleaned_data["last_name"]
            user.username = uform.cleaned_data["username"]
            user.password = uform.cleaned_data["password"]
            user.save()
            ### Creating Student ###
            student = sform.save(commit=False)
            student.user = user
            student.roll = sform.cleaned_data["roll"]
            student.save()
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        uform = UserSignUpForm()
        sform = StudentForm()
    d = {"uform": uform, "sform": sform}
    return render(request, "student.html", d)


def detail(request):
    data = Teacher.objects.get(user_id=12)
    d = {"data": data}
    return render(request, "data.html", d)


def tchr(request):
    if request.method == "POST":
        uform = UserSignUpForm(request.POST)
        tform = TeacherForm(request.POST)
        if uform.is_valid() and tform.is_valid():
            user = uform.save()
            user.first_name = uform.cleaned_data["first_name"]
            user.last_name = uform.cleaned_data["last_name"]
            user.username = uform.cleaned_data["username"]
            user.password = uform.cleaned_data["password"]
            user.save()
            ### Creating Teacher ###
            teacher = Teacher(user=user)
            for i in tform.cleaned_data["students"]:
                teacher.students.set([i])
            teacher.save()
            """
            teacher = tform.save(commit=False)
            teacher.user = user
            for i in tform.cleaned_data["students"]:
                teacher.students.set([i])
            teacher.save()
            # teacher.students = tform.cleaned_data["students"]
            """
            return HttpResponse("ok")
        else:
            return HttpResponse("error")
    else:
        uform = UserSignUpForm()
        tform = TeacherForm()
    d = {"uform": uform, "tform": tform}
    return render(request, "teacher.html", d)


def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    d = {"form": form}
    return render(request, "authorform.html", d)


def book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    d = {"form": form}
    return render(request, "bookform.html", d)


def publication(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PublicationForm()
    d = {"form": form}
    return render(request, "pubform.html", d)
