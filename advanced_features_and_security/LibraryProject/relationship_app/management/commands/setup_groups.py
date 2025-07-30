from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Set up user groups and assign permissions'

    def handle(self, *args, **kwargs):
        permissions_map = {
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
            'Editors': ['can_create', 'can_edit'],
            'Viewers': ['can_view'],
        }

        content_type = ContentType.objects.get_for_model(Book)

        for group_name, perms in permissions_map.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                perm = Permission.objects.filter(codename=codename, content_type=content_type).first()
                if perm:
                    group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' setup complete."))

