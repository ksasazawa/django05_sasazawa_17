from django.shortcuts import render, redirect
from . import forms
from .models import Users, Post, Person
import os
import datetime
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'camos_app/home.html')

def client_login(request):
    login_form = forms.ClientLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active and user.user_type == 'client':
                login(request, user)
                return redirect("camos_app:client_home")
            else:
                messages.warning(request, "ユーザかパスワードが間違っています")
        else:
            messages.warning(request, "ユーザかパスワードが間違っています")
    return render(request, 'camos_app/client_login.html', context={
        'login_form':login_form
    })
    
def client_login2(request):
    login_form = forms.ClientLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active and user.user_type == 'client':
                login(request, user)
                return redirect("camos_app:client_home")
            else:
                messages.warning(request, "ユーザかパスワードが間違っています")
        else:
            messages.warning(request, "ユーザかパスワードが間違っています")
    return render(request, 'camos_app/client_login2.html', context={
        'login_form':login_form
    })

def supplier_login(request):
    login_form = forms.SupplierLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active and user.user_type == 'supplier':
                login(request, user)
                return redirect("camos_app:supplier_home")
            else:
                messages.warning(request, "ユーザかパスワードが間違っています")
        else:
            messages.warning(request, "ユーザかパスワードが間違っています")
    return render(request, 'camos_app/supplier_login.html', context={
        'login_form':login_form
    })
    
def supplier_login2(request):
    login_form = forms.SupplierLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active and user.user_type == 'supplier':
                login(request, user)
                return redirect("camos_app:supplier_home")
            else:
                messages.warning(request, "ユーザかパスワードが間違っています")
        else:
            messages.warning(request, "ユーザかパスワードが間違っています")
    return render(request, 'camos_app/supplier_login2.html', context={
        'login_form':login_form
    })

def client_regist(request):
    add_form = forms.ClientCreationForm()
    if request.method == 'POST':
        add_form = forms.ClientCreationForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("camos_app:client_login")
    return render(request, 'camos_app/client_regist.html', context = {
        'add_form': add_form
    })
    
def client_regist2(request):
    add_form = forms.ClientCreationForm()
    if request.method == 'POST':
        add_form = forms.ClientCreationForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("camos_app:client_login2")
    return render(request, 'camos_app/client_regist2.html', context = {
        'add_form': add_form
    })

def supplier_regist(request):
    if request.method == 'POST':
        add_form = forms.SupplierCreationForm(request.POST, request.FILES)
        if add_form.is_valid():
            add_form.save()
            return redirect("camos_app:supplier_login")
    else:
        add_form = forms.SupplierCreationForm()
    return render(request, 'camos_app/supplier_regist.html', context = {
        'add_form': add_form
    })
    
def supplier_regist2(request):
    if request.method == 'POST':
        add_form = forms.SupplierCreationForm(request.POST, request.FILES)
        if add_form.is_valid():
            add_form.save()
            return redirect("camos_app:supplier_login2")
    else:
        add_form = forms.SupplierCreationForm()
    return render(request, 'camos_app/supplier_regist2.html', context = {
        'add_form': add_form
    })

@login_required
def client_home(request):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(create_user=request.user).count()
    if Post.objects.filter(create_user=request.user, data_added__startswith=dt.date()):
        new_post_cnt = Post.objects.filter(create_user=request.user, data_added__startswith=dt.date()).count()
    else:
        new_post_cnt = 0
    return render(request, 'camos_app/client_home.html', context={
        'post_cnt': post_cnt,
        'new_post_cnt': new_post_cnt,
        'person_cnt': person_cnt,
    })

@login_required
def supplier_home(request):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    post_all_cnt = Post.objects.filter(agent__contains=request.user.company_name).count()
    person_cnt = Person.objects.filter(create_user=request.user).count()
    return render(request, 'camos_app/supplier_home.html', context={
        'post_cnt': post_cnt,
        'post_all_cnt': post_all_cnt,
        'person_cnt': person_cnt,
    })

@login_required
def client_job_list(request):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    posts = Post.objects.all()
    return render(request, "camos_app/client_job_list.html", context = {
        "posts": posts,
        "person_cnt": person_cnt,
    })

@login_required
def client_job_detail(request, id):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    post = Post.objects.get(id=id)
    return render(request, "camos_app/client_job_detail.html", context = {
        "post": post,
        "person_cnt": person_cnt,
    })
    
@login_required
def client_job_edit(request, id):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    post = Post.objects.get(id=id)
    form = forms.PostForm(initial={
        'title': post.title,
        'job': post.job,
        'qualification': post.qualification,
        'location': post.location,
        'body': post.body,
        'price': post.agent,
        'create_user': post.create_user,
        'create_user_company': post.create_user_company,  
    })
    return render(request, "camos_app/client_job_edit.html", context = {
        "post": post,
        "person_cnt": person_cnt,
        "form": form,
    })

