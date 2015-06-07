# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.template.defaultfilters import default
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Вопрос',max_length = 200)
    question_date = models.DateField('Время публикации')
    
    def __unicode__(self):
        return self.question_text
      
    def was_published_recently(self):
        return self.choice_set.count()>= 0
    #was_published_recently.admin_order_field = 'question_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Есть ответы?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('Ответ',max_length = 200)
    choice_votes = models.IntegerField('Голоса',default = 0)
    
    def __unicode__ (self):
        return ' // '.join((self.choice_text,str(self.choice_votes)))