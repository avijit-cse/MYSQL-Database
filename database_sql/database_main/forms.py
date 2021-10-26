from django import forms
from database_main import models

class newfrom(forms.ModelForm):
    class Meta:
        model = models.mugisian
        fields = "__all__"

class albumfrom(forms.ModelForm):
    class Meta:
        model = models.album
        fields = "__all__"