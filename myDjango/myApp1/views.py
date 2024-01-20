from django.shortcuts import render
from myApp1.models import Worker


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

def profile_view(request):
    return render(request, 'web/profile.html')
