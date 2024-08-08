from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    aluno = models.ManyToManyField(Aluno, blank=True,null=True)

    def __str__(self):
        return self.nome



