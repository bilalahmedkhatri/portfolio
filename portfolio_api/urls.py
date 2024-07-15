from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio_api.views.testimonialview import testimonial_view, testimonial_form_submittion, TestimonialAPI
from portfolio_api.views.contactview import contact_form_view
from portfolio_api.views.projects import projects_view


urlpatterns = [
    path('testimonial/', testimonial_view, name="testimonial"),
    path('contact-form/', contact_form_view, name="contect-form"),
    path('projects/', projects_view, name="projects"),
    # django templates views
    path("testimonial-form-submittion",
         testimonial_form_submittion, name="testimonial-form"),
    # will work on that - test kiya likn kush issues hain
    path('testimonial-class/', TestimonialAPI.as_view(), name='class-testimonial')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
