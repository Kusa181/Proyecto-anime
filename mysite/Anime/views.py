from django.shortcuts import render
from .models import Anim, Author, AnimInstance, Genre

# Create your views here.
def index(request):

    num_animes=Anim.objects.all().count()
    num_intances=AnimInstance.objects.all().count()
    num_authors=Author.objects.count()
    return render(
        request,
        'index.html',
        context={'num_animes':num_animes,'num_instances':num_intances,'num_authors':num_authors},
    )


