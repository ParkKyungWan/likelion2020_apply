from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .forms import PostApply

from .models import Apply

def home(request):
    return render(request,'home.html')

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

def confirm(request):
    if request.method == 'POST':
        form = PostApply(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'success.html')
    else:
        form = PostApply()
    return render(request, 'apply.html', {'form': form})