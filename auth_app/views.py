from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
# login refer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from .models import Cart

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
        # applys_sub = Cart.objects.filter(user=request.user)[0]
        applys_sub = Cart.objects.get(id=3)
        print('applys: ', applys_sub)

    return render(request, 'profile.html', context={'data': data})


@login_required
def add(request, id):
    # applier = get_object_or_404(Apply, id=id)
    applier = Apply.objects.get(id=id)
    # cart = Cart.objects.get(user=request.user)
    # print(applier.name)
    cart = Cart()
    cart.add_item.add(applier.name)
    # print('type : ', applier)
    return redirect('/auth/profile')
    # return render('/admin')

@login_required
def remove(request, applier_id):
    applier = get_object_or_404(Apply, id=applier_id)
    cart = Cart()
    cart.add_item.remove(applier)
    return redirect('/auth/profile')
