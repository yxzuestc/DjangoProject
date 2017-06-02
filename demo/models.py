# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question_text
    def was_published_recently(self):
        return timezone.now() - self.pub_date <= datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
