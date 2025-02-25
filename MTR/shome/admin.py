from django.contrib import admin

# Register your models here.
from .models import product,Softwarez,Gaming,Contact
admin.site.register(product)
admin.site.register(Softwarez)
admin.site.register(Gaming)
admin.site.register(Contact)