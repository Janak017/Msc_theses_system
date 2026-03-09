from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Thesis)
admin.site.register(Evaluation)
admin.site.register(CommitteeMember)
admin.site.register(Submission)
admin.site.register(ThesisCommittee)
admin.site.register(UserProfile)