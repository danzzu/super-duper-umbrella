from django.forms import CharField, Form, ImageField, IntegerField


class ItemForm(Form):
  name = CharField()
  manufacturer = CharField()
  cost = IntegerField()
  weight = IntegerField()
  image = ImageField()
