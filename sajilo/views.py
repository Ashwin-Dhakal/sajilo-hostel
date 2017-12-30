from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import All_hostel

def searchlist(request):
    queryset_list=All_hostel.objects.all()
    query1= str.lower(request.GET.get('q1'))
    query2= str.lower(request.GET.get('q2'))
    if query1 and query2:
        queryset_list = All_hostel.objects.filter(Q(gender=query1) &
                                                Q(location=query2)).distinct()
        context={'queryset_list':queryset_list}
        return render(request,'sajilo/searchlist.html',context)
    else:
        return render(request, 'sajilo/404.html')



def index(request):
    return render(request,'sajilo/index.html')

def hostel_list(request):
    queryset = All_hostel.objects.all()
    context = {
        "object_list": queryset,  # this context is the dictionary for impoting the objects of databaser
            }
    return render(request, 'sajilo/hostel_list.html', context)

def hostel_detail(request, id):
    instance = get_object_or_404(All_hostel, id=id)
    context = {
           "instance":instance,
                }
    return render(request, 'sajilo/hostel_detail.html', context)


