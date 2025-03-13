from django.contrib import admin
from .models import Doctor, Designation, Specialization, AvailableTime, Review

# Register your models here.

admin.site.register(AvailableTime)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', ), }

# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'rating']

#     def first_name(self, obj):
#         return obj.reviewer.user.first_name
    
#     def last_name(self, obj):
#         return obj.reviewer.user.last_name

admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Doctor)
admin.site.register(Review)

