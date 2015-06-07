# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuastionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_date', 'was_published_recently')
    fieldsets = [
        (None,    {'fields' : ['question_text']}), 
        ('Время', {'fields' : ['question_date'], 'classes' : ['collapse']})      
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuastionAdmin)