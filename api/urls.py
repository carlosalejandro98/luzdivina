
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^comunidad_detalle/$',views.ComunidadLista.as_view()),
    url(r'^comunidad_detalle/(?P<pk>[0-9]+)/$',views.ComunidadDetalle.as_view()),
    url(r'^boda_detalle/$',views.BodaLista.as_view()),
    url(r'^boda_detalle/(?P<pk>[0-9]+)/$',views.BodaDetalle.as_view()),
    url(r'^bautizo_detalle/$',views.BautizoLista.as_view()),
    url(r'^bautizo_detalle/(?P<pk>[0-9]+)/$',views.BautizoDetalle.as_view()),
    url(r'^comunion_detalle/$',views.ComunionLista.as_view()),
    url(r'^comunion_detalle/(?P<pk>[0-9]+)/$',views.ComunionDetalle.as_view()),
    url(r'^persona_detalle/$', views.PersonaLista.as_view()),
    url(r'^persona_detalle/(?P<pk>[0-9]+)/$',views.PersonaDetalle.as_view()),
    url(r'^boda_detalle_solicitud/$',views.BodaListaSolicitud.as_view()),
    url(r'^boda_detalle_solicitud/(?P<pk>[0-9]+)/$',views.BodaDetalleSolicitud.as_view()),
    url(r'^bautizo_detalle_solicitud/$',views.BautizoListaSolicitud.as_view()),
    url(r'^bautizo_detalle_solicitud/(?P<pk>[0-9]+)/$',views.BautizoDetalleSolicitud.as_view()),
    url(r'^comunion_detalle_solicitud/$',views.ComunionListaSolicitud.as_view()),
    url(r'^comunion_detalle_solicitud/(?P<pk>[0-9]+)/$',views.ComunionDetalleSolicitud.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)