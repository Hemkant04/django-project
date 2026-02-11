from django.shortcuts import render
from .models import Employee

# Create your views here.

def index(request):

    students = [
    {
        "name": "Amit Rai",
        "age": 15,
        "grade": 10,
        "roll_no": 1,
        "city": "Pokhara"
    },
    {
        "name": "Sita Sharma",
        "age": 14,
        "grade": 9,
        "roll_no": 2,
        "city": "Kathmandu"
    },
    {
        "name": "Ramesh Thapa",
        "age": 16,
        "grade": 10,
        "roll_no": 3,
        "city": "Butwal"
    }
]
    
    context = {"key": students}


    return render(request , 'web_app/index.html',context)
    
def project(request):
   
    data_context = {
        "page_title": "Project Dashboard",
        "company_name": "TechFlow Systems",
        "generated_at": "2023-10-25 14:30",
       
       
        "tasks": [
            {"id": "T-101", "task": "Server Migration", "owner": "Alice", "priority": "High"},
            {"id": "T-102", "task": "Update CSS", "owner": "Bob", "priority": "Low"},
            {"id": "T-103", "task": "Client Meeting", "owner": "Charlie", "priority": "Medium"},
            {"id": "T-104", "task": "Fix Login Bug", "owner": "Alice", "priority": "High"},
        ]
    }

    return render(request, 'web_app/project.html', data_context)
   
def employee(request):
    data = Employee.objects.all()
    context = {'data':data}

    return render(request, 'web_app/employee.html',context)



from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmployeeForm


def add_employee(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()

    return render(request, "web_app/form.html", {"form": form})



def portfolio(request):
    context = {
        "name": "Hemkant Sah",
        "About_Me":"I am a passionate Data Science student who enjoys working with data, building machine learning models, and extracting meaningful insights. I focus on solving real-world problems using Python and modern data tools.",
        "email": "hemkanta04@gmail.com",
        "linkedin": "https://www.linkedin.com/in/hemkantsah01/",
        "github": "https://github.com/hemkant04",

        "skills" : [
            {"skill": "Python"},
            {"skill": "Machine Learning"},
            {"skill": "Pandas"},
            {"skill": "Numpy"},
            {"skill": "Matplotlib"},
            {"skill": "SQL"},
            {"skill": "Deep Learning"}
        ]
    }
    return render(request, "web_app/portfolio.html", context)
