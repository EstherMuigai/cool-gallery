from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^categories$',views.categories,name = 'categories'),
    url('^category$', views.category, name='category_results'),
    url('^location/[a-zA-Z]',views.location,name = 'location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    