from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.decorators import login_required   

from .forms import PostApply

from .models import Apply

def home(request):
    return render(request,'home.html')

def next(request):
    return render(request, 'next.html')

@login_required
def check_apply(request):
    applys = Apply.objects.all()
    return render(request, 'admin/check.html', {'applys':applys})

def applier(request, applier_id):
    applier = get_object_or_404(Apply, pk=applier_id)
    return render(request, 'admin/applier.html', {'applier':applier})

def delete_applier(request, applier_id):
    applier = Apply.objects.get(id=applier_id)
    applier.delete()
    return redirect('/apply/foradmin')

def confirm(request):
    if request.method == 'POST':
        form = PostApply(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'success.html')
        else:
            return render(request,'fail.html')
    else:
        form = PostApply()
    return render(request, 'apply.html', {'form': form})