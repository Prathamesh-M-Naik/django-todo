from django.shortcuts import render, redirect
from .models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        Task.objects.create(
            title=title,
            description=description
        )

    return redirect("home")


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = not task.completed
    task.save()

    return redirect("home")


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect("home")
