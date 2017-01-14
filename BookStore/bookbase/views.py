from django.shortcuts import render_to_response, redirect
from django.views.generic.edit import FormView
from bookbase.forms import LoginForm, SignUpForm,CartForm
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.contrib.auth import login 
from django.contrib.auth import logout
from bookbase.models import Book 
from bookbase.models import Cart 
from django.template import loader
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_protect
from bookbase import codes

# Create your views here.
class IndexView(FormView):

	form_class= LoginForm
	template_name = 'index.html'
	success_url = 'books/' 
	
	def dispatch(self, *args, **kwargs):
		return super(IndexView,self).dispatch(*args , **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())
		success_url = 'books/'
		if (self.request.session.test_cookie_worked()):
			self.request.session.delete_test_cookie()

		return super(IndexView,self).form_valid(form)	
	
	def get_context_data(self, **kwargs):
		context = super(IndexView,self).get_context_data(**kwargs)
		return context

	def form_invalid(self, form):	
		return self.render_to_response(self.get_context_data(form=form))

class SignUpView(FormView):
	form_class= SignUpForm
	template_name = 'signup.html' 
	success_url = ''
	def dispatch(self, *args, **kwargs):
		return super(SignUpView,self).dispatch(*args,**kwargs)


	def form_valid(self,form):
			username = form.cleaned_data['username'] #username
			email = form.cleaned_data['email'] #email
			password = form.cleaned_data['password'] #password
			password_again = form.cleaned_data['password_again']
			if (password == password_again):
 				user = User.objects.create_user(username = username, email=email , password = password)
 				user.save()
		        redirect_to = settings.LOGIN_REDIRECT_URL
		    	
			return super(SignUpView,self).form_valid(form)	
	
	def get_context_data(self, **kwargs):
		context = super(SignUpView,self).get_context_data(**kwargs) 
		return context
		

	def form_invalid(self,form):
		return self.render_to_response(self.get_context_data(form=form))	

class BooksView(TemplateView):
	template_name = 'books.html'
	def get_context_data(self, **kwargs):
		context = super(BooksView, self).get_context_data(**kwargs)
		
		sortby = self.request.GET.get('sortby')
		
		if sortby == None:
			sortby = 'title'
		
		age = str(self.request.GET.get('age' ))
		category = str(self.request.GET.get('category' ))
		
		genre = str(self.request.GET.get('genre'))
		
		
		
		
		
		 
		sort_options = {'title':'title', 'price_low':'price', 'price_high':'-price', 'rating':'rating' }
		context['cat_q']= str(category)
		context['age_q'] = str(age)
		context['genre_q'] = str(genre)
		
		try:
			context['book_list'] = Book.objects.order_by(sort_options[sortby])	
			context['debug'] = 1
			if category == 'None':
				context['book_list'] = Book.objects.order_by(sort_options[sortby])
				context['debug'] = 2
			if category == '1':
				context['book_list'] = Book.objects.filter(category=1).order_by(sort_options[sortby])
				context['debug'] = 3
				if genre != 'None' and age!= 'None':
					context['book_list'] = Book.objects.filter(category=1,genre=genre,age_group=age).order_by(sort_options[sortby])
					context['debug'] = 4
				elif genre!= 'None':
					context['book_list'] = Book.objects.filter(category=1,genre=genre).order_by(sort_options[sortby])
					context['debug'] = 5
				elif age!= 'None':
					context['book_list'] = Book.objects.filter(category=1,age_group=age).order_by(sort_options[sortby])
					context['debug'] = 6
			if category == '2':
				context['book_list'] = Book.objects.filter(category=2).order_by(sort_options[sortby])
				context['debug'] = 11
				if genre != 'None' and age!= 'None':
					context['book_list'] = Book.objects.filter(category=2, genre=genre, age_group=age).order_by(sort_options[sortby])
					context['debug'] = 7
				elif genre != 'None':
					context['book_list'] = Book.objects.filter(category=2, genre=genre).order_by(sort_options[sortby])
					context['debug'] = 8			
				elif age != 'None':					
					context['book_list'] = Book.objects.filter(category=2,  age_group=age).order_by(sort_options[sortby])
					context['debug'] = 9
		except KeyError:
			books =  Book.objects.order_by(sort_options['title'])
			for book in books:
				book.in_user_cart = False
				for cartentry in Cart.objects.all():
					if cartentry.book == book and cartentry.customer == self.request.user:
						book.in_user_cart = True	
			context['book_list'] = books
			context['debug'] = 10
			
		books = context['book_list']
		for book in books:
				book.in_user_cart = False
				for cartentry in Cart.objects.all():
					if cartentry.book == book and cartentry.customer == self.request.user:
						book.in_user_cart = True
		categories = []
		agegroups = []
		tags = []
		genres = []
		for category in codes.CATEGORY:
			temp = {} 
			temp['code'] = category[0]
			temp['text'] = category[1]
			categories.append(temp)
		for agegroup in codes.AGEGROUP:
			temp = {} 
			temp['code'] = agegroup[0]
			temp['text'] = agegroup[1]
			agegroups.append(temp)
		for tag in codes.TAG:
			temp = {} 
			temp['code'] = tag[0]
			temp['text'] = tag[1]
			tags.append(temp)
		for genre in codes.GENRE:
			temp = {} 
			temp['code'] = genre[0]
			temp['text'] = genre[1]
			genres.append(temp)

		context['categories'] = categories
		context['agegroups']=agegroups
		context['tags']=tags
		context['genres']=genres
		if not len(context['book_list']): 
			context['no_books'] = "There are no books to display"
		context['mediaroot'] = settings.MEDIA_ROOT
		return context
    	def dispatch(self, *args, **kwargs):
    		return super(BooksView,self).dispatch(*args,**kwargs)

class BookDetailView(TemplateView):
	template_name = 'bookdetail.html'
	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		return context



class CartView(TemplateView):
	
	template_name = 'cart.html'
	def get_context_data(self,**kwargs):

		UserId = self.request.user	
		context = super(CartView,self).get_context_data(**kwargs)
		
		total = 0
		bookIds = Cart.objects.values_list('book',flat=True).filter(customer=UserId)
		book_prices = Book.objects.values_list('price',flat=True).filter(pk__in=set(bookIds))
		for i in book_prices:
			total = total + i

		context['cartOfUser'] = Book.objects.filter(id__in=set(bookIds)) 	
		context['total_price'] = total 
		return context
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
    		return super(CartView,self).dispatch(*args,**kwargs)	
 	


class LoginView(FormView):

	form_class= LoginForm
	template_name = 'login.html'
	success_url = '/books/' 
	
	def dispatch(self, *args, **kwargs):
		return super(LoginView,self).dispatch(*args , **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())
		success_url = '/books/'
		if (self.request.session.test_cookie_worked()):
			self.request.session.delete_test_cookie()
			

		return super(LoginView,self).form_valid(form)	
	
	def get_context_data(self, **kwargs):
		context = super(LoginView,self).get_context_data(**kwargs)
		return context

	def form_invalid(self, form):	
		return self.render_to_response(self.get_context_data(form=form))


#@csrf_protect
def addToCart(request,get_book):
	book = Book.objects.get(id=get_book)	
	user = request.user
	cart = Cart.objects.create(book=book, customer=user, status=1, quantity=1)	
	cart.save()
	return redirect('/books/')
#@csrf_protect
def deleteFromCart(request, get_book):
	book = Book.objects.get(id=get_book)
	user = request.user
	cart = Cart.objects.filter(book=book, customer=user).delete()
	return redirect('/cart/')
	
	
	
