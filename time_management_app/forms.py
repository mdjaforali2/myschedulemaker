from django import forms
from django.core.exceptions import ValidationError
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category', 'task_name', 'starting_time', 'ending_time', 'priority', 'status', 'description', 'starting_date', 'ending_date', 'days_of_week']

        widgets = {
            'starting_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'ending_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'starting_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ending_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        starting_time = cleaned_data.get('starting_time')
        ending_time = cleaned_data.get('ending_time')
        starting_date = cleaned_data.get('starting_date')
        ending_date = cleaned_data.get('ending_date')

        if starting_date and ending_date:
            # Ensure starting_date is not ahead of ending_date
            if starting_date > ending_date or (starting_date == ending_date and starting_time >= ending_time):
                raise ValidationError("Starting date and time cannot be ahead of or equal to ending date and time.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['starting_time'].label = 'Starting Time'
        self.fields['ending_time'].label = 'Ending Time'
        self.fields['starting_date'].label = 'Starting Date'
        self.fields['ending_date'].label = 'Ending Date'

        # Add Bootstrap classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
