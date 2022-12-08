from django.shortcuts import render
from django.views import View
# Create your views here.

class index_view(View):
    template = 'portafolio/index.html'

    def get(self, request):
        return render(request, self.template)

# def index(request):
#     return render(request, "portafolio/index.html")