from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})


def repositary(request):
       
    if request.method == 'POST':
       username = request.POST.get("screen_name",'')
       response = requests.get('https://api.github.com/users/'+username+'/repos')
     
       user = response.json()
       
         
       return render(request, 'blog/repositary.html', {'reposi':user,'user':username})
           
      



