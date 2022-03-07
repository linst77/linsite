from django.contrib.auth import views, login
from django.shortcuts import render, redirect, reverse
from .form import LoginViewForm
from .models import NewCustomUser
from motest.models import MoTestModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseRedirect

def customer_login(request):
    # print (request.POST)
    if request.method == 'POST':
        email_exist = NewCustomUser.objects.filter(email=request.POST.get('email'), phone=request.POST.get('phone')).first()
        print ( email_exist)
        if email_exist:
            # login with email_exist one
            login( request, email_exist)
            # return HttpResponse("email_exist")
            current_page = MoTestModel.objects.filter(email=email_exist.email).first()
            # if phone is not there
            if current_page is None:
                current_page = create_motestmodel( email_exist)
            # phone number update if it is none
            if len( current_page.phone) < 2 or current_page is None:
                current_page.phone = request.POST.get('phone')
                current_page.save()
            return redirect ('motest:motest_detail', pk=current_page.id)

        # user is a new one
        else:
            # return HttpResponse("new")
            # info = form.cleaned_data
            form = LoginViewForm(request.POST)
            if form.is_valid():
                new_user = NewCustomUser.objects.create_user( email = form.cleaned_data['email'],
                                                              phone = form.cleaned_data['phone']
                                                              )
                login(request, new_user)

                # make new page
                new_page = MoTestModel.objects.create(user=new_user,
                                                      email=request.POST.get('email'),
                                                      phone=request.POST.get('phone'),
                                                      )
                new_page.save()
                return redirect('motest:motest_detail', pk=new_page.id)
            else:
                messages.error(request, 'Invalid form submission.')
                return redirect('acct:login')

    else:
        form = LoginViewForm()
        return render(request, 'acct/login.html', {'form': form})

def username_exists(email):
    if NewCustomUser.objects.filter(email=email).exists():
        return True
    return False

def create_motestmodel( user):
    new_page = MoTestModel.objects.create(user=user,
                                      email=user.email,
                                      phone=user.phone,
                                      )
    return new_page

