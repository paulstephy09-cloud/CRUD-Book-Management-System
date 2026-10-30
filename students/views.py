from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# Read - Display students
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


# Create - Add student
def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add_student.html', {'form': form})


# Update - Edit student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'update_student.html', {'form': form})


# Delete - Remove student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'delete_student.html', {'student': student})
