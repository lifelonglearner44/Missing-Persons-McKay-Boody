from django.urls import path
from .views import indexPageView
from .views import faqPageView
from .views import showPeoplePageView
from .views import displayPersonPageView

urlpatterns = [
    path("<int:id>/", displayPersonPageView, name= "displayPerson"),
    path("showPeople/", showPeoplePageView, name ="showPeople"),
    path("", indexPageView, name = "index"),
    path("faq/", faqPageView, name = "faq"),
]
