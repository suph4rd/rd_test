from django.db import models
from django.db.models import Sum, CheckConstraint, Q
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from rest_framework_simplejwt.state import User


class PositionRelations(models.Model):
    '''Cвязь начальник и подчинённый'''
    position = models.CharField(max_length=255, unique=True, verbose_name='Должность')
    level = models.SmallIntegerField(verbose_name='Уровень должности')

    def __str__(self):
        return self.position

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(level__lt=6),
                name="amount_levels"
            )
        ]
        verbose_name = 'Должность и её уровень'
        verbose_name_plural = 'Должность и её уровень'


class Employee(models.Model):
    '''Модель работников'''
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    position = models.ForeignKey(PositionRelations, on_delete=models.CASCADE,
                              verbose_name='Должность')
    chief = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    date_employ = models.DateField(auto_now=True, verbose_name='Дата приёма на работу')
    salary = models.DecimalField(max_digits=12 ,decimal_places=2, verbose_name='Заработная плата')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def salary_all(self):
        return '%s' % (self.salarypaid_set.filter(employee=self)\
                                   .only('sum_paid')\
                                   .aggregate(Sum('sum_paid'))['sum_paid__sum'])
    salary_all.short_description = 'Всего выплачено'

    def salary_info(self):
        return self.salarypaid_set.all()

    def get_chief_id(self):
        return mark_safe('<a href="{0}">{1}</a>'.format(self.chief_id, "Начальник"))
    get_chief_id.short_description = _("Объект начальника")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'


class SalaryPaid(models.Model):
    '''Данные по выплате заработной платы'''
    employee = models.ForeignKey(Employee, verbose_name='Работник', on_delete=models.CASCADE)
    date_paid = models.DateField(verbose_name='Дата выплаты')
    sum_paid = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма выплаты',)

    def __str__(self):
        return f"{self.employee} {self.date_paid} {self.sum_paid}"

    class Meta:
        verbose_name = 'Заработная плата'
        verbose_name_plural = 'Заработная плата'