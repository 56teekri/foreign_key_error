from django import forms
from .models import Book, Author, Publications, Teacher, Student
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["students"]


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password",
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publications
        fields = "__all__"
