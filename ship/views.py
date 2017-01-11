from django.views import generic
from .models import Department, SingleRecord


class IndexView(generic.ListView):
        template_name = 'ship/index.html'
        context_object_name = 'all_records'

        def get_queryset(self):
                return SingleRecord.objects.all()


class DepartmentView(generic.ListView):
        template_name = 'ship/departments.html'
        context_object_name = 'all_departments'

        def get_queryset(self):
                return Department.objects.all()


class DetailView(generic.DetailView):
    model = Department
    template_name = 'ship/detail.html'


class RecordsView(generic.ListView):
    template_name = 'ship/records.html'
    context_object_name='all_records'
    def get_queryset(self):
        return SingleRecord.objects.all()









# from django.http import Http404
# from django.shortcuts import render, get_object_or_404
# from .models import Department, Soldier, SingleRecord
#
#
# def index(request):
#     all_departments = Department.objects.all()
#     all_records = SingleRecord.objects.all()
#     return render(request, 'ship/index.html', {'all_departments': all_departments, 'all_records': all_records})
#
#
# def detail(request, department_id):
#     department = get_object_or_404(Department, pk=department_id)
#     return render(request, 'ship/detail.html', {'department': department, })


# def baknaz_team(request, department_id):
#     department = get_object_or_404(Department, pk=department_id)
#     try:
#         selected_soldier = department.soldier_set.get(pk=request.POST['soldier'])
#     except(KeyError, Soldier.DoesNotExist):
#         return render(request, 'ship/detail.html',
#                       {'department': department, 'error_message': "You did not select a valid soldier"})
#     else:
#         selected_soldier.is_baknaz_team = True
#         selected_soldier.save()
#         return render(request, 'ship/detail.html', {'department': department, })

