from django.shortcuts import render
from .forms import FileUploadForm
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import FileResponse
from django.urls import reverse
from azure.storage.blob import BlobServiceClient
from django.conf import settings
from django.shortcuts import get_object_or_404
# Create your views here.

#For the File upload

def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Success") 
            return render(request, 'SuccessUpload.html',{'file':form} )# Redirect to a success page
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})


#For the File Download and  View


#For the Login 
