from django import forms
from .models import JobRequirement

class JobRequirementForm(forms.ModelForm):
    class Meta:
        model = JobRequirement
        fields = [
            'title', 
            'description',
            'skills_required',
            'workers_needed', 
            'daily_wage', 
            'location', 
            'start_date',
            'duration_days',
            'provides_housing', 
            'provides_meals', 
            'provides_medical'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm', 'rows': 3}),
            'skills_required': forms.TextInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'workers_needed': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'daily_wage': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'location': forms.TextInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'start_date': forms.DateInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm', 'type': 'date'}),
            'duration_days': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg px-4 py-2 text-slate-900 dark:text-white focus:outline-none focus:border-blue-500 transition shadow-sm'}),
        }
