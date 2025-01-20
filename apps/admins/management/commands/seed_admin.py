from django.core.management.base import BaseCommand
from apps.admins.models import Admin
from apps.accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Seed admin data'

    def handle(self, *args, **options):
        # Create CustomUser for admin
        admin_user, created = CustomUser.objects.get_or_create(
            email='admin@admin.com',
            defaults={
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        # Create or update Admin profile
        admin, created = Admin.objects.get_or_create(
            user=admin_user,
            defaults={
                'first_name': 'Admin',
                'last_name': 'One',
                'is_admin': True
            }
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'Admin {"created" if created else "updated"} successfully'
            )
        )