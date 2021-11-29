from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    Repeat_password = forms.CharField(label='Repeat_password', widget=forms.PasswordInput)
    class_num = forms.CharField(label = 'class_num', widget=forms.NumberInput)

    class meta:
        model = User
        fields = ['username', 'password', 'class_num' ]


    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Repeat_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['Repeat_password']