from django.conf.urls import url
from bookbase.views import SignUpView, LoginView, IndexView, BooksView, BookDetailView, CartView,addToCart, deleteFromCart
from django.conf import settings



urlpatterns = [
		url(r'^$',IndexView.as_view(),name = 'index'),
		url(r'signup',SignUpView.as_view(),name = 'signup'),
		url(r'^books',BooksView.as_view(),name = 'books'),
		url(r'^bookdetails/[0-9]{4}',BookDetailView.as_view()),
		url(r'AddingtoCart/([0-9]+)/$',addToCart,name='addtocart'),
		url(r'deleteFromCart/([0-9]+)/$',deleteFromCart, name='deletecart'),
		url(r'^cart/',CartView.as_view()),
		url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
		url(r'accounts/login/', LoginView.as_view()),
		] 

