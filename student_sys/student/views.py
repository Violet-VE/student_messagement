#########################################
# 作者：小纯洁				#
# 时间：2019.6.8			#
#########################################
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Create your views here.

from .models import Student
from .forms import StudentForm


class IndexView(View):
    # Class-based view:
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)

    # 流水式代码：
    # def index(request):
    #   students = Student.get_all()
    #   if request.method == 'POST':
    #       form = StudentForm(request.POST)
    #       if form.is_valid():
    #           form.save()
    #           return HttpResponseRedirect(reverse('index'))
    #   else:
    #       form = StudentForm()
    #   context = {
    #       'students': students,
    #       'form': form,
    #   }
    #   return render(request, 'index.html', context=context)

    # students = Student.objects.all()
    # return render(request, 'index.html', context={'students': students})
    # words = 'World!'
    # return render(request, 'index.html', context={'words': words})

    # 手动构建Form
    # students = Student.objects.all()
    # if request.method == 'POST':
    #     form = StudentForm(request.POST)
    #     if (form.is_valid()):
    #         cleaded_data = form.cleaned_data
    #         student = Student()
    #         student.name = cleaded_data['name']
    #         student.name = cleaded_data['sex']
    #         student.name = cleaded_data['profession']
    #         student.name = cleaded_data['email']
    #         student.name = cleaded_data['qq']
    #         student.name = cleaded_data['phone']
    #         student.save()
    #         return HttpResponseRedirect(reverse('index'))
    # else:
    #     form = StudentForm()
    # context = {
    #     'students': students,
    #     'form': form,
    # }
    # return render(request, 'index.html', context=context)
