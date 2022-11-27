from django import forms 

class ReviewForm(forms.Form):
    user_name = forms.CharField()
    user_mail = forms.EmailField()
    