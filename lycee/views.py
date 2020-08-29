from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm, PresenceForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

def index (request):
  result_list = Cursus.objects.order_by('name')

  context = { 'liste' : result_list}
 
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  student_list = Student.objects.filter(cursus=cursus_id)

  context = {'student_list' : student_list}

  return render (request, 'lycee/student/student_list.html', context)

def detail_student(request,student_id):

    result_list = get_object_or_404(Student, pk=student_id)

    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

def call_of_roll(request,cursus_id):
  
  result_list = Student.objects.filter(cursus=cursus_id)
  if request.method=="POST":
    date = request.POST.get("calendar")
    for student in result_list :
      missing=request.POST.get("student"+str(student.id))
      call_of = Presence()
      call_of.date=date
      call_of.student=student
      if missing=="on" : 
        call_of.isMissing=True 
      else :
        call_of.isMissing=False
      call_of.save()
    context = {'liste': result_list,}
    return render (request, 'lycee/call_of_roll.html' , context)
  else : 
    context = {'liste': result_list,}
    return render (request, 'lycee/call_of_roll.html' , context)
  
class StudentCreateView(CreateView):
  model = Student
  form_class = StudentForm
 
  template_name = "lycee/student/create.html"
  
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentUpdateView(UpdateView):
  model = Student
  form_class = StudentForm
  template_name = "lycee/student/student_edit.html"

  template_name_suffix = '_edit'

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class ParticularCorView(CreateView):
  model = Presence
  form_class = PresenceForm
 
  template_name = "lycee/particular_cor.html"
  
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))
