from django.shortcuts import render, get_object_or_404, redirect
from mainapp.models import jrsUser, job, companies
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginP(request):
    if request.user.is_authenticated:
        jrsuser = jrsUser.users.get(username=request.user.username)
        return render(request, 'main.html', {'logged':jrsuser})
    else:
        return render(request, 'index.html')
        
def mainpage(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'main.html', {'logged':jrsuser})

def searchResult(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    freesrc = request.POST.get('freesrc')
    locsrc = request.POST.get('locationsrc')
    if(freesrc != ''):
        jobs1 = job.objects.filter(title__contains = freesrc)
        jobs2 = job.objects.filter(company__contains = freesrc)
        jobs3 = job.objects.filter(jobType__contains = freesrc)       
        jobs4 = job.objects.filter(location__contains = freesrc)
        jobs = jobs1 | jobs2 | jobs3 | jobs4
        jobs = jobs.order_by('-id')
        i = 0
        while i+1 < len(jobs):
            if(jobs[i].id == jobs[i+1].id):
                jobs.remove(jobs[i+1].id)
            else:
                i += 1 
    elif (locsrc != ''):
        jobs = job.objects.filter(location__contains = locsrc)
    else:
        jobs = job.objects.all()
    jobs = jobs.order_by('-rank')
    listsize = len(jobs)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'jobs_list.html', {'logged':jrsuser, 'jobs':jobs, 'size':listsize})
    
def jobsList(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobs = job.objects.order_by('-rank')
    listsize = len(jobs)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'jobs_list.html', {'logged':jrsuser, 'jobs':jobs, 'size':listsize})

def jobDetails(request, jobid):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobtosee = get_object_or_404(job, id=jobid)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'job_details.html', {'logged':jrsuser, 'jobdetails' : jobtosee})

def applicationForm(request, jobid):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobdetails = get_object_or_404(job, id = jobid)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'job_application.html', {'logged':jrsuser, 'jobdetails':jobdetails})

def register(request):
    return render(request, 'register.html')

def addUser(request):
    _username = request.POST.get('userName')
    for i in jrsUser.users.all():
        if(i.username == _username):
            return render(request, 'register.html', {'FORM_ERROR': "Username exists"})
    _email = request.POST.get('emailAddress')
    _password = request.POST.get('password')
    _password2 = request.POST.get('rePassword')
    if(_password != _password2):
        return render(request, 'register.html', {'FORM_ERROR': "Password doesn't match"})
    _location = request.POST.get('location')
    newuser = jrsUser(username = _username, email = _email, location = _location)
    newuser.save()
    backuser = User.objects.create_user(_username)
    backuser.set_password(_password)
    backuser.save()
    return render(request, 'index.html')

def myJobs(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobs = job.objects.all().filter(postedby=request.user.username)
    listsize = len(jobs)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'myjobs.html', {'logged':jrsuser, 'jobs':jobs, 'size':listsize})

def addJobForm(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jrsuser = jrsUser.users.get(username=request.user.username)
    comp = companies.objects.get(name = jrsuser.company)
    return render(request, 'addjob.html', {'logged':jrsuser, 'comp':comp})

def addJob(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    _postedby = request.user.username
    _comapny = jrsUser.users.get(username = request.user.username).company
    _title = request.POST.get('jobTitle')    
    _jobType = request.POST.get('jobType')
    _salary = request.POST.get('salaryOption')
    _description = request.POST.get('jobDescription')
    _mustmeet1 = request.POST.get('mustMeet1')
    _mustmeet2 = request.POST.get('mustMeet2')
    _mustmeet3 = request.POST.get('mustMeet3')
    _mustmeet4 = request.POST.get('mustMeet4')
    _mustmeet5 = request.POST.get('mustMeet5')
    _mustmeet6 = request.POST.get('mustMeet6')
    comp = get_object_or_404(companies, name=_comapny)
    _logo = comp.logo
    _rank = comp.rank
    _location = comp.location
    newjob = job(postedby = _postedby, company = _comapny, logo = _logo, rank = _rank, location = _location, title = _title, jobType = _jobType, salary = _salary, jobDescription = _description, mustmeet1 = _mustmeet1, mustmeet2 = _mustmeet2, mustmeet3 = _mustmeet3, mustmeet4 = _mustmeet4, mustmeet5 = _mustmeet5, mustmeet6 = _mustmeet6)
    newjob.save()
    return myJobs(request)

def loginCheck(request):
    _username = request.POST.get('username')
    _password = request.POST.get('password')
    user = authenticate(request, username = _username, password = _password)
    if user is not None:
        login(request, user)
        jrsuser = jrsUser.users.get(username=request.user.username)
        return render(request, 'main.html', {'logged':jrsuser})
    else:
        return render(request, 'index.html', {'LOGIN_ERROR': "Wrong username / password"})

def logoutUser(request):
    logout(request)
    return render(request, 'index.html', {'LOGIN_ERROR': "Logged out successfuly"})

def delJob(request, jobid):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobtodel = get_object_or_404(job, id=jobid)
    jobtodel.delete()
    return redirect('/myjobs')

def redirector(request, whereto):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/' + whereto)

def applyRedirector(request, whereto):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/job_details/' + whereto)

def editjob(request, jobid):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobdetails = get_object_or_404(job, id=jobid)
    jrsuser = jrsUser.users.get(username=request.user.username)
    return render(request, 'altarjob.html', {'logged':jrsuser, 'jobdetails':jobdetails})

def backtoMyJobs(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/myjobs')

def confirmedit(request, jobid):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    jobtoedit = get_object_or_404(job, id=jobid)
    jobtoedit.title = request.POST.get('jobTitle')    
    jobtoedit.jobType = request.POST.get('jobType')
    jobtoedit.salary = request.POST.get('salaryOption')
    jobtoedit.description = request.POST.get('jobDescription')
    jobtoedit.mustmeet1 = request.POST.get('mustMeet1')
    jobtoedit.mustmeet2 = request.POST.get('mustMeet2')
    jobtoedit.mustmeet3 = request.POST.get('mustMeet3')
    jobtoedit.mustmeet4 = request.POST.get('mustMeet4')
    jobtoedit.mustmeet5 = request.POST.get('mustMeet5')
    jobtoedit.mustmeet6 = request.POST.get('mustMeet6')
    jobtoedit.save()
    return redirect('/myjobs')

def reMain(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/main')