from django.urls import path

from .views import SignUpView, about, index


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', about, name='about'),
    path('index/', index, name='index')
]
