from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="index.html"),
        kwargs={'active_view':'index'},
        name="index"),
    url(r'^map/$', TemplateView.as_view(template_name="location.html"),
        kwargs={'active_view':'location'},
        name="location"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"),
        kwargs={'active_view':'contact'},
        name="contact"),
    url(r'^projects/$', TemplateView.as_view(template_name="projects.html"),
        kwargs={'active_view':'projects'},
        name="projects"),

)
