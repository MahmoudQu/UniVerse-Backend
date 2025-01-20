from django.core.management.base import BaseCommand
from django_seed import Seed
from apps.universities.models import University
from apps.departments.models import Department


class Command(BaseCommand):
    help = 'Seed the database with universities and departments'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        # Universities data
        universities_data = [
            'The University of Jordan',
            'Yarmouk University',
            'Mutah University',
            'Jordan University of Science and Technology',
            'The Hashemite University',
            'Al al-Bayt University',
            'Al-Balqa Applied University',
            'Al-Hussein Bin Talal University',
            'Tafila Technical University',
            'German-Jordanian University',
            'Al-Ahliyya Amman University',
            'Applied Science Private University',
            'Amman Arab University',
            'Irbid National University',
            'Al-Isra University',
            'Jadara University',
            'Jerash Private University',
            'Middle East University',
            'Jordan Academy of Music',
            'Petra University',
            'Philadelphia University',
            'Zarqa Private University',
            'Princess Sumaya University for Technology',
            'Al-Zaytoonah University of Jordan',
            'Other',
        ]

        # Departments data with icons
        departments_data = [
            {'name': 'Engineering', 'icon': 'flaticon-settings-1'},
            {'name': 'Information Technology (IT)',
             'icon': 'flaticon-web-programming'},
            {'name': 'Business and Economics', 'icon': 'flaticon-money-1'},
            {'name': 'Architecture and Design', 'icon': 'flaticon-vector'},
            {'name': 'Medicine and healthcare', 'icon': 'flaticon-first-aid-kit-1'},
            {'name': 'Arts and Humanities', 'icon': 'flaticon-headhunting'},
            {'name': 'English and translation', 'icon': 'flaticon-promotion'},
            {'name': 'Education', 'icon': 'flaticon-notebook'},
            {'name': 'Science', 'icon': 'flaticon-heart'},
            {'name': 'Agriculture', 'icon': 'flaticon-car'},
            {'name': 'Other', 'icon': 'flaticon-rocket-ship'},
        ]

        # Seed Universities
        for name in universities_data:
            University.objects.get_or_create(name=name)

        # Seed Departments with icons
        for department in departments_data:
            Department.objects.get_or_create(
                name=department['name'],
                icon=department['icon']
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded universities and departments with icons'))
