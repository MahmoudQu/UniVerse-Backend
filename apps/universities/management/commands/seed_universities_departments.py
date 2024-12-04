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

        # Departments data
        departments_data = [
            'Engineering',
            'Information Technology (IT)',
            'Business and Economics',
            'Architecture and Design',
            'Medicine and healthcare',
            'Arts and Humanities',
            'Law and Sharia',
            'Education',
            'Science',
            'Agriculture',
            'Other',
        ]

        # Seed Universities
        for name in universities_data:
            University.objects.get_or_create(name=name)

        # Seed Departments
        for name in departments_data:
            Department.objects.get_or_create(name=name)

        self.stdout.write(self.style.SUCCESS('Successfully seeded universities and departments'))