from django.shortcuts import render
#from django.http import HttpResponse
#from .models import CandidateName
#from .models import ProfileContent
#from .models import CollegeName
#from .models import Experience
#from .models import projects
#from .models import Certifications
#from .models import Socialmedia,contacts
#from django.template.context_processors import csrf
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        cname=request.POST["country"]
        sname=request.POST["subject"]
        email=request.POST["email"]
        message = request.POST["message"] + " from " + email
        #sendemail operations
        send_mail(sname, message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently = False)
        
    return render(request,"form.html")

