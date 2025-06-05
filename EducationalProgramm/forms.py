from .models import EducationProgram
from django.forms import ModelForm, TextInput, NumberInput, Select, CheckboxInput, Textarea


class EducationProgramForm(ModelForm):
    class Meta:
        model = EducationProgram
        fields = ['name', 'year','course','module','discipline','is_team', 'description']

        
            

        widgets = {
            "name": TextInput(attrs={
                'class': "form-control",
                'placeholder' : 'Введите название'    
            }),
             "year": NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Год'
            }),
            'course': Select(choices=EducationProgram.COURSE, attrs={
                'class': 'form-control'
            }),
           'module': Select(choices=EducationProgram.MODULE, attrs={
                'class': 'form-control'
            }),
            "discipline": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название предмета'
            }),
            "is_team": CheckboxInput(attrs={
                'class': "form-check-input"
            }),
            "description": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Краткая справка по проекту',
                'rows': 4
            })
            
        }