import datetime
from app.models import Salary_paid, Employes
from test_rocketdata.celery import app


@app.task
def delete_user(id):
        Salary_paid.objects.filter(emploee__id=id).delete()

@app.task
def set_salary():
    for user in Employes.objects.all().only('salary'):
        Salary_paid.objects.create(
            emploee=user,
            date_paid=datetime.datetime.now(),
            sum_paid=user.salary
        )