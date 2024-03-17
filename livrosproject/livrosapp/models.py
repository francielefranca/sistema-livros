# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Autor(models.Model):
    idautor = models.IntegerField(primary_key=True)
    nomeautor = models.CharField(max_length=150, blank=True, null=True)
    sexoautor = models.CharField(max_length=45, blank=True, null=True)
    idgeneroaut = models.ForeignKey('Genero', models.DO_NOTHING, db_column='idgeneroaut', blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    idgeneroautor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Avaliacao(models.Model):
    idavaliacao = models.IntegerField(primary_key=True)
    comentarioav = models.TextField(blank=True, null=True)
    notaav = models.IntegerField(blank=True, null=True)
    idlivroav = models.ForeignKey('Livros', models.DO_NOTHING, db_column='idlivroav', blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    nota = models.IntegerField(blank=True, null=True)
    idlivro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avaliacao'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Editora(models.Model):
    ideditora = models.IntegerField(primary_key=True)
    nome = models.CharField(unique=True, max_length=150, blank=True, null=True)
    cnpj = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editora'


class Genero(models.Model):
    idgenero = models.IntegerField(primary_key=True)
    nome = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'genero'


class Grupo(models.Model):
    idgrupo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    qtnpessoa = models.IntegerField(blank=True, null=True)
    idgenerogrupo = models.ForeignKey(Genero, models.DO_NOTHING, db_column='idgenerogrupo', blank=True, null=True)
    idautorgrupo = models.ForeignKey(Autor, models.DO_NOTHING, db_column='idautorgrupo', blank=True, null=True)
    nomegrupo = models.CharField(max_length=150, blank=True, null=True)
    qtnpessoas = models.IntegerField(blank=True, null=True)
    idgenero = models.IntegerField(blank=True, null=True)
    idautor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class Livros(models.Model):
    idlivros = models.IntegerField(primary_key=True)
    titulolivro = models.CharField(max_length=150)
    qtnpaginaslivro = models.IntegerField(blank=True, null=True)
    datapublicacaolivro = models.DateField(blank=True, null=True)
    idgenerolivro = models.ForeignKey(Genero, models.DO_NOTHING, db_column='idgenerolivro', blank=True, null=True)
    idautorlivro = models.ForeignKey(Autor, models.DO_NOTHING, db_column='idautorlivro', blank=True, null=True)
    ideditoralivro = models.ForeignKey(Editora, models.DO_NOTHING, db_column='ideditoralivro', blank=True, null=True)
    titulo = models.CharField(unique=True, max_length=150, blank=True, null=True)
    qtnpaginas = models.IntegerField(blank=True, null=True)
    datapublicacao = models.DateField(blank=True, null=True)
    idgenero = models.IntegerField(blank=True, null=True)
    idautor = models.IntegerField(blank=True, null=True)
    ideditora = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'livros'


class Participantes(models.Model):
    idparticipantes = models.IntegerField(primary_key=True)
    idgrupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='idgrupo', blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participantes'


class Publicacao(models.Model):
    idpublicacao = models.IntegerField(primary_key=True)
    idlivro = models.ForeignKey(Livros, models.DO_NOTHING, db_column='idlivro', blank=True, null=True)
    ideditora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='ideditora', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacao'


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, null=True)
    apelido = models.CharField(max_length=150, blank=True, null=True)
    leituras = models.TextField(blank=True, null=True)
    lider = models.IntegerField(blank=True, null=True)
    idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='idgenero', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'usuario'
