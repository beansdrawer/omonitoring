from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Record
from django.shortcuts import get_object_or_404

def index(request):

    records = Record.objects.all().order_by('-pk')

    return render(request, 'monitor/index.html', {
        'records' : records
    })


def monitor(request):

    if request.method == "POST" :
        record = Record()
        record.battery = request.POST["battery"] + "%"
        record.led_color = request.POST["led_color"]
        record.firmv = request.POST["firmv"]
        record.encoder = request.POST["encoder"]
        record.save()
        # records = Record.objects.all().order_by('-pk')

        return HttpResponseRedirect('/monitor/')
        # return render(request, 'monitor/monitor.html', {
        #     'records': records
        # })

    else :

        records = Record.objects.all().order_by('-pk')
        # return render(request, 'monitor/monitor_prac.html', {
        return render(request, 'monitor/monitor.html', {
            'records' : records
        })

def monitor_detail(request, pk):

    record = Record.objects.get(pk=pk)
    return render(request, 'monitor/monitor_detail.html', {
        'record': record
    })

def monitor_delete(request, pk):
    delRecord = get_object_or_404(Record, pk=pk)
    delRecord.delete()
    records = Record.objects.all().order_by('-pk')
    return redirect('/monitor', {
        'records' : records
    })

def spec(request):
    records = Record.objects.all().order_by('-pk')
    return render(request, 'monitor/spec.html', {
        'records' : records
    })


def maker(request):

    return render(request, 'monitor/maker.html')