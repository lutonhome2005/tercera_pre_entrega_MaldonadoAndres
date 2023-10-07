from django.db import models

# Create your models here.
class Galeria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fechaCreacion = models.DateField()
    obras = models.ManyToManyField('ObraArte', related_name='galerias', blank=True)
    imagen = models.ImageField(upload_to='galerias/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
        
class Usuario (models.Model):
    nombreUsuario = models.CharField(max_length=50)
    apellidoUsuario = models.CharField(max_length= 60)
    edadUsuario = models.IntegerField()
    emailUsuario = models.EmailField(unique=True)
    carrito = models.OneToOneField('Carrito', on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.nombreUsuario

class Artista (models.Model):
    nombreArtista = models.CharField(max_length=50)
    apellidoArtista = models.CharField(max_length= 60)
    nacionalidadArtista = models.CharField(max_length=50)
    emailArtista = models.EmailField(unique=True)
    imagen = models.ImageField(upload_to='artistas/', null=True, blank=True)

    def __str__(self):
        return f' {self.nombreArtista} - {self.apellidoArtista}'
    
class ObraArte(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    autor = models.ForeignKey('Artista', on_delete=models.CASCADE, related_name='obras')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField()
    fechaCreacion = models.DateField()
    vendido = models.BooleanField(default=False)
    # Relación ForeignKey a Galeria
    # Una ObraArte pertenece a una Galeria
    galeria = models.ForeignKey(Galeria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Autor: {self.autor} Título: {self.titulo}'

class Carrito(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='carritos')
    obras = models.ManyToManyField(ObraArte)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Carrito de {self.comprador.nombreUsuario}"
    
    