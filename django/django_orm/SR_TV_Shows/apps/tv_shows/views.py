from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime


def index(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "main/index.html", context)

def add_show(request):
	return render(request, "main/add_show.html")

def add(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'], release_date=request.POST['date'])
        num = Show.objects.get(title=request.POST['title']).id
        return redirect(f'/shows/{num}')

def edit_show(request, num):
    new_date = Show.objects.get(id=num).release_date.strftime('%m/%d/%y')
    context = {
        'show' : Show.objects.get(id=num),
        'cdate' : new_date
    }
    return render(request, "main/edit_show.html", context)

def show_info(request, num):
    new_date = Show.objects.get(id=num).release_date.strftime('%B %d, %Y %I:%M %p')
    context = {
        'show' : Show.objects.get(id=num),
        'cdate' : new_date
    }
    return render(request, "main/show_info.html", context)

def update(request, num):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{num}/edit')
    elif request.POST['date'] == "" or request.POST['date'] == '':
        Show.objects.filter(id=num).update(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'])
        return redirect("/shows")
    else:
        Show.objects.filter(id=num).update(title=request.POST['title'], network=request.POST['network'], desc=request.POST['desc'], release_date=request.POST['date'])
        return redirect(f"/shows/{num}")
        
def purchase(request):
    if 'total_purchased' not in request.session:
        request.session['total_purchased'] = int(request.form['amount'])
    else:
        request.session['total_purchased'] += int(request.form['amount'])
    context = {
        "total" : Show.objects.get(id=int(request.form['hidden']).price) * int(request.FORM['amount'])
    }
    
    return redirect("/thank_you")
    
def thanks(request):
    return render

def delete_show(request, num):
    Show.objects.get(id=num).delete()
    return redirect("/shows")
