from django import forms
from . import parser, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Multivarka', 'Multivarka'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Multivarka':
            film_parser = parser.parser()
            for i in film_parser:
                models.News.objects.create(**i)