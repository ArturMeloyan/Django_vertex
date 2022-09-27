from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeBG, Info
# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        info = Info.objects.all()
        return render(request, self.template_name, {'homebg':homebg, 'info':info})
