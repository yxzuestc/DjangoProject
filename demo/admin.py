# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Question, Choice
from django.contrib import admin

# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Infomation', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    # 在question中显示choice
    list_display = ('question_text', 'pub_date', 'was_published_recently')  #显示的字段
    list_filter = ['pub_date']      #过滤器
    search_fields = ['question_text']   #搜索


admin.site.register(Question, QuestionAdmin)
