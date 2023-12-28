from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.home, name='my-home'),
    path('about', views.about, name='my-about'),
    path('services', views.services, name='my-services'),
    path('team', views.team, name='my-team'),
    path('career', views.career, name='my-career'),
    path('hire-us', views.hireus, name='hire-us'),
    path('portfolio', views.portfolio, name='my-portfolio'),
    path('contact', views.contact, name='my-contact')
    
]
