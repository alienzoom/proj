from django import forms
from .models import Project, ProjectRequirement

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'team_activities', 'work_conditions',
            'start_date', 'end_date', 'budget'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'team_activities': forms.Textarea(attrs={'rows': 4}),
            'work_conditions': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectRequirementForm(forms.ModelForm):
    class Meta:
        model = ProjectRequirement
        fields = [
            'skill_name', 'level_requirement', 'work_condition',
            'people_count', 'is_mandatory', 'price'
        ]


# Форма для быстрого создания требования (AJAX)
class QuickRequirementForm(forms.Form):
    skill_name = forms.CharField(max_length=200)
    level = forms.ChoiceField(choices=ProjectRequirement.SKILL_LEVEL_CHOICES, required=False)
    people_count = forms.IntegerField(min_value=1, initial=1)