import datetime
from app.models import Salary_paid, Employes
from rocketdata.celery import app


@app.task
def delete_user(list_user_id):
    Salary_paid.objects.filter(emploee__id__in=list_user_id).delete()

@app.task
def set_salary():
    for user in Employes.objects.all().only('salary'):
        Salary_paid.objects.create(
            emploee=user,
            date_paid=datetime.datetime.now(),
            sum_paid=user.salary
        )