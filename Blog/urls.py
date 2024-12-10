from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    #path("category/<str:category_name>/", views.blog_category, name="blog_category"),
    path("category/<str:category_name>/", views.blog_category, name="blog_category"),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    
]