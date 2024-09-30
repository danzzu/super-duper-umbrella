from django.shortcuts import redirect, render
from django.views import View

from django_project.forms import ItemForm
from django_project.models import Item as ItemModel


class Home(View):

  def get(self, request):
    list_items = list(ItemModel.objects.all())
    return render(request=request,
                  template_name="index.html",
                  context={"items": list_items})


class Item_Info(View):

  def get(self, request, name):
    find_item = ItemModel.objects.get(name=name)
    return render(
        request=request,
        template_name="info.html",
        context={'item': find_item},
    )


class Item(View):

  def get(self, request):
    return render(request=request,
                  template_name='new.html',
                  context={'form': ItemForm().as_div()})

  def post(self, request):
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():
      form_data = form.cleaned_data
      item = ItemModel(name=form_data['name'],
                       manufacturer=form_data['manufacturer'],
                       cost=form_data['cost'],
                       weight=form_data['weight'],
                       image=form_data['image'])
      item.save()
      return redirect('/')
    else:
      form = ItemForm()
      return render(request=request,
                    template_name='new.html',
                    context={'form': form})
