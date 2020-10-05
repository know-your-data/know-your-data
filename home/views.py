from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


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


def visualizationView(request):
    return render(request, 'data.html')

# def aboutView(request):
#     return render(request, 'home/about.html')

# def contact(request):
#     return render(request, 'home/contact.html')