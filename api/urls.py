from django.urls import path
from .views import SignInView,books,book_detail,MyBooks,MyBookDetails,Mbooks,MbookDetail
from django.views.generic import TemplateView

urlpatterns=[
    path('name',TemplateView.as_view(template_name='home.html')),
    path('books',books,name="getbooks"),
    path('books/<int:id>',book_detail,name="detail"),
    path('cbooks',MyBooks.as_view(),name="cbooks"),
    path('cbooks/<int:id>',MyBookDetails.as_view(),name="cdetail"),
    path('mbooks',Mbooks.as_view(),name="mbook"),
    path('mbook/<int:pk>',MbookDetail.as_view(),name="Mdetail"),
    path('signin',SignInView.as_view(),name="login"),
]