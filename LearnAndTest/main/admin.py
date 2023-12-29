from django.contrib import admin

from .models import Tests, Teachers, Questions, Answers, Library, Students

admin.site.register(Tests)
admin.site.register(Teachers)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Library)
admin.site.register(Students)
