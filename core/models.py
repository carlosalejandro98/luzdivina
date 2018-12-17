from django.db import models

# Create your models here.


class Comunidad(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Agente(models.Model):
    nombreAgente = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreAgente

class Ministro(models.Model):
    nombreMinistro = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreMinistro

class Coordinador(models.Model):
    nombreCoordinador = models.CharField(max_length=45)

    def __str__(self):
        return self.nombreCoordinador

class Comunidadcatolica(models.Model):
    NombreComunidad = models.CharField(max_length=45)

    def __str__(self):
        return self.NombreComunidad

class Login(models.Model):
    usuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)

    def __str__(self):
        return self.usuario


class Bautizo(models.Model):
    bautizado = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    padrino = models.CharField(max_length=45)
    madrina = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.bautizado

class BautizoSolicitud(models.Model):
    bautizado = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    padrino = models.CharField(max_length=45)
    madrina = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.bautizado


class Boda(models.Model):
    nombreNovia = models.CharField(max_length=45)
    nombreNovio = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreNovia

class BodaSolicitud(models.Model):
    nombreNovia = models.CharField(max_length=45)
    nombreNovio = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreNovia


class Comunion(models.Model):
    nombreComunion = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComunion

class ComunionSolicitud(models.Model):
    nombreComunion = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComunion

class Persona(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre