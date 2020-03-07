from django.shortcuts import render
from .models import Apply
# Create your views here.
def home(request):
    return render(request,'home.html')
def apply(request):
    return render(request,'apply.html')


def confirm(request):
    human = Apply()
    human.name = str(request.GET['name'])
    human.gender = str(request.GET['gender'])
    human.phone = str(request.GET['phone'])
    human.year = str(request.GET['year'])
    human.major = str(request.GET['major'])
    human.url = str(request.GET['url'])
    human.why = str(request.GET['why'])
    human.service = str(request.GET['service'])
    human.memory = str(request.GET['memory'])
    human.coding = str(request.GET['coding'])
    human.save()
    return render(request,'success.html')