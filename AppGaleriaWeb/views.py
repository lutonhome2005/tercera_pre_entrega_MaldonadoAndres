from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import * 
from django.urls import path
from AppGaleriaWeb import views


# Create your views here.

#Creamos la vista de Inicio
def index(request):
    return render(request, 'index.html')

#Creamos la vista de Inicio
def artistas(request):
    return render(request, 'artistas.html')

#Creamos la vista para Galerias
def galerias(request):
    return render(request, 'galerias.html')

#Creamos la vista para Registrarse
def registrarse(request):
    return render(request,'registrarse.html')

#Creamos la vista de Registro de usuarios
def registrar (request):
    return render(request,'registro.html')


#Creamos la vista de contactos
def contactos(request):
    return render(request,'contactos.html')

#def formularioAltaArtista(request):
    
#    return render(request,'formularioAltaArtista.html')

def formularioAltaArtista(request):
    
    if request.method == 'POST':
        # Obtengo los datos del formulario
        nombre_artista = request.POST['nombreArtista']
        apellido_artista = request.POST['apellidoArtista']
        nacionalidad_artista = request.POST['nacionalidadArtista']
        email_artista = request.POST['emailArtista']
        tipo = request.POST['tipo']  # Obtener el tipo de usuario
        #Creo la instancia del modelo Artista y la guarda en BD
        
        artista = Artista(
                nombreArtista=nombre_artista,
                apellidoArtista=apellido_artista,
                nacionalidadArtista=nacionalidad_artista,
                emailArtista=email_artista
            )
        artista.save()
            
        #form = formularioAltaArtista(request.POST)
        return render(request, 'index.html')  # si todo salio bien envia a págian de inicio
    
    else:
        # es una solicitud GET, mostrar de nuevo el formulario
        #return render(request,'formularioAltaArtista.html')
        return render(request, 'formularioAltaArtista.html')

from .models import Usuario  # Asegúrate de importar el modelo adecuado

#Creo la funcion para dar de alta los usuarios
def formularioAltaUsuario(request):
    if request.method == 'POST':
        # Obtengo los datos del formulario
        nombre_usuario = request.POST['nombreUsuario']
        apellido_usuario = request.POST['apellidoUsuario']
        edad_usuario = request.POST['edadUsuario']
        email_usuario = request.POST['emailUsuario']
        # Creo la instancia del modelo Usuario y la guardo en la BD
        
        usuario = Usuario(
            nombreUsuario=nombre_usuario,
            apellidoUsuario=apellido_usuario,
            edadUsuario=edad_usuario,
            emailUsuario=email_usuario
        )
        usuario.save()
        
        # Puedes mostrar un mensaje de éxito si lo deseas
        return render(request, 'index.html') 

        

    else:
        # Es una solicitud GET, mostrar el formulario
        return render(request, 'formularioAltaUsuario.html')


#Creo funcion para dar de alta la obra.

def formularioAltaObraArte(request):
    artistas = Artista.objects.all() 
    if request.method == 'POST':
        # Obtengo los datos del formulario
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        autor_id = request.POST['autor']
        precio = request.POST.get('precio')  # Podría ser nulo, por lo que usamos get
        imagen = request.FILES['imagen']
        fecha_creacion = request.POST['fechaCreacion']
        vendido = request.POST.get('vendido', False)  # Podría ser nulo, por lo que usamos get

        # Creo la instancia del modelo ObraArte y la guardo en la BD
        obra_arte = ObraArte(
            titulo=titulo,
            descripcion=descripcion,
            autor_id=autor_id,
            precio=precio,
            imagen=imagen,
            fechaCreacion=fecha_creacion,
            vendido=vendido
        )
        obra_arte.save()

        # Puedes mostrar un mensaje de éxito si lo deseas
        return render(request, 'index.html')

    else:
        # Es una solicitud GET, mostrar el formulario
        return render(request, 'formularioAltaObraArte.html', {'artistas': artistas})
        #return render(request, 'formularioAltaObraArte.html')



# Creo la funcion para dar de alta las galerías
from django.shortcuts import render
from .models import Galeria, ObraArte

# Vista para el formulario de alta de galería
def formularioAltaGaleria(request):
    # Obtén la lista de obras de arte disponibles para asociar a la galería
    obras_de_arte = ObraArte.objects.all()

    if request.method == 'POST':
       
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha_creacion = request.POST['fechaCreacion']
        obras_seleccionadas = request.POST.getlist('obras')

        # Crea la instancia de Galeria
        galeria = Galeria(
            nombre=nombre,
            descripcion=descripcion,
            fechaCreacion=fecha_creacion
        )
        galeria.save()

        # Asocia las obras de arte seleccionadas a la galería
        galeria.obras.set(obras_seleccionadas)

        # Puedes mostrar un mensaje de éxito si lo deseas
        return render(request, 'index.html')

    else:
        # Es una solicitud GET, muestra el formulario de alta de galería
        return render(request, 'formularioAltaGaleria.html', {'obras_de_arte': obras_de_arte})


# Vista para el formulario de alta los carritos

def formularioAltaCarrito(request):
    # Obtén la lista de obras de arte disponibles para agregar al carrito
    obras_de_arte = ObraArte.objects.all()
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        comprador_id = request.POST['comprador']
        obras_seleccionadas = request.POST.getlist('obras')

        # Crea la instancia del Carrito
        carrito = Carrito(comprador_id=comprador_id)
        carrito.save()

        # Asocia las obras de arte seleccionadas al carrito
        carrito.obras.set(obras_seleccionadas)

        

        # Puedes mostrar un mensaje de éxito si lo deseas
        return render(request, 'index.html')

    else:
        # Es una solicitud GET, muestra el formulario de alta de carrito
        return render(request, 'formularioAltaCarrito.html', {'obras_de_arte': obras_de_arte, 'usuarios': usuarios})

#Listadossss

#Listados de Artistas
def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'artistas.html', {'artistas': artistas})

#Listado de Galerias
from django.shortcuts import render
from .models import Galeria, ObraArte

def lista_galerias(request):
    galerias = Galeria.objects.all()
    
    # Crear una lista de diccionarios para almacenar obras y artistas de cada galería
    galerias_info = []
    for galeria in galerias:
        obras = galeria.obras.all()
        obras_info = [{'nombre_obra': obra.titulo, 'nombre_artista': obra.autor.nombreArtista} for obra in obras]
        galeria_info = {'nombre_galeria': galeria.nombre, 'obras_info': obras_info}
        galerias_info.append(galeria_info)
    
    return render(request, 'galerias.html', {'galerias_info': galerias_info})

#Busqueda de artistas
def buscar_artista(request):
    resultados = None
    sin_resultados= False 

    if request.method == 'POST':
        nombre = request.POST.get('nombre_artista')
        apellido = request.POST.get('apellido_artista')
        nacionalidad = request.POST.get('nacionalidad_artista')
        email = request.POST.get('email_artista')

        # Realiza la búsqueda en base a los campos del formulario
        resultados = Artista.objects.filter(
            nombreArtista__icontains=nombre,
            apellidoArtista__icontains=apellido,
            nacionalidadArtista__icontains=nacionalidad,
            emailArtista__icontains=email
        )
        if not resultados:
            sin_resultados = True
            
    else:
        nombre = ''
        apellido = ''
        nacionalidad = ''
        email = ''

    return render(request, 'buscar_artista.html', {
        'nombre': nombre,
        'apellido': apellido,
        'nacionalidad': nacionalidad,
        'email': email,
        'resultados': resultados,
        'sin_resultados': sin_resultados,
    })

