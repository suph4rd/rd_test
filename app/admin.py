from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from app.models import Position_relations, Employes, Salary_paid
from app.tasks import delete_user


def delete_records(modeladmin, request, queryset):
    '''action на удаление информации о заработной плате всех выбраных сотрудников'''
    if queryset.count() > 20:
        list_user_id = []
        for user in queryset:
            list_user_id.append(user.id)
        delete_user.delay(list_user_id)
    else:
        Salary_paid.objects.filter(emploee__in=queryset).delete()
delete_records.short_description = "Удалить информацию о заработной плате выбраных сотрудников"


@admin.register(Employes)
class Emploees_admin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('first_name', 'last_name', 'middle_name', 'position',
                    'get_chief', 'salary', 'salary_all')
    list_filter = ('position','position__level')
    actions = [delete_records]

    def get_chief(self, obj):
        chief = str(obj.chief)
        return mark_safe('<a href="{0}">{1}</a>'.format(chief.split()[0], chief))
    get_chief.short_description = _("Начальник")


@admin.register(Salary_paid)
class Salary_paid_admin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('emploee', 'date_paid', 'sum_paid')


@admin.register(Position_relations)
class Position_relations_admin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('position', 'level')