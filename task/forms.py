from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from task.models import Tasklist
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
  
    class Meta:
        model = User
        fields =['username','email']
        labels ={'email':'Email'}
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))



class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = ['title','status','schedule']
        widgets = {
            'schedule':forms.TimeInput(attrs={'type':'time'})
        }

class UpdateProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    profilepic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}),required=False)
    
    class Meta:
        models = User
        fields = ['username', 'first_name', 'last_name', 'email']

    