from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index-page"),
    path('about-us', views.about_us, name="about-page"),
    path('our-projects', views.our_projects, name="projects-page"),
    path('reviews', views.reviews, name="reviews-page"),
    path('contact-us', views.contact_us, name="contact-page"),
    path('sales', views.sales, name="sales-page"),
    path('order-page', views.order_page, name="order-page"),
    path('order-page/<slug:slug>', views.order_form, name="order-form")
]
