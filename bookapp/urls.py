from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView,UserRegistration,DDelete,DDetailView,DUpdate,DBookListView,DBookCreateView,BookCreateView,ListView,BookUpdateView,DetailView,DeleteBook
urlpatterns =[
    path("home",TemplateView.as_view(template_name="createbook.html"),name="createbook"),
    path("createbook",BookCreateView.as_view(),name="createbook"),
    path("BookList",ListView.as_view(),name="List"),
    path("Books/<int:id>",BookUpdateView.as_view(),name="update"),
    path("Books/detail/<int:id>",DetailView.as_view(),name="detail"),
    path("Books/delete/<int:id>",DeleteBook.as_view(),name="delete"),
    path("dbooks",DBookCreateView.as_view(),name="dcreate"),
    path("dbooks/list",DBookListView.as_view(),name="dlist"),
    path("dbooks/update/<int:id>",DUpdate.as_view(),name="dupdate"),
    path("dbooks/detail/<int:pk>",DDetailView.as_view(),name="ddetail"),
    path("dbooks/remove/<int:pk>",DDelete.as_view(),name="ddelete"),
    path("login",LoginView.as_view(),name="login"),
    path("Register",UserRegistration.as_view(),name="register"),
]

