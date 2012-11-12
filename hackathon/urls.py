from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^$', TemplateView.as_view(template_name="location.html"), name="location"),
    url(r'^$', TemplateView.as_view(template_name="contact.html"), name="contact"),

)
