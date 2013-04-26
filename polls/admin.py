from django.contrib import admin
from polls.models import Poll,Choice

#admin.site.register(Poll)

class ChoiceInline(admin.StackedInline):
    model=Choice
    extra=3


class PollAdmin(admin.ModelAdmin):
    #fields=['pub_date','question']
    fieldsets=[(None,{'fields':['question']}),('Date information', {'fields':['pub_date']}),]
    inlines=[ChoiceInline]
    list_display=('question','pub_date','was_published_recently')
    
admin.site.register(Poll,PollAdmin)



#from polls.models import Choice

#admin.site.register(Choice)