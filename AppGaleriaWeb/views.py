from django.shortcuts import render , get_object_or_404,redirect
from django.http import HttpResponse
from .models import * 
from django.urls import path, reverse
from AppGaleriaWeb import views
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
#Envio de email
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.

def enviar_correo(request):
    if request.method == 'POST':
        nombre_completo = request.POST['nombre_completo']
        telefono = request.POST['telefono']
        email = request.POST['email']
        asunto = request.POST['asunto']
        descripcion = request.POST['descripcion']

        # Cuerpo del mensaje
        mensaje = f'Nombre: {nombre_completo}\nTeléfono: {telefono}\nEmail: {email}\nAsunto: {asunto}\nDescripción: {descripcion}'

        try:
            # Enviar correo
            send_mail(
                'Formulario de Contacto',  # Asunto del correo
                mensaje,  # Cuerpo del correo
                settings.EMAIL_HOST_USER,  # Remitente
                ['CoderPtyhonWeb2023@gmail.com'],  # Destinatario
                fail_silently=False,
            )
            return redirect('email_exitoso')  # Redirige a una página de éxito
        except Exception as e:
            # Manejo de errores (puedes personalizar esto)
            return redirect('email_fallido')  # Redirige a una página de error
    else:
        return render(request, 'contactos.html')
    

# Vista para enviar una consulta de un artista
def enviar_consulta_artista(request):
    artista_id = request.GET.get('artista_id')
    obra_id = request.GET.get('obra_id')
    
  
    artista = get_object_or_404(Artista, pk=artista_id)
    obra = get_object_or_404(ObraArte, pk=obra_id) if obra_id else None
    
    if request.method == 'POST':
        nombre_completo = request.POST['nombreCompleto']
        telefono = request.POST['telefono']
        email = request.POST['email']
        mensaje = request.POST['mensaje']

        # Dirección de correo a la que se enviará la consulta
        destinatario = artista.emailArtista  # Cambia esto a la dirección de correo real

        # Cuerpo del mensaje
        cuerpo_mensaje = f'Nombre: {nombre_completo}\nTeléfono: {telefono}\nEmail: {email}\nMensaje: {mensaje}'

        try:
            # Enviar correo
            send_mail(
                'Consulta de Artista',  # Asunto del correo
                cuerpo_mensaje,  # Cuerpo del correo
                email,  # Remitente (cambia esto)
                [destinatario],  # Destinatario
                fail_silently=False,
            )
            return render(request, 'email_exitoso.html')  # Redirige a la página de éxito
        except Exception as e:
            # Manejo de errores (puedes personalizar esto)
            return render(request, 'email_fallido.html')  # Redirige a la página de error

    return render(request, 'consulta_artista.html', {'artista': artista, 'obra': obra})




#Envio Exitoso
#Creamos la vista de Inicio
def email_exitoso(request):
    return render(request, 'email_exitoso.html')

#Email Fallido
def email_fallido(request):
    return render(request, 'email_fallido.html')


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

#Creamos la vista de Aviso de Registro
def aviso_registroArtista (request):
    return render(request,'aviso_registroArtista.html')


#Creamos la vista de contactos
def contactos(request):
    return render(request,'contactos.html')

def nuestros_servicios(request):
     return render(request, 'nuestros_servicios.html')

def sobre_nosotros(request):
    return render (request, 'sobre_nosotros.html')

def pagina_en_construccion(request):
    return render (request, 'pagina_en_construccion.html')


from django.core.files.uploadedfile import InMemoryUploadedFile
def formularioAltaArtista(request):
    
    if request.method == 'POST':
        # Obtengo los datos del formulario
        nombre_artista = request.POST['nombreArtista']
        apellido_artista = request.POST['apellidoArtista']
        nacionalidad_artista = request.POST['nacionalidadArtista']
        email_artista = request.POST['emailArtista']
        #tipo = request.POST['tipo']  # Obtener el tipo de usuario
        imagen = request.FILES.get('imagen')  # Obtener el archivo de imagen
        #Creo la instancia del modelo Artista y la guarda en BD
        
        artista = Artista(
                nombreArtista=nombre_artista,
                apellidoArtista=apellido_artista,
                nacionalidadArtista=nacionalidad_artista,
                emailArtista=email_artista,
                imagen = imagen # Asignar la imagen al campo 'imagen'
            )
        artista.save()
            
        #form = formularioAltaArtista(request.POST)
        return render(request, 'index.html')  # si todo salio bien envia a págian de inicio
    
    else:
        # es una solicitud GET, mostrar de nuevo el formulario
        #return render(request,'formularioAltaArtista.html')
        return render(request, 'formularioAltaArtista.html')


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



from django.contrib.auth.decorators import user_passes_test

# Define una función de prueba que verifica si el usuario tiene permiso para escribir en la BD
def tiene_permiso_escritura(user):
    return user.has_perm('permiso_personalizado')

#
def registro_exitoso_obra_arte(request):
    return render(request, 'registro_exitoso_obra_arte.html')


#--------------------------------------------------------------------------------------------------

from django.shortcuts import render
from .models import ObraArte

def formularioAltaObraArte1(request):
    artistas = Artista.objects.all()
    galerias = Galeria.objects.all()
    
     
    if request.method == 'POST':
        # Obtén los datos del formulario
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        autor_id = request.POST['autor']
        precio = request.POST['precio']
        fecha_creacion = request.POST['fechaCreacion']
        vendido = request.POST.get('vendido', False)
        imagen = request.FILES['imagen']

        # Crea la instancia de ObraArte
        obra_arte = ObraArte(
            titulo=titulo,
            descripcion=descripcion,
            autor_id=autor_id,
            precio=precio,
            fechaCreacion=fecha_creacion,
            vendido=vendido,
            imagen=imagen,
        )
        obra_arte.save()
        
        # Asocia la obra de arte a la galería seleccionada
        galeria_id = request.POST['galeria']
        if galeria_id:
            galeria = Galeria.objects.get(id=galeria_id)
            galeria.obras.add(obra_arte)



        # Puedes mostrar un mensaje de éxito si lo deseas
        return render(request, 'registro_exitoso_obra_arte.html')

    else:
        # Es una solicitud GET, muestra el formulario de alta de ObraArte
        # Debes proporcionar una lista de artistas disponibles para seleccionar el autor
        # Por ejemplo, artistas = Artista.objects.all()
        return render(request, 'formularioAltaObraArte1.html', {'artistas': artistas,'galerias': galerias})





#Creo funcion para dar de alta la obra.

from django.shortcuts import render, redirect
from .models import ObraArte, Galeria
from .forms import ObraArteForm

def formularioAltaObraArte(request):
    artistas = Artista.objects.all() 
    galerias = Galeria.objects.all()
    obra_guardada = False  # Variable para indicar si la obra se guardó con éxito
    
    if request.method == 'POST':
        form = ObraArteForm(request.POST, request.FILES)
        if form.is_valid():
            obra_arte = form.save()
            
            # Si deseas asociar la obra de arte a una galería, puedes hacerlo aquí
            galeria_id = request.POST.get('galeria', None)
            if galeria_id:
                galeria = Galeria.objects.get(pk=galeria_id)
                obra_arte.galeria = galeria
                obra_arte.save()
                
                
            return render(request, 'registro_exitoso_obra_arte.html')  # Redirige a donde quieras después de guardar
        else:
            print(form.errors)  # Imprime los errores de validación en la consola para depuración
    else:
        form = ObraArteForm()
    
    return render(request, 'formularioAltaObraArte.html', {'form': form, 'galerias': galerias, 'obra_guardada': obra_guardada,'artistas': artistas})

    

# Creo la funcion para dar de alta las galerías


# Vista para el formulario de alta de galería
def formularioAltaGaleria(request):
    # Obtén la lista de obras de arte disponibles para asociar a la galería
    obras_de_arte = ObraArte.objects.all()

    if request.method == 'POST':
       
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha_creacion = request.POST['fechaCreacion']
        obras_seleccionadas = request.POST.getlist('obras')
        
        imagen = request.FILES.get('imagen')

        # Crea la instancia de Galeria
        galeria = Galeria(
            nombre=nombre,
            descripcion=descripcion,
            fechaCreacion=fecha_creacion,
            imagen = imagen,
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

def lista_artistas(request):
    artistas = Artista.objects.all()
    artista_seleccionado = None

    # Verificar si se ha seleccionado un artista específico en la solicitud GET
    artista_id = request.GET.get('artista_id')
    if artista_id:
        try:
            artista_seleccionado = Artista.objects.get(id=artista_id)
        except Artista.DoesNotExist:
            pass

    return render(request, 'artistas.html', {
        'artistas': artistas,
        'artista_seleccionado': artista_seleccionado,
    })



#Listado de Galerias

def lista_galerias(request):
    galerias = Galeria.objects.all()
    
    # Crear una lista de diccionarios para almacenar obras, artistas, imágenes y descripciones de cada galería
    galerias_info = []
    
    for galeria in galerias:
        obras = galeria.obras.all()
        obras_info = [{'nombre_obra': obra.titulo, 'nombre_artista': obra.autor.nombreArtista} for obra in obras]
        
        # Obtén la URL de la imagen de la galería o una imagen por defecto si no hay imagen
        if galeria.imagen:
            imagen_galeria_url = galeria.imagen.url
        else:
            imagen_galeria_url = '{% static "images/pinceles-paleta.jpg" %}'  # Coloca aquí la URL de la imagen estática por defecto
        
        galeria_info = {
            'id_galeria': galeria.pk,
            'nombre_galeria': galeria.nombre,
            'obras_info': obras_info,
            'imagen_galeria': imagen_galeria_url,  # Agrega la URL de la imagen de la galería
            'descripcion_galeria': galeria.descripcion  # Agrega la descripción de la galería
        }
        
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

#def lista_obras_galeria(request, galeria_id):
    #print("Valor de galeria_id:", galeria_id)  # Imprime 
#    galeria = get_object_or_404(Galeria, pk=galeria_id)
#    obras = galeria.obras.all()
#    return render(request, 'lista_obras_galeria.html', {'obras': obras})


###--------------------------------------------------------------------------------------------------


def lista_obras_galeria(request, galeria_id):
    print("Valor de galeria_id:", galeria_id)  # Imprime el ID de la galería
    galeria = get_object_or_404(Galeria, pk=galeria_id)
    obras = galeria.obras.all()
    print("Número de obras recuperadas:", len(obras))  # Imprime el número de obras
    return render(request, 'lista_obras_galeria.html', {'obras': obras})





def detalle_obra(request, obra_id):
    obra = get_object_or_404(ObraArte, pk=obra_id)
    
    # Obtener el artista_id de la obra
    artista_id = obra.autor.id
    
    # Generar la URL inversa para 'obras_por_artista' con el artista_id
    previous_url = reverse('obras_por_artista', kwargs={'artista_id': artista_id})
    
    return render(request, 'detalle_obra.html', {'obra': obra, 'previous_url': previous_url})


def detalle_obra_galeria(request, obra_id):
    obra = get_object_or_404(ObraArte, pk=obra_id)
    
    # Obtener la galería de la obra (si existe) a través del conjunto relacionado 'galeria'
    galeria = obra.galeria
    
    # Recuperar todas las obras que pertenecen a la misma galería que la obra actual
    obras_galeria = ObraArte.objects.filter(galeria=galeria)
    
    # Generar la URL inversa para 'lista_obras_galeria' con el galeria_id
    previous_url = reverse('lista_obras_galeria', kwargs={'galeria_id': galeria.id if galeria else None})
    
    return render(request, 'detalle_obra_galeria.html', {'galeria': galeria, 'obra': obra, 'obras_galeria': obras_galeria, 'previous_url': previous_url})


#Consulta Artista
def consulta_artista(request):
    artista_id = request.GET.get('artista_id')
    obra_id = request.GET.get('obra_id')
    
    artista = get_object_or_404(Artista, pk=artista_id)
    obra = get_object_or_404(ObraArte, pk=obra_id) if obra_id else None
    
    return render(request, 'consulta_artista.html', {'artista': artista, 'obra': obra})


def accion_consulta(request, artista_id, obra_id):
    # Redirigir al usuario al formulario de consulta
    return redirect('consulta_artista')


def obras_por_artista(request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    obras = ObraArte.objects.filter(autor=artista)
    
    if obras:
        return render(request, 'obras_por_artista.html', {'artista': artista, 'obras': obras})
    else:
        mensaje = f"{artista.nombreArtista} {artista.apellidoArtista} no ha registrado ninguna obra."
        return render(request, 'sin_obras.html', {'mensaje': mensaje})

#login Artista

def login_view (request):
    
    if request.method == 'POST':
        
        miFormulario = AuthenticationForm (request, data=request.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username=usuario,password=psw)
            
            if user:
                
                login(request,user)
                return render (request,'registrarse.html',{"mensaje": f'Bienvenido {usuario}' })
            
          
        return render (request,'registrarse.html',{"mensaje": f'Datos incorrectos!!!'})
    
    else:
        miFormulario = AuthenticationForm(request)          
        return render(request, 'login.html', {"miFormulario": miFormulario})

#Registro de usuarios
def register(request):
    
    if request.method == 'POST':
            
            miFormulario = UserCreationForm (request.POST)
            
            if miFormulario.is_valid():
                
                data = miFormulario.cleaned_data
                usuario = data["username"]
                miFormulario.save()
                return render (request,'registrarse.html',{"mensaje": f'Usuario {usuario} creado con exito!!!!' })
            
               
            return render (request,'registrarse.html',{"mensaje": f'Formulario Inválido' })
    else:
        miFormulario = UserCreationForm()          
        return render(request, 'alta_usuario.html', {"miFormulario": miFormulario})