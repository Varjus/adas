from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.cd_aluno
    class Meta:
        managed = True
        db_table = 'dados_saresp'