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


class DadosSaresp(models.Model):
    id_reg = models.AutoField(primary_key=True)
    cd_aluno = models.BigIntegerField(blank=True, null=True)
    ano_saresp = models.IntegerField(blank=True, null=True)
    nome_dep = models.CharField(max_length=12, blank=True, null=True)
    mun = models.CharField(max_length=15, blank=True, null=True)
    codesc = models.BigIntegerField(blank=True, null=True)
    escola = models.CharField(max_length=255, blank=True, null=True)
    tipo_classe = models.IntegerField(blank=True, null=True)
    serie_ano = models.CharField(max_length=255, blank=True, null=True)
    classe = models.BigIntegerField(blank=True, null=True)
    tp_sexo = models.CharField(max_length=1, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    periodo = models.CharField(max_length=5, blank=True, null=True)
    nec_esp_1 = models.CharField(max_length=255, blank=True, null=True)
    nec_esp_2 = models.CharField(max_length=255, blank=True, null=True)
    nec_esp_3 = models.CharField(max_length=255, blank=True, null=True)
    nec_esp_4 = models.CharField(max_length=255, blank=True, null=True)
    nec_esp_5 = models.CharField(max_length=255, blank=True, null=True)
    tip_prova = models.CharField(max_length=1, blank=True, null=True)
    tem_nec = models.IntegerField(blank=True, null=True)
    cad_prov_lp = models.IntegerField(blank=True, null=True)
    cad_prov_mat = models.IntegerField(blank=True, null=True)
    cad_prov_cie = models.IntegerField(blank=True, null=True)
    particip_lp = models.IntegerField(blank=True, null=True)
    particip_mat = models.IntegerField(blank=True, null=True)
    particip_cie = models.IntegerField(blank=True, null=True)
    total_ponto_lp = models.IntegerField(blank=True, null=True)
    total_ponto_mat = models.IntegerField(blank=True, null=True)
    total_ponto_cie = models.IntegerField(blank=True, null=True)
    porc_cert_lp = models.FloatField(blank=True, null=True)
    porc_cert_mat = models.FloatField(blank=True, null=True)
    porc_cert_cie = models.FloatField(blank=True, null=True)
    profic_lp = models.FloatField(blank=True, null=True)
    profic_mat = models.FloatField(blank=True, null=True)
    profic_cie = models.FloatField(blank=True, null=True)
    nivel_profic_lp = models.CharField(max_length=16, blank=True, null=True)
    nivel_profic_mat = models.CharField(max_length=16, blank=True, null=True)
    nivel_profic_cie = models.CharField(max_length=16, blank=True, null=True)
    classific_lp = models.CharField(max_length=12, blank=True, null=True)
    classific_mat = models.CharField(max_length=12, blank=True, null=True)
    classific_cie = models.CharField(max_length=12, blank=True, null=True)
    validade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dados_saresp'


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
