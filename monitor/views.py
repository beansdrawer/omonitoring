from django.shortcuts import render
from .models import Record

def index(request):

    records = Record.objects.all().order_by('-pk')

    return render(request, 'monitor/index.html', {
        'records' : records,
        'color': 'red'
    })


def monitor(request):

    records = Record.objects.all().order_by('-pk')

    # return render(request, 'monitor/monitor_prac.html', {
    return render(request, 'monitor/monitor.html', {
        'records' : records,
        'color': 'red'
    })

def monitor_detail(request, pk):

    record = Record.objects.get(pk=pk)
    return render(request, 'monitor/monitor_detail.html', {
        'record': record
    })

def spec(request):
    records = Record.objects.all().order_by('-pk')

    return render(request, 'monitor/spec.html', {
        'records' : records,
        'color': 'red'
    })


def maker(request):

    return render(request, 'monitor/maker.html')