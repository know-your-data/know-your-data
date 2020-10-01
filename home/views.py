from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def homeView(request):
    my_content = {
        'social_platforms':  ['Twitter', 'Facebook', 'Google', 'Instagram', 'Netflex', 'Amazon'], 
    }
    return render(request, 'home.html', my_content)






# def homeView(request):
#     return render(request, 'home/about.html')

# def homeView(request):
#     return render(request, 'home/contact.html')