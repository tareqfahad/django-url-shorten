from django.shortcuts import render , redirect


# Create your views here.
from createurl.models import Target

def redirect(request , target):
    try:
        t = Target.objects.get(hash_code=target)
        return render(request , 'redirect/index.html' , {'url' : t.target})

    except (KeyError):
        return render(request , 'redirect/index.html' , {'error' : 'Not found'})
