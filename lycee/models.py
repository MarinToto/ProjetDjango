from django.db import models
from django import forms

# Create your models here.
class Cursus(models.Model):
  name = models.CharField(
    max_length=50,
    blank=False,
    null=True,
    default='aucun'
  )
  year_from_bac = models.SmallIntegerField(
    help_text ="year since le bac",
    verbose_name="year",
    blank=False,
    null=True,
    default=0
  )
  scholar_year = models.CharField(
    max_length=9,
    blank=False,
    null=True,
    default='0000-00001'
  )
  def __str__(self):
    return self.name + " " + self.scholar_year

class Student(models.Model):
  first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False
    )
  birth_date = models.DateField(
    verbose_name='date of birth',
    blank=False,
    null=True
    )
  last_name = models.CharField(
    verbose_name="last name",
    help_text="last name of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="???",
    max_length=255, # taille maximale du champ
    )
  phone = models.CharField(
    verbose_name="phone number",
    help_text="phone number of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="0999999999",
    max_length=10, # taille maximale du champ
    )
  email = models.EmailField(
    verbose_name="email",
    help_text="phone number of the student",
    blank=False, # pas de champ vide
    null=False, # pas de champ null (a conjuguer avec default
    default="x@y.z",
    max_length=255, # taille maximale du champ
    )
  comments = models.CharField(
    verbose_name="comments",
    help_text="some comments about the student",
    blank=True,
    null=False, # pas de champ null (a conjuguer avec default
    default="",
    max_length=255, # taille maximale du champ
    )
  cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE, # necessaire selon la version de Django
    null=True
    )
  def __str__(self):
    return self.first_name + " " + self.last_name + " (" + self.email + ")"

class Presence(models.Model):
  student = models.ForeignKey(
    Student,
    on_delete=models.CASCADE,
    null=False
  )
  date = models.CharField(
    verbose_name="Date",
    help_text="No date",
    blank=False,
    null=True,
    max_length=255, 
  )
  isMissing = models.BooleanField(
    verbose_name = "Absent"
  )
  reason = models.CharField(
    verbose_name="Excuse",
    help_text="No excuse",
    blank=True,
    null=False,
    max_length=255
  )
  
  