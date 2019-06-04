from django import forms
from models import Profile, Blog, Images
from django_markdown.fields import MarkdownFormField

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = True,
        label = 'Username',
        max_length = 32
    )
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = True,
        label = 'First name',
        max_length = 32
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = True,
        label = 'Last name',
        max_length = 32
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    repeat_password = forms.CharField(
        required=True,
        label = 'Repeat Password',
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required = True,
        #label = 'Username',
        max_length = 32
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required = True,
        #label = 'Password',
        max_length = 32,
    )

class editProfileForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ['bio', 'instagram', 'fb', 'website', 'twitter']
    

class newBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'info', 'cover']   


class newPostForm(forms.Form):
    title = forms.CharField(
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=True,
            label='Title',
            max_length=50
        )

    info = MarkdownFormField(
            widget=forms.TextInput(attrs={'id': 'mdField', 'class': 'form-control'}),
            required = False,
            label = 'Short description',
            max_length = 5000,
        )


class addToGaleryForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']