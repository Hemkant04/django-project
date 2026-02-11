from django import forms
from .models import Employee
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "role", "department", "status"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control py-4 px-4 border rounded-lg mt-2",
                "placeholder": "Enter employee name"
            }),
            "role": forms.TextInput(attrs={
                "class": "form-control py-4 px-4 border rounded-lg mt-2",
                "placeholder": "Enter role"
            }),
            "department": forms.TextInput(attrs={
                "class": "form-control py-4 px-4 border rounded-lg",
                "placeholder": "Enter department"
            }),
            "status": forms.Select(attrs={
                "class": "form-control py-4 px-4 border rounded-lg"
            }),
        }



form = EmployeeForm()