@login_required
def client_job_create(request):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            job = form.cleaned_data['job']
            qualification = form.cleaned_data['qualification']
            location = form.cleaned_data['location']
            body = form.cleaned_data['body']
            price = form.cleaned_data['price']
            agent = form.cleaned_data['agent']
            create_user = request.user
            create_user_company = form.cleaned_data['create_user_company']
            form = Post.objects.create(title=title, job=job, qualification=qualification, location=location, body=body, price=price, agent=agent, create_user=create_user, create_user_company=create_user_company)
            return redirect("camos_app:client_home")
    else:
        form = forms.PostForm()      
    return render(request, "camos_app/client_job_create.html", context = {
        "form": form,
        "person_cnt": person_cnt
    })

@login_required
def supplier_job_list(request):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    posts = Post.objects.filter(agent__contains=request.user.company_name)
    return render(request, 'camos_app/supplier_job_list.html', context = {
        'posts': posts,
        'post_cnt': post_cnt,
    })
    
@login_required
def supplier_job_map(request):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    posts = Post.objects.filter(agent__contains=request.user.company_name)
    return render(request, 'camos_app/supplier_job_map.html', context = {
        'posts': posts,
        'post_cnt': post_cnt,
    })
    
@login_required
def supplier_job_detail(request, id):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    post = Post.objects.get(id=id)
    return render(request, "camos_app/supplier_job_detail.html", context = {
        "post": post,
        "post_cnt": post_cnt
    })

@login_required
def supplier_person_create(request, id):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            qualification = form.cleaned_data['qualification']
            construction1 = form.cleaned_data['construction1']
            construction2 = form.cleaned_data['construction2']
            construction3 = form.cleaned_data['construction3']
            create_user = request.user
            create_user_company = request.user.company_name
            # create_user_company = form.cleaned_data['create_user_company']
            form = Person.objects.create(name=name, age=age, sex=sex, qualification=qualification, construction1=construction1, construction2=construction2, construction3=construction3, create_user=create_user, create_user_company=create_user_company, job=post)
            return redirect("camos_app:supplier_home")
    else:
        form = forms.PersonForm()
    return render(request, "camos_app/supplier_person_create.html", context={
        "form": form,
        "id": id,
        "post_cnt": post_cnt,
    })

@login_required
def client_worker_list(request):
    people_all = Person.objects.all()
    people = []
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            people.append(person)
            person_cnt += 1
    return render(request, 'camos_app/client_worker_list.html', context={
        'people': people,
        'person_cnt': person_cnt,
    })
    
@login_required
def client_worker_detail(request, id):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    person = Person.objects.get(id=id)
    if request.method == "POST":
        form = forms.ResultForm(request.POST)
        if form.is_valid():
            person.result = form.cleaned_data['result']
            person.save()
            return redirect('camos_app:client_home')
    else:
        form = forms.ResultForm() 
    return render(request, "camos_app/client_worker_detail.html", context = {
        "form": form,
        "person": person,
        "person_cnt": person_cnt,
    })
    
    
    person = Person.objects.get(id=id)
    return render(request, "camos_app/client_worker_detail.html", {"person": person})

@login_required
def supplier_worker_list(request):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    people = Person.objects.filter(create_user=request.user)
    return render(request, 'camos_app/supplier_worker_list.html', context={
        'people': people,
        'post_cnt': post_cnt,
    })

@login_required
def client_settings(request):
    people_all = Person.objects.all()
    person_cnt = 0
    for person in people_all:
        if person.job.create_user == request.user:
            person_cnt += 1
    if request.method == "POST":
        form = forms.ClientChangeForm(request.POST)
        if form.is_valid():
            user = Users.objects.get(id=request.user.id)
            user.username = form.cleaned_data["username"]
            user.company_name = form.cleaned_data["company_name"]
            user.site_name = form.cleaned_data["site_name"]
            user.save()
            return redirect('camos_app:client_home')
    else:
        form = forms.ClientChangeForm(initial={
            'username': request.user.username,
            # 'email': request.user.email,
            'company_name': request.user.company_name,
            'site_name': request.user.site_name,
        })
    return render(request, 'camos_app/client_settings.html', context = {
        'form': form,
        "person_cnt": person_cnt,
    })
    
@login_required
def supplier_settings(request):
    dt = datetime.datetime.today()
    post_cnt = Post.objects.filter(agent__contains=request.user.company_name, data_added__startswith=dt.date()).count()
    if request.method == "POST":
        form = forms.SupplierChangeForm(request.POST)
        if form.is_valid():
            user = Users.objects.get(id=request.user.id)
            user.username = form.cleaned_data["username"]
            user.company_name = form.cleaned_data["company_name"]
            user.capital = form.cleaned_data["capital"]
            user.website = form.cleaned_data["website"]
            user.save()
            return redirect('camos_app:supplier_home')
    else:
        form = forms.SupplierChangeForm(initial={
            'username': request.user.username,
            'company_name': request.user.company_name,
            'capital': request.user.capital,
            'website': request.user.website,
        })    
    return render(request, 'camos_app/supplier_settings.html', context={
        "post_cnt": post_cnt,
        "form": form,
    })

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'ログアウトしました')
    return redirect('camos_app:home')

