from django.shortcuts import render,redirect, get_object_or_404
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

def check_apply(request):
    applys = Apply.objects.all()
    # applys_list = Apply.objects.all()
    return render(request, 'check.html', {'applys':applys})

def applier(request, applier_id):
    applier = get_object_or_404(Apply, pk=applier_id)
    return render(request, 'applier.html', {'applier':applier})

def delete_applier(request, applier_id):
    applier = Apply.objects.get(id=applier_id)
    applier.delete()
    return redirect('/foradmin')