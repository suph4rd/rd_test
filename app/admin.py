from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from app.models import Position_relations, Employes, Salary_paid


def delete_records(modeladmin, request, queryset):
    '''action на удаление информации о заработной плате всех выбраных сотрудников'''
    for user in queryset:
        Salary_paid.objects.filter(emploee=user).delete()
delete_records.short_description = "Удалить информацию о заработной плате выбраных сотрудников"


@admin.register(Employes)
class Emploees_admin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('first_name', 'last_name', 'middle_name', 'position',
                    'chief', 'salary', 'salary_all')
    list_filter = ('position','position__level')
    actions = [delete_records]

    def chief(self, obj):
        '''Ссылка на объект начальника'''
        id = Employes.objects.get(position=obj.position.chief).id
        chief = Employes.objects.get(position=obj.position.chief).position
        return mark_safe('<a href="{0}">{1}</a>'.format(id, chief))

    chief.short_description = _("Начальник")


@admin.register(Salary_paid)
class Salary_paid_admin(admin.ModelAdmin):
    list_display = ('emploee', 'date_paid', 'sum_paid')


@admin.register(Position_relations)
class Position_relations_admin(admin.ModelAdmin):
    list_display = ('position', 'chief', 'level')


