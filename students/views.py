from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list')
