from django.shortcuts import render, redirect
from .models import Person
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
# Create your views here.


def home(request):
    return render(request, 'data/home.html')


#@login_required
def search(request):
    if request.method == 'POST':
        if request.POST['first'] == '' and request.POST['last'] == '' and request.POST['address'] == '' \
                and request.POST['city'] == '' and request.POST['state'] == '' and request.POST['zip'] == '' \
                and request.POST['phone'] == ''and request.POST['email'] == '':
            context = {
                'error': 'You forgot to enter something'
            }
            return render(request, 'data/search.html', context)
        elif request.POST['phone'] == '':
            result = Person.objects.filter(first__contains=request.POST['first'], last__contains=request.POST['last'],
                                           address__contains=request.POST['address'],
                                           city__contains=request.POST['city'],
                                           state__contains=request.POST['state'], zip__contains=request.POST['zip'],
                                           business_name__contains=request.POST['business'],
                                           email__contains=request.POST['email'])
            context = {
                'result': result
            }
            return render(request, 'data/search.html', context)

        else:
            result = Person.objects.filter(first__contains=request.POST['first'], last__contains=request.POST['last'],
                                           address__contains=request.POST['address'], city__contains=request.POST['city'],
                                           state__contains=request.POST['state'], zip__contains=request.POST['zip'],
                                           business_name__contains=request.POST['business'],
                                           email__contains=request.POST['email'], cell__contains=request.POST['phone'])
            context = {
                'result': result
                }
            return render(request, 'data/search.html', context)

    else:
        return render(request, 'data/search.html')


#@login_required
def add_new_person(request):
    if request.method == 'POST':
        new_person = Person(first=request.POST['first'], last=request.POST['last'], address=request.POST['address'],
                            city=request.POST['city'], state=request.POST['state'], zip=request.POST['zip'],
                            email=request.POST['email'])
        new_person.save()
        return render(request, 'data/add_new_person.html')
    else:
        return render(request, 'data/add_new_person.html')


class UpdateView(UpdateView):
    model = Person
    template_name = 'data/edit.html'
    fields = '__all__'
    success_url = '/data/search'
