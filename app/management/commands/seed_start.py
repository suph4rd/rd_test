from django.core.management.base import BaseCommand
import faker
from django.contrib.auth.models import User
from django_seed import Seed
from app.models import Employes, Salary_paid, Position_relations

class Command(BaseCommand):
    help = 'Activate seeder'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        fake = faker.Faker()
        seeder = Seed.seeder()

        if Position_relations.objects.count() < 5:
            level = (x for x in range(1, 6))
            seeder.add_entity(Position_relations, 5, {
                'position': lambda x: fake.job(),
                'level': lambda x: next(level)
            })

        seeder.add_entity(Employes, 10, {
            'first_name': lambda x: fake.first_name_male(),
            'last_name': lambda x: fake.last_name_male(),
            'middle_name': lambda x: fake.first_name_male(),
            'chief': lambda x: Employes.objects.last()
            if Employes.objects.exists() else None,
            'position': lambda x: Position_relations.objects.order_by("?")[0],
            'date_employ': lambda x: fake.date(),
            'salary': lambda x: fake.pydecimal(positive=True, right_digits=2, max_value=15000),
            'user': lambda x: User.objects.create(
                username=fake.profile('username')['username'],
                password=fake.password(),
                email=fake.unique.email()),
        })

        seeder.add_entity(Salary_paid, 100, {
            'emploee': lambda x: Employes.objects.order_by("?")[0],
            'date_paid': lambda x: fake.date(),
            'sum_paid': lambda x: fake.pydecimal(positive=True, right_digits=2, max_value=15000)
        })

        seeder.execute()