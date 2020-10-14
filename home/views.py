from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import json
from home.models import *

# from pathlib import Path
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


def homeView(request):
    my_content = {
        'social_platforms':  ['Twitter', 'Facebook', 'Google', 'Instagram', 'Netflex', 'Amazon'], 
    }
    return render(request, 'home.html', my_content)

def uploadView(request):
    if request.method == 'POST':
        file_upload = request.FILES['doc']
        file_storage = FileSystemStorage()
        file_storage.save(file_upload.name, file_upload)
    return render(request, 'upload.html')


# with open(os.path.join(BASE_DIR, 'home/media/your_topics.json'), "r") as read_file:
#     data = json.load(read_file)    
#     print(data.keys())

def visualizationView(request):
    if request == 'GET':
        hek = request.is_secure()
        cont = link()
        cont.save(hek.name, hek)

    return render(request, 'data.html', cont)

# def aboutView(request):
#     return render(request, 'home/about.html')

# def contact(request):
#     return render(request, 'home/contact.html')