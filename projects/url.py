from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('site/<webapp_id>',views.site,name='site'),
    path('profile/<username>',views.profile,name='profile'),
    path('all-projects/',views.search_all_projects,name='search_all_projects'),
    path('api/profile/',views.ProfileList.as_view(),name='profilelist'),
    path('api/webapp/',views.ProjectsList.as_view(),name='projectlist'),
    path('newproject/',views.create_new_project,name='create_new_project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)