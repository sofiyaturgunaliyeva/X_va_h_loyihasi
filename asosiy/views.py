from django.shortcuts import render
from.models import *
# from django.shortcuts import render, redirect

def home(sorov):
    qidiruv = sorov.GET.get("searched")
    # xohish
    togri = Togri.objects.filter(soz = qidiruv)
    if len(togri) == 0:
        notogri = Notogri.objects.filter(soz = qidiruv)
        if len(notogri) == 0:
            togri = "Bunaqa so'z bazada yo'q"
            notogri = ""
        else:
            togri = notogri[0].togri_s
            notogri = Notogri.objects.filter(togri_s = togri)
    else:
        togri = togri.first()
        notogri = Notogri.objects.filter(togri_s=togri)
    content = {
        "t": togri,
        "n": notogri
    }
    return render(sorov,'result.html',content)