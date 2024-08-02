# scheduler_app/forms.py
"""
# scheduler_app/forms.py

from django import forms
from .models import ScheduledPost

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['text', 'image', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class MultipleFileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) 


# scheduler_app/forms.py

from django import forms
from .models import ScheduledPost

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['text', 'image', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileUploadForm(forms.Form):
    files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}))
""" 
# scheduler_app/forms.py

# scheduler_app/forms.py


# scheduler_app/forms.py

# scheduler_app/forms.py
"""
from django import forms
from .models import ScheduledPost

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['text', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class MultipleFileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


# scheduler_app/forms.py

from django import forms
from .models import ScheduledPost

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['text', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class MultipleFileUploadForm(forms.Form):
    files = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
"""  


from django import forms
from .models import ScheduledPost

class ScheduledPostForm(forms.ModelForm):
    class Meta:
        model = ScheduledPost
        fields = ['text', 'image', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }




  

