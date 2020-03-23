from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
# login refer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
# from .models import Cart

from apply_app.models import Apply


# Create your views here.

def login(request):
    return render(request, 'login.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'parm1': 'hello', 'parm2': 'django', 'auth': request.user.is_authenticated}
        print(request.user)
        return render(request, 'index.html', context=context)

@login_required
def profile(request):
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
    return redirect('/apply/foradmin/')

# Not using add, remove 
@login_required
def add(request, id):
    applier = Apply.objects.get(id=id)
    cart = Cart()
    cart.add_item.add(applier.name)
    return redirect('/auth/profile')

@login_required
def remove(request, applier_id):
    applier = get_object_or_404(Apply, id=applier_id)
    cart = Cart()
    cart.add_item.remove(applier)
    return redirect('/auth/profile')
