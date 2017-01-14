from django.contrib import admin
from bookbase.models import Book, Customer, Cart
# Register your models here.
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.site_header = 'Book Base Administration'