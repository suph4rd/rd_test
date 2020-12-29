from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from app.models import PositionRelations, SalaryPaid, Employee
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
    list_select_related = True
    list_display = ('first_name', 'last_name', 'middle_name', 'position',
                    'get_chief', 'salary', 'salary_all')
    list_filter = ('position','position__level')
    actions = [delete_records]

    def get_chief(self, obj):
        chief = str(obj.chief)
        return mark_safe('<a href="{0}">{1}</a>'.format(chief.split()[0], chief))
    get_chief.short_description = _("Начальник")


@admin.register(SalaryPaid)
class SalaryPaidAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('employee', 'date_paid', 'sum_paid')


@admin.register(PositionRelations)
class PositionRelationsAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('position', 'level')