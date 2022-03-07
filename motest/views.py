from django.shortcuts import render
from django.views.generic import UpdateView
from .models import MoTestModel, FileModels
from acct.models import NewCustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import *

# Create your views here.

#slug search
@login_required
def motest_datail_view( request, slug=None, pk=None):

    if slug is not None:
        user_model = NewCustomUser.objects.get(slug=slug)
        instance = MoTestModel.objects.filter(user=user_model).first()
    else:
        instance = MoTestModel.objects.get(id=pk)

    form_1 = UploadFileForm(None)
    form_2 = FirstUpload(None)
    form_3 = SecondUpload(None)

    context = {'form_1': form_1,
               'form_2': form_2,
               'form_3': form_3,
               }

    if request.method == 'POST':

        form_1 = UploadFileForm(request.POST)
        form_2 = FirstUpload(request.POST)
        form_3 = SecondUpload(request.POST)
        context = {'form_1': form_1,
                   'form_2': form_2,
                   'form_3': form_3,
                   }
        author = request.user.id
        if request.POST['form_type'] == 'info-form':
            if form_1.is_valid():
                # print (form_1)
                post = form_1.save(commit=False)
                post.user_id = author
                post.save()
                return render(request, 'motest/motest_detail.html', {'context': context})

        elif request.POST['form_type'] == 'first-form':
            if form_2.is_valid():
                files = request.FILES.getlist('files')
                # print(request.POST, request.FILES)
                instance.content_first = form_2.cleaned_data['content_first']
                instance.save()

                instance.photo_first.add( image_model( instance.photo_first, author, files))
                return render(request, 'motest/motest_detail.html', {'context': context})

        elif request.POST['form_type'] == 'second-form':
            if form_3.is_valid():
                files = request.FILES.getlist('files')
                instance.content_sec = form_3.cleaned_data['content_sec']
                instance.save()
                instance.photo_sec.add( image_model( instance.photo_sec, author, files))
                return render(request, 'motest/motest_detail.html', {'context': context})

        elif request.POST['form_type'] == 'form_final':
            return render( request, 'motest/motest_detail.html', {'context': context})

        else:
            form_01 = UploadFileForm()
            return render(request, 'motest/motest_detail.html', {'context': context})
    else:
        form_1 = UploadFileForm( instance=instance)
        context['form_1'] = form_1
        return render(request, 'motest/motest_detail.html', {'context': context})

def image_model(instance, author, files):

    for i in files:
        file = FileModels()
        file.user_id = author
        file.files = i
        file.save()
        instance.add(file)
