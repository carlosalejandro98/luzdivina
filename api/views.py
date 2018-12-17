from rest_framework import generics
from .serializers import ComunidadSerializers, BodaSerializers, BautizoSerializers, ComunionSerializers, PersonaSerializers, ComunionSerializersSolicitud, BautizoSerializersSolicitud, BodaSerializersSolicitud 
from core.models import Comunidad, Boda, Bautizo, Comunion, Persona, BodaSolicitud, ComunionSolicitud, BautizoSolicitud
# Create your views here.
class ComunidadLista(generics.ListCreateAPIView):
    queryset = Comunidad.objects.all()
    serializer_class= ComunidadSerializers

class ComunidadDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunidad.objects.all()
    serializer_class=ComunidadSerializers

class BodaLista(generics.ListCreateAPIView):
    queryset = Boda.objects.all()
    serializer_class= BodaSerializers

class BodaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boda.objects.all()
    serializer_class= BodaSerializers    

class BautizoLista(generics.ListCreateAPIView):
    queryset = Bautizo.objects.all()
    serializer_class= BautizoSerializers

class BautizoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bautizo.objects.all()
    serializer_class= BautizoSerializers  

class ComunionLista(generics.ListCreateAPIView):
    queryset = Comunion.objects.all()
    serializer_class= ComunionSerializers

class ComunionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comunion.objects.all()
    serializer_class= ComunionSerializers  

class PersonaLista(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class= PersonaSerializers

class PersonaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class= PersonaSerializers

class BodaListaSolicitud(generics.ListCreateAPIView):
    queryset = BodaSolicitud.objects.all()
    serializer_class= BodaSerializersSolicitud

class BodaDetalleSolicitud(generics.RetrieveUpdateDestroyAPIView):
    queryset = BodaSolicitud.objects.all()
    serializer_class= BodaSerializersSolicitud    

class BautizoListaSolicitud(generics.ListCreateAPIView):
    queryset = BautizoSolicitud.objects.all()
    serializer_class= BautizoSerializersSolicitud

class BautizoDetalleSolicitud(generics.RetrieveUpdateDestroyAPIView):
    queryset = BautizoSolicitud.objects.all()
    serializer_class= BautizoSerializersSolicitud  

class ComunionListaSolicitud(generics.ListCreateAPIView):
    queryset = ComunionSolicitud.objects.all()
    serializer_class= ComunionSerializersSolicitud

class ComunionDetalleSolicitud(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComunionSolicitud.objects.all()
    serializer_class= ComunionSerializersSolicitud  
