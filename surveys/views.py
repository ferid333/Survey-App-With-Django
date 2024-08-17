from itertools import count
from math import ceil
from django.shortcuts import render,redirect
from .models import Survey
from django.http import HttpResponse
# Create your views here.


def create_survey(request):
    if not request.user.is_authenticated :
        return redirect("login")
    else:    
        return render(request,"surveys/createsurvey.html")


def new_survey(request):
    if request.method=="POST":
       question=request.POST["question"]
       option1=request.POST["option1"]
       option2=request.POST["option2"]
       option3=request.POST["option3"]
       option4=request.POST["option4"]
       option5=request.POST["option5"]
       username=request.user.get_username()
       new_survey=Survey.objects.create(question=question,option1=option1,option2=option2,user=username,option3=option3,option4=option4,option5=option5)
       new_survey.save()
       return redirect("home")
    return render(request,"surveys/createsurvey.html")        

def show_all_surveys(request,page):
    allsurveys_count=Survey.objects.all().count()
    items_per_page=4
    pages=[p for p in range(1,ceil(allsurveys_count/items_per_page)+1)]
    last_item=items_per_page*page
    first_item=last_item-items_per_page
    str_slice=f"{first_item}:{last_item}"
    context={
      "surveys":Survey.objects.all(),
      "pages":pages,
      "active_page":page,
      "str_slice":str_slice,
      "entered_survey":request.session["visits"]
    }
    return render(request,"surveys/allsurveys.html",context)


def vote_survey(request,survey):
    if not survey in request.session["visits"]:
        current_survey=Survey.objects.get(slug=survey)
        context={
            "survey":current_survey,
            "options":[current_survey.option1,current_survey.option2,current_survey.option3,current_survey.option4,current_survey.option5]
        }
        return render(request,"surveys/vote.html",context)    
    else:
        return redirect("showresult",survey)

def vote_result(request,survey):
    if not 'visits' in request.session or not request.session['visits']:
     request.session['visits'] = [survey]
    else:
     saved_list = request.session['visits']
     saved_list.append(survey)
     request.session['visits'] = saved_list
    if request.method=="POST":
     p=request.POST["radioinputs"]
     current_survey=Survey.objects.get(slug=survey)
     if p==current_survey.option1:
        current_survey.option1_count+=1
        current_survey.save()
     if p==current_survey.option2:
       current_survey.option2_count+=1
       current_survey.save() 
     if p==current_survey.option3:
      current_survey.option3_count+=1
      current_survey.save()
     if p==current_survey.option4:
       current_survey.option4_count+=1
       current_survey.save()
     if p==current_survey.option5:
        current_survey.option5_count+=1
        current_survey.save()        
    return redirect("showresult",survey)
def show_result(request,survey):
    current_survey=Survey.objects.get(slug=survey)
    context={
         "survey":current_survey,
         "options":{
            current_survey.option1:current_survey.option1_count/current_survey.allcounts*100,
            current_survey.option2:current_survey.option2_count/current_survey.allcounts*100,
            current_survey.option3:current_survey.option3_count/current_survey.allcounts*100,
            current_survey.option4:current_survey.option4_count/current_survey.allcounts*100,
            current_survey.option5:current_survey.option5_count/current_survey.allcounts*100
         }
    }
    return render(request,"surveys/surveyresult.html",context)