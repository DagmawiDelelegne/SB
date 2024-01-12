from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm,LoginForm,BookSearchForm,BookForm
from .models import Profile,Book
def home(request):
    
    return render(request, 'shareab/index.html')

#Register

def register(request):
   
    form = CreateUserForm()

    if request.method == "POST":
          form = CreateUserForm(request.POST,request.FILES)

          if form.is_valid():
               user=form.save()
               Profile.objects.create(user=user, bio=form.cleaned_data['bio'],profile_image=form.cleaned_data['profile_image'], campus=form.cleaned_data['campus'])
               return redirect('login')
          
    else:
         form = CreateUserForm()            
    context = {"form": form}
    return  render(request, 'shareab/register.html', context)


#login user
def my_login(request):
     
    form = LoginForm()

    if request.method == 'POST':
          
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
               
               username = request.POST.get('username')
               password = request.POST.get('password')

               user = authenticate(request, username=username, password=password)
               if user is not None:
                    auth.login(request,user)
                    return redirect("dashboard")
    context = {'form':form}

    return render (request,'shareab/login.html',context=context)

@login_required(login_url='login')
def dashboard(request):
    results = None

    if request.method == 'GET':
        form = BookSearchForm(request.GET)

        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Book.objects.filter(title__icontains=search_query)

    else:
        form = BookSearchForm()
    return render(request, 'shareab/dashboard.html', {'form': form, 'results': results})
     
"""
@login_required(login_url='login')
def book_search(request):
     results = None
     if request.method == 'GET':
          
          form = BookSearchForm(request.GET)

          if form.is_valid():
               search_query = form.cleaned_data['search_query']
               results = Book.objects.filter(title__icontains=search_query)
               return render(request, 'search_results.html', {'results': results, 'form': form})
          
     else:
        form = BookSearchForm()
"""
     

@login_required(login_url='login')
def add_Book(request):
     if request.method == 'POST':
          form = BookForm(request.POST)
          if form.is_valid():
               title = form.cleaned_data['title']
               author = form.cleaned_data['author']
               course = form.cleaned_data['course']
               user = request.user
               Book.objects.create(title=title, author=author, course=course, user=user)
               return redirect('dashboard')
     else:
          form = BookForm()

     return render(request, 'shareab/add_book.html', {'form': form})

                
    #logout user
def my_logout(request):
     
     auth.logout(request)

     return redirect("login")
          
