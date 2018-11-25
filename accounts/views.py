from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#-------------below are codes --------------------------------------------------------------------------

#TODO: implement user authentication system


def signup(request):
    if request.method == 'POST':# if the server request is POST not GET

        if request.POST['password1'] == request.POST['password2']:
            #if password matches
            try:
                #look in server and see whether the user name already been taken
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already exist, please think of a new one.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    #check type of server request
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None: #if we do find a user according to the user input
            auth.login(request, user)
            return redirect('loggedin')
        else:
            return render(request, 'accounts/login.html',{'error':'Incorrect name or password, please re-enter.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        #log out and return to start page
        #TODO: add a "you have successfully log out" notice?

        return redirect('home')

def loggedin(request):
    return render(request, 'accounts/loggedin.html')


#test: file uploading



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
