from django.shortcuts import render
from bookapp.models import BookModel
# Create your views here.
from .serializers import BookSerializer,BookClassSerializer,LoginSerializer
from django.http import JsonResponse,Http404
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# function based
# get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,authentication,permissions
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
# authentication , permissions (username,password)


@csrf_exempt
def books(request):
    if request.method == "GET":
        books = BookModel.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=404)



# bookapi(book_name,author,quantity=10,copies_sold)

# api/v1/books/id
@csrf_exempt
def book_detail(request,id):
    book = BookModel.objects.get(id=id)
    if request.method =="GET":
        serializer=BookSerializer(book)
        return JsonResponse(serializer.data,status=200,safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BookSerializer(instance=book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=404)
    elif request.method == "DELETE":
        book.delete()
        return JsonResponse({"message":"Deleted"})


class MyBooks(APIView):

    def get(self,request):
        books = BookModel.objects.all()
        serializer = BookClassSerializer(books,many=True)
        return Response(serializer.data,status=200)
    def post(self,request):
        serializer = BookClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)


class MyBookDetails(APIView):

    def get_object(self,id):
        try:
            return BookModel.objects.get(id=id)
        except:
            return Http404

    def get(self,request,*args,**kwargs):
        book = self.get_object(id=kwargs.get("id"))
        serializer = BookClassSerializer(book)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        book = self.get_object(id=kwargs.get("id"))
        serializer = BookClassSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)
    def delete(self,request,*args,**kwargs):
        book = self.get_object(id=kwargs.get("id"))
        book.delete()
        return Response({"msg":"Book is deleted"})


class Mbooks(generics.GenericAPIView,
             mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = BookModel.objects.all()
    serializer_class = BookClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["book_name","author","price","pages"]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class MbookDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset = BookModel.objects.all()
    serializer_class = BookClassSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class SignInView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("passwords")
            user = authenticate(request,username=username,password=password)
            if user:
                token,created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=200)
            else:
                return Response({"msg":"invalid credentials"},status=400)
        else:
            return Response({"msg": "Check for Validity of credentials"}, status=400)