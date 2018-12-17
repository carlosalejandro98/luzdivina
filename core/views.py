from django.shortcuts import render
from .models import Comunidad, Boda, Bautizo, Comunion, Comunidadcatolica, Agente, Coordinador, Ministro, BodaSolicitud, ComunionSolicitud, BautizoSolicitud

# Create your views here.


def Home(request):
    return render(request, 'core/index.html')

def Cliente(request):
    return render(request, 'core/listadoCliente.html')

def ListadoBoda(request):
    return render(request, 'core/listadoBodas.html')

def ListadoBautizo(request):
    return render(request, 'core/listadoBautizo.html')



def ListadoComunion(request):
    return render(request, 'core/listadoComunion.html')

def FormularioAgente(request):
    lt = Agente.objects.all()
    if request.POST:
        nombreAgente = request.POST["nombreAgente"]
       
        agente = Agente(
            nombreAgente = nombreAgente
        )

        agente.save()
    return render(request, 'core/formularioAgente.html', {'agentes': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formularioAgente.html', {'agentes': lt})

def FormularioMinistro(request):
    lt = Ministro.objects.all()
    if request.POST:
        nombreMinistro = request.POST["nombreMinistro"]
       
        ministro = Ministro(
            nombreMinistro = nombreMinistro
        )

        ministro.save()
    return render(request, 'core/formularioMinistro.html', {'ministros': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formularioMinistro.html', {'ministros': lt})


def FormularioCoordinador(request):
    lt = Coordinador.objects.all()
    if request.POST:
        nombreCoordinador = request.POST["nombreCoordinador"]
       
        coordinador = Coordinador(
            nombreCoordinador = nombreCoordinador
        )

        coordinador.save()
    return render(request, 'core/formularioCoordinador.html', {'coordinadores': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formularioCoordinador.html', {'coordinadores': lt})


def Bautiso(request):
    listado = Bautizo.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formularioBautizo.html', {'listado': listado, 'comunidadCatolica': comunidadCatolica})


def Formulario(request):
    lt = Comunidad.objects.all()
    if request.POST:
        nombreNovia = request.POST["nombreNovia"]
        nombreNovio = request.POST["nombreNovio"]
        numeroContacto = request.POST["numeroContacto"]
        emailContacto = request.POST["emailContacto"]
        tipoParroquia = request.POST["tipoParroquia"]

        obj_tipo = Comunidad.objects.get(id=tipoParroquia)

        boda = Boda(
            nombreNovia=nombreNovia,
            nombreNovio=nombreNovio,
            numeroContacto=numeroContacto,
            emailContacto=emailContacto,
            tipoParroquia=obj_tipo
        )

        boda.save()
    return render(request, 'core/formulario.html', {'tipoParroquias': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formulario.html', {'tipoParroquias': lt})


def Comunione(request):
    listado = Comunion.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formularioComunion.html', {'listado': listado, 'comunidadCatolica': comunidadCatolica})


def Listado2(request):
    listado = Comunidad.objects.all()
    listado_uno = Agente.objects.all()
    listado_dos = Coordinador.objects.all()
    listado_tres = Ministro.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/indexLogin.html', {'listado': listado, 'listado_uno': listado_uno, 'listado_dos': listado_dos, 'listado_tres': listado_tres, 'comunidadCatolica': comunidadCatolica})

def Listado(request):
    listado = Boda.objects.all()
    comunidadCatolica = Comunidadcatolica.objects.all()
    return render(request, 'core/formulario.html', {'listado': listado, 'comunidadCatolica': comunidadCatolica})

def ListadoBoda(request):
    listado = BodaSolicitud.objects.all()
    return render(request, 'core/listadoBodas.html', {'listado': listado})

def ListadoBautizo(request):
    listado = BautizoSolicitud.objects.all()
    return render(request, 'core/listadoBautizo.html', {'listado': listado})

def ListadoComunion(request):
    listado = ComunionSolicitud.objects.all()
    return render(request, 'core/listadoComunion.html', {'listado': listado})


def Login(request):
    if request.POST:
        usuario = request.POST["usuario"]
        password = request.POST["password"]
        login = Login.objects.get(usuario=usuario, password=password)
    return render(request, 'core/login.html')

def IndexLogin(request):
    return render(request, 'core/indexLogin.html')


def FormularioComunidad(request):
    lt = Comunidadcatolica.objects.all()
    if request.POST:
        NombreComunidad = request.POST["NombreComunidad"]
       
        comunidadCatolica = Comunidadcatolica(
            NombreComunidad = NombreComunidad
        )

        comunidadCatolica.save()
    return render(request, 'core/formularioComunidad.html', {'comunidades': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formularioComunidad.html', {'comunidades': lt})

def FormularioParroquia(request):
    lt = Comunidad.objects.all()
    if request.POST:
        nombre = request.POST["nombre"]
       
        comunidad = Comunidad(
            nombre = nombre
        )

        comunidad.save()
    return render(request, 'core/formularioParroquia.html', {'parroquias': lt, 'mensaje': 'Registrado Correctamente'})

    return render(request, 'core/formularioParroquia.html', {'parroquias': lt})