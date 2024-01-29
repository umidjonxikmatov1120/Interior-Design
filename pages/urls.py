from django.urls import path

from pages.views import contact_page_view, blog_page_view

app_name = 'pages'

urlpatterns = [
    path('', contact_page_view, name='contact'),
    path('blog/', blog_page_view, name='blog'),
]