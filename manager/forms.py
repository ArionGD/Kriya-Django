from django import forms
from accounts.models import User
from worker.models import WorkerProfile

class WorkerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    # Worker Profile fields
    skills = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'e.g., Carpentry, Masonry'}))
    experience_years = forms.IntegerField(initial=0)
    location = forms.CharField(required=False, max_length=200)
    daily_wage_expected = forms.DecimalField(required=False, max_digits=10, decimal_places=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = User.Role.WORKER
        if commit:
            user.save()
            WorkerProfile.objects.create(
                user=user,
                skills=self.cleaned_data.get('skills', ''),
                experience_years=self.cleaned_data.get('experience_years', 0),
                location=self.cleaned_data.get('location', ''),
                daily_wage_expected=self.cleaned_data.get('daily_wage_expected', None)
            )
        return user
