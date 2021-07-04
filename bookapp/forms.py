
from django.forms import ModelForm
from .models import BookModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookCreateForm(ModelForm):
    class Meta:
        model = BookModel
        fields = "__all__"


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]