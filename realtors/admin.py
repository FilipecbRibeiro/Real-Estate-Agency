from django.contrib import admin

# Register your models here.

from .models import Realtor


class RealtorsAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'phone', 'hire_date', 'is_emp_month' )
    list_display_links=('id', 'name')
    list_editable=('email', 'phone', 'is_emp_month')
    list_per_page=5
    search_field=('name')
    
admin.site.register(Realtor,RealtorsAdmin)
