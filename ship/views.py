from django.shortcuts import render, get_object_or_404
from .models import Department, Soldier, SingleRecord


def index(request):
    all_departments = Department.objects.all()
    all_records = SingleRecord.objects.all()
    all_soldiers = Soldier.objects.all()


    # for soldier in all_soldiers:
    #       last_records = SingleRecord.objects.filter('soldier.soldier_name').latest('time_stamp')

    last_record_soldier_1 = SingleRecord.objects.filter(tag_string='0xA4 0xD8 0xB8 0x62').latest('time_stamp')
    last_record_soldier_2 = SingleRecord.objects.filter(tag_string='0xC1 0xA6 0x52 0x26').latest('time_stamp')
    cic_counter = 0
    engine_counter = 0

    if last_record_soldier_1.compartment == 532:
        cic_counter = cic_counter + 1
    if last_record_soldier_1.compartment == 522:
        engine_counter = engine_counter + 1
    if last_record_soldier_2.compartment == 532:
        cic_counter = cic_counter + 1
    if last_record_soldier_2.compartment == 522:
        engine_counter = engine_counter + 1

    return render(request, 'ship/index.html',
                  {'all_departments': all_departments, 'all_records': all_records,
                   # 'last_records': last_records
                   'last_record_soldier_1': last_record_soldier_1,
                   'last_record_soldier_2': last_record_soldier_2,
                   'cic_counter': cic_counter,
                   'engine_counter': engine_counter
                   })


def departments(request):
    all_departments = Department.objects.all()
    return render(request, 'ship/departments.html', {'all_departments': all_departments})


def details(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'ship/detail.html', {'department': department, })


def records(request):
    all_records = SingleRecord.objects.all()
    return render(request, 'ship/records.html', {'all_records': all_records})




# from django.views import generic
# from .models import Department, SingleRecord
#
#
# class IndexView(generic.ListView):
#         template_name = 'ship/index.html'
#         context_object_name = 'all_records'
#
#         def get_queryset(self):
#                 return SingleRecord.objects.all()
#
#
# class DepartmentView(generic.ListView):
#         template_name = 'ship/departments.html'
#         context_object_name = 'all_departments'
#
#         def get_queryset(self):
#                 return Department.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Department
#     template_name = 'ship/detail.html'
#
#
# class RecordsView(generic.ListView):
#     template_name = 'ship/records.html'
#     context_object_name='all_records'
#     def get_queryset(self):
#         return SingleRecord.objects.all()



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

