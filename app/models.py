from django.db import models
from django.db.models import Sum
from rest_framework_simplejwt.state import User


class Position_relations(models.Model):
    '''Cвязь начальник и подчинённый'''
    position = models.CharField(max_length=255, unique=True, verbose_name='Должность')
    level = models.SmallIntegerField(verbose_name='Уровень должности')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if Position_relations.objects.all().count() < 5:
            super().save()
        else:
            raise Exception('Превышение количества записей!')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность и её уровень'
        verbose_name_plural = 'Должность и её уровень'


class Employes(models.Model):
    '''Модель работников'''
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    position = models.ForeignKey(Position_relations, on_delete=models.CASCADE,
                              verbose_name='Должность')
    chief = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    date_employ = models.DateField(auto_now=True, verbose_name='Дата приёма на работу')
    salary = models.DecimalField(max_digits=12 ,decimal_places=2, verbose_name='Заработная плата')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def salary_all(self):
        return self.salary_paid_set.filter(emploee=self)\
                                   .only('sum_paid')\
                                   .aggregate(Sum('sum_paid'))['sum_paid__sum']
    salary_all.short_description = 'Всего выплачено'

    def salary_info(self):
        return self.salary_paid_set.all()

    def __str__(self):
        return f"{self.pk} {self.first_name} {self.last_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'


class Salary_paid(models.Model):
    '''Данные по выплате заработной платы'''
    emploee = models.ForeignKey(Employes, verbose_name='Работник', on_delete=models.CASCADE)
    date_paid = models.DateField(verbose_name='Дата выплаты')
    sum_paid = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Сумма выплаты',)

    def __str__(self):
        return f"{self.emploee} {self.date_paid} {self.sum_paid}"

    class Meta:
        verbose_name = 'Заработная плата'
        verbose_name_plural = 'Заработная плата'