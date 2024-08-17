from django import views
from django.urls import path
from . import views


urlpatterns = [
    path("createsurvey/",views.create_survey,name="createsurvey"),
    path("createsurvey/newsurvey",views.new_survey,name="newsurvey"),
    path("allsurveys/<int:page>",views.show_all_surveys,name="allsurveys"),
    path("survey/<slug:survey>",views.vote_survey,name="votesurvey"),
    path("survey/<slug:survey>/vote",views.vote_result,name="voteresult"),
    path("survey/<slug:survey>/result/",views.show_result,name="showresult")
]
