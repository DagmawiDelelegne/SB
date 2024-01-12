from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms 

from .choices import CAMPUS_CHOICES
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    campus = forms.ChoiceField(choices=CAMPUS_CHOICES, required=True)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3, 'cols' : 30}), required=False)
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'campus', 'bio', 'profile_image']

# - login a user
        
class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())

# - search bar
class BookSearchForm(forms.Form):
     search_query = forms.CharField(label="Search for books", max_length= 100)

# - add a book
class BookForm(forms.Form):
     title = forms.CharField(max_length=255)
     author = forms.CharField(max_length=255)
     course = forms.CharField(max_length=255)
