import datetime
from app.models import SalaryPaid, Employee
from rocketdata.celery import app


@app.task
def delete_user(list_user_id):
    SalaryPaid.objects.filter(emploee__id__in=list_user_id).delete()

@app.task
def set_salary():
    for user in Employee.objects.all().only('salary'):
        SalaryPaid.objects.create(
            emploee=user,
            date_paid=datetime.datetime.now(),
            sum_paid=user.salary
        )