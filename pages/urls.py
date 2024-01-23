from django.urls import path

from pages.views import home_page_view, contact_page_view, blog_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('', contact_page_view, name='contact'),
    path('blog', blog_page_view, name='blog'),
]