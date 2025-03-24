from django import forms
from .models import *

class Gender_form(forms.ModelForm):

    class Meta:
        model = Gender
        fields = "__all__"

class Fees_form(forms.ModelForm):
    
    class Meta:
        model = courses
        fields = ['Price']

class students_form(forms.ModelForm):
    gender_opt = Gender_form()
    class Meta:
        model = students
        fields = ['Name','gender','Mobile_no','Address','Selected_course','batch','duration']
    # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # gender = forms.ChoiceField( choices=[gender_opt], required=False)(widget=forms.ChoiceField(attrs={'class': 'form-control'}))
    # Mobile_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Selected_course = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # batch = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # duration = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class Billing_form(forms.ModelForm):

    class Meta:
        model = billing
        fields= "__all__"
class Accounts_Form(forms.ModelForm):
    
    class Meta:
        model = expences
        fields = ["date",'opening_balance','Expence_detail','Expence_Amount','Total_Expences','closing_balance']
