from django.contrib import admin
from app.models import PositionLevel, SalaryPaid, Employee
from app.tasks import delete_user


def delete_records(modeladmin, request, queryset):
    '''action for delete information about salary of all selected employees'''
    if queryset.count() > 20:
        list_user_id = list(queryset.values_list('id', flat=True))
        delete_user.delay(list_user_id)
    else:
        SalaryPaid.objects.filter(employee__in=queryset).delete()


delete_records.short_description = "Удалить информацию о заработной плате выбраных сотрудников"


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'position',
                    'get_chief_id', 'salary', 'salary_all')
    list_filter = ('position', 'position__level')
    actions = [delete_records]


@admin.register(SalaryPaid)
class SalaryPaidAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('employee', 'date_paid', 'sum_paid')


@admin.register(PositionLevel)
class PositionRelationsAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('position', 'level')
