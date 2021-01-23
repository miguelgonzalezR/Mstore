from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class usuman(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo')

        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombres,apellidos, password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario



class usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=50)
    email = models.EmailField('Correo electronico', max_length=60, unique=True)
    nombres = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    is_active = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=True) #default=False
    objects = usuman()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
    
