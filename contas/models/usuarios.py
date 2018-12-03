from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.shortcuts import reverse
from datetime import date

PERFIS = (
    ('C', 'Coordenador'),
    ('P', 'Professor'),
    ('A', 'Aluno'),
)

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('O nome de login é obrigatório')
        login = self.model.normalize_username(login)
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, password=None, **extra_fields):
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        from contas.models import Coordenador
        self.model = Coordenador
        extra_fields.setdefault('tipo', 'C')
        extra_fields.setdefault('nome', login)
        extra_fields.setdefault('celular', login)
        extra_fields.setdefault('email', login)
        return self._create_user(login, password, **extra_fields)

# Create your models here.
class Usuario(AbstractBaseUser):

    login = models.CharField(max_length=100, unique=True)
    password = models.CharField("Senha", max_length=128, db_column="senha")
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1), blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=PERFIS)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    @property
    def is_staff(self):
        return self.tipo == 'C'

    @property
    def perfil(self):
        if self.tipo == 'A':
            return self.aluno
        elif self.tipo == 'P':
            return self.professor
        else:
            return self.coordenador

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return self.perfil.get_absolute_url()
