from django import forms
from .models import Profile,webapps,ratings,comment

class profileform(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','pub_date']


class ratingsform(forms.ModelForm):
    class Meta:
        model=ratings
        exclude=['webapp','user','average']
    
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        exclude=['webapp','user']



class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class webappsform(forms.ModelForm):
    class Meta:
        model=webapps
        exclude=['profile','user','pub_date']
  