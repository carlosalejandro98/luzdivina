from core.models import Comunidad, Boda, Bautizo, Comunion, Persona, BodaSolicitud, ComunionSolicitud, BautizoSolicitud
from rest_framework import serializers

class ComunidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields= ('id', 'nombre')

class BodaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Boda
        fields = ('id', 'nombreNovia', 'nombreNovio', 'numeroContacto', 'emailContacto', 'tipoParroquia')

class BautizoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bautizo
        fields = ('id', 'bautizado', 'edad', 'padrino', 'madrina', 'tipoParroquia')

class ComunionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunion
        fields = ('id', 'nombreComunion', 'edad', 'numeroContacto', 'emailContacto', 'direccion', 'tipoParroquia')

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'nombre', 'apellido', 'edad')

class BodaSerializersSolicitud(serializers.ModelSerializer):
    class Meta:
        model = BodaSolicitud
        fields = ('id', 'nombreNovia', 'nombreNovio', 'numeroContacto', 'emailContacto', 'tipoParroquia')

class BautizoSerializersSolicitud(serializers.ModelSerializer):
    class Meta:
        model = BautizoSolicitud
        fields = ('id', 'bautizado', 'edad', 'padrino', 'madrina', 'tipoParroquia')

class ComunionSerializersSolicitud(serializers.ModelSerializer):
    class Meta:
        model = ComunionSolicitud
        fields = ('id', 'nombreComunion', 'edad', 'numeroContacto', 'emailContacto', 'direccion', 'tipoParroquia')