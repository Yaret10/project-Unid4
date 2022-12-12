from django import forms
from .models import Projects

class FormProjects(forms.Form):
    class Meta:
        model = Projects
        fields = ["Photo","Title","Description","Tags","url_gitHub"]
