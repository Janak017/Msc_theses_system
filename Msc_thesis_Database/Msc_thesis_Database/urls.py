from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Accounts & Authentication
    path('', include('apps.accounts.urls')),
    # Departments
    path('departments/', include('apps.departments.urls')),
    # Students
    path('students/', include('apps.students.urls')),
    # Supervisors
    path('supervisors/', include('apps.supervisors.urls')),
    # Theses
    path('theses/', include('apps.theses.urls')),
    # Legacy app (for backward compatibility during migration)
    path('legacy/', include('thesis.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)