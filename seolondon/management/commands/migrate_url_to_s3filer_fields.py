# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model
from seolondon.management.commands.helpers.url_to_s3filer import copy_url_to_filer


class Command(BaseCommand):
    help = 'temporary command: migrate filer images'

    def _update_model_url_s3filer(self,
            app_label, model_name, url_field_name, s3filer_field_name):

        model_class = get_model(app_label, model_name)
        qs = model_class.objects.filter(
            **{'{}__startswith'.format(url_field_name): 'http'}).filter(
        **{'{}__isnull'.format(s3filer_field_name): True})

        for instance in qs:
            self.stdout.write('working on {} of {}'.format(instance.id, model_name))
            try:
                copy_url_to_filer(instance, url_field_name, s3filer_field_name)
                self.stdout.write('SUCCESS: updated {} of {}'.format(
                instance.id, model_name))
            except Exception as exc:
                self.stdout.write('FAILED: {} of {}'.format(
                    instance.id, model_name))
                self.stdout.write(str(exc))

    def handle(self, *args, **options):
        configs = [
            {
                'app_label': 'djangocms_repeater',
                'model_name':'SuccessStory',
                'url_field_name':'oldStoryImage',
                's3filer_field_name':'story_image',
            },
            {
                'app_label': 'djangocms_repeater',
                'model_name': 'TeamMember',
                'url_field_name': 'oldImage',
                's3filer_field_name': 'image',
            },
        ]

        for config in configs:
            self._update_model_url_s3filer(**config)
