from django.shortcuts import render,redirect
from .forms import BookCreateForm,RegForm
from django.views.generic import DeleteView,TemplateView,CreateView,ListView,UpdateView,DetailView
from .models import BookModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class DBookCreateView(CreateView):
    model = BookModel
    form_class = BookCreateForm
    template_name = "createbook.html"
    success_url = reverse_lazy("List")

class DBookListView(ListView):
    model = BookModel
    template_name = "listbook.html"
    context_object_name = "books"

class DUpdate(UpdateView):

    template_name = "updatebook.html"
    form_class = BookCreateForm
    model = BookModel
    success_url = reverse_lazy("dlist")

class DDetailView(DetailView):
    model = BookModel
    template_name = "detailbook.html"
    context_object_name = "book"

class DDelete(DeleteView):
    model = BookModel
    template_name = "deletebook.html"
    success_url = reverse_lazy("List")

class UserRegistration(CreateView):
    model = User
    form_class = RegForm
    template_name = "userreg.html"
    success_url = reverse_lazy("login")

class LoginView(TemplateView):
    model = User
    template_name = "Login.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('usrname')
        password=request.POST.get('pasword')
        user=authenticate(request,username=username,password=password)
        if user:
            print("success")
            login(request,user)
            return redirect("List")
        else:
            print("failed")
            return render(request, self.template_name)















class BookCreateView(TemplateView):
    model = BookModel
    form_class = BookCreateForm
    template_name = "createbook.html"
    context={}
#     for get function
    def get(self,request,*args,**kwargs):
        form = self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            print("saved")
            form.save()
            return redirect("List")


class GetObjectMixin:
    def get_object(self,id):
        return self.model.objects.get(id=id)

# List all books
class ListView(TemplateView,GetObjectMixin):
    model = BookModel
    template_name = "listbook.html"
    context={}
    def get(self,request,*args,**kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)


# book create


# detail view
class DetailView(TemplateView,GetObjectMixin):
    model = BookModel
    template_name = "detailbook.html"
    context={}
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        self.context["book"]=book
        return render(request,self.template_name,self.context)

# update book

class BookUpdateView(TemplateView,GetObjectMixin):
    model = BookModel
    form_class = BookCreateForm
    template_name = "updatebook.html"
    context={}

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=self.get_object(id)
        form= self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        form=self.form_class(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("List")


# delete

class DeleteBook(TemplateView,GetObjectMixin):
    model = BookModel
    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("id"))
        book.delete()
        return redirect("List")