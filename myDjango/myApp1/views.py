from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy

from .forms import CreateUserForm
from .models import Worker


def index_view(request):
    # region work with db
    # Worker.objects.get(id=5).delete()
    # worker_to_change = Worker.objects.get(id=5)
    # worker_to_change.surname = 'Пятых'
    # worker_to_change.save()
    # Worker.objects.filter(id=5).update(name='Альберт')

    # new_worker = Worker(name='Эдуард', surname='Третьих', salary=50000)
    # new_worker.save()
    # Worker.objects.create(name='Эдуард', surname='Третьих', salary=50000)

    # all_workers = Worker.objects.all()
    # for i in all_workers:
    #     print(f'ID: {i.id}\n Name: {i.name}\n Surname: {i.surname}\n')
    # print(all_workers)

    # workers_filtered = Worker.objects.filter(salary=60000)
    # print(workers_filtered)
    # endregion

    all_workers = Worker.objects.all()
    return render(request, 'index.html', context={'data': all_workers})


@login_required
def profile_view(request):
    return render(request, 'web/profile.html')


def register_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('profile')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


class WebPasswordResetView(PasswordResetView):
    template_name = 'web/password_reset_email.html'
    success_url = reverse_lazy("profile")


class WebPasswordChangeView(PasswordChangeView):
    template_name = 'web/password_change.html'
    success_url = reverse_lazy("profile")
