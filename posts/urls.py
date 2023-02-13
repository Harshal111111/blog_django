from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = 'index'),
    path("post/<str:pk>", views.post, name = 'post'),
    path('contact',views.contact_page, name = 'contact'),
    path('about',views.about_page, name = 'about')
]