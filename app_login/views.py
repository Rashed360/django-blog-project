from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from app_login.forms import SignUpForm, ProfileUpdateForm, UserProfileForm
from django.contrib.auth import login as user_login, authenticate, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    form = SignUpForm()
    registerd = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registerd = True
    context={'form':form,'registerd':registerd}
    return render(request, 'app_login/signup.html', context)

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                user_login(request, user)
                return HttpResponseRedirect(reverse('app_blog:blogs'))
    context={'form':form}
    return render(request, 'app_login/login.html', context)

@login_required
def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    context={}
    return render(request, 'app_login/profile.html', context)

@login_required
def profile_update(request):
    current_user = request.user
    form = ProfileUpdateForm(instance=current_user)
    if request.method == 'POST':
        form = ProfileUpdateForm(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
            # form = ProfileUpdateForm(instance=current_user)
    context={'form':form,}
    return render(request, 'app_login/profile_update.html', context)

@login_required
def profile_extra(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    context={'form':form, 'action':'Add'}
    return render(request, 'app_login/profile_extra.html', context)

@login_required
def profile_extra_update(request):
    form = UserProfileForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    context={'form':form, 'action':'Update'}
    return render(request, 'app_login/profile_extra.html', context)

@login_required
def password_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    context={'form':form,'changed':changed}
    return render(request, 'app_login/password_change.html', context)