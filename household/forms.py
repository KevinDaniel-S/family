from django import forms
from .models import Family

class FamilyCreationForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name', )
        labels = {
                'name':'Family name',
                }

    def clean_name(self):
        cd = self.cleaned_data
        user = cd['name'].capitalize()
        return user

