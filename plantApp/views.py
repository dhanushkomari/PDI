from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import upload_form
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'plantApp/home.html')

    '''if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']

        user = authenticate(username = uname, password = pwd)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                print('logged in')
                return render(request, 'plantApp/home.html')
        else:
            messages.warning(request,'***Invalid Credentials')
            return render(request, 'plantApp/login.html')

        
    else:
        return render(request, 'plantApp/login.html')'''


def upload(request):
    if request.method == "POST":
        print(request.FILES['picture'])
        print('post method')
        return redirect('plantApp:home')
    else:
        form = upload_form()
    return render(request, 'plantApp/upload_image.html', {'form':form})



def result(request):
    return render(request, 'plantApp/result.html')


def contact(request):
    if request.method == "POST":
        print('form submitted')
        return redirect('plantApp:home')
    else:
        return render(request, 'plantApp/contact.html')


#########################################################

class Home(TemplateView):
    template_name = 'plantApp/home.html'


