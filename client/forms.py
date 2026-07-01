from django import forms
from .models import JobRequirement

class JobRequirementForm(forms.ModelForm):
    class Meta:
        model = JobRequirement
        fields = [
            'title', 
            'workers_needed', 
            'daily_wage', 
            'location', 
            'provides_housing', 
            'provides_meals', 
            'provides_medical'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-slate-900 focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'workers_needed': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-slate-900 focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'daily_wage': forms.NumberInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-slate-900 focus:outline-none focus:border-blue-500 transition shadow-sm'}),
            'location': forms.TextInput(attrs={'class': 'w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-slate-900 focus:outline-none focus:border-blue-500 transition shadow-sm'}),
        }
