from django.contrib import admin
from .models import Question,Choice

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)

#using tabular inline
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date Info',{'fields':['published_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)