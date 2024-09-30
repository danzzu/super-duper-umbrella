from django.db.models import CharField, ImageField, IntegerField, Model


class Item(Model):
  name = CharField(max_length=30)
  manufacturer = CharField(max_length=30)
  cost = IntegerField()
  weight = IntegerField()
  image = ImageField(upload_to='django_project/static/images')
