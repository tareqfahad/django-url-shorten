from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from .models import Target
# Create your views here.
from random import choices
import string
def index(request):
    return render(request , 'createurl/index.html',{})

def create(request):
    try:
        hash = ''.join(choices(string.ascii_uppercase + string.digits, k=5))
        t = Target(hash_code = hash , target = request.POST['target'])
        t.save() 
        new_destination =  request.get_host() + "/" + hash 
    except (KeyError):
        return HttpResponse('error')
    
    return render(request , 'createurl/index.html' , {'url':new_destination})