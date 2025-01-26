from django.contrib import admin
from .models import Questions,Quiz,Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class AnswerinLine(admin.TabularInline):
    model = Answer
    fields = ['answers','is_right']

class QuiestionsAdmin(admin.ModelAdmin):
    list_display = ['title','quiz','date_created']
    inlines = [AnswerinLine]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answers','is_right','question']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuiestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
