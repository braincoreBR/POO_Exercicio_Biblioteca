from django.db import models

# Create your models here.

class TipoCurso(models.TextChoices):
    CONTINUO = "Continuo"
    PONTUAL = "Pontual"
    

class Cursos(models.Model):
    nmCurso = models.CharField(max_length=100)
    tpCurso = models.CharField(max_length=10, choices=TipoCurso, blank=False, null=False)
    dtInicio = models.DateTimeField()
    descricao= models.TextField(max_length=100, null=True)

    def __str__(self) :
        return f'{self.nmCurso}: {self.tpCurso} - {self.carga_horaria} '
    
    class Meta:
        verbose_name= 'Cadastro de curso'
        verbose_name_plural='Cadastros de cursos'
        ordering = ['-dtInicio']


class Aluno(models.Model):
    Sexo = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'N/A')
    )
    nomeAluno = models.CharField(max_length=100, null=False)
    dataNascimento = models.DateTimeField(null=False)
    sexo = models.CharField(max_length=1, choices=Sexo, blank=False, null=False, default='F')
    cpfAluno = models.IntegerField()
    emailAluno = models.CharField(max_length=100, null=False)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    celularAluno = models.IntegerField()
    endereco = models.CharField(max_length=200)
    respFinanceiro = models.BooleanField(default=True)
    respPedagogico = models.BooleanField(default=True)
    

    def __str__(self) :
        return f'{self.nomeAluno}[{self.emailAluno}]'
    class Meta:
        verbose_name ='Formulário de Aluno'
        verbose_name_plural ='Formulários de Aluno'
        ordering = ['-dataCadastro']


class Responsavel(models.Model):
    Parentesco = (
        ('M', 'Mãe'),
        ('P', 'Pai'),
        ('I', 'Irmã(o)'),
        ('A', 'Avós'),
        ('O', 'Outros')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tpParente = models.CharField(max_length=1, choices=Parentesco, blank=False, null=False, default='M')
    nome = models.CharField(max_length=100, null=False)
    dataNascimento = models.DateTimeField()
    cpfParen = models.IntegerField()
    emailParen = models.CharField(max_length=100, null=False)
    dataCadastro = models.DateTimeField(auto_now_add=True)
    celularParen = models.IntegerField()
    endereco = models.CharField(max_length=200)
    respFinanceiro = models.BooleanField(default=True)
    respPedagogico = models.BooleanField(default=True)
    

    def __str__(self) :
        return f'{self.aluno}[{self.nome}]'
    class Meta:
        verbose_name ='Formulário de Responsável'
        verbose_name_plural ='Formulários de Responsável'
        ordering = ['-dataCadastro']