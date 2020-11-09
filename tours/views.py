from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View


# Create your views here.
def custom_handler404(request, exception):
    return HttpResponseNotFound(' Ой, страницы не существует... Простите извините!')


def custom_handler500(request, *args, **argv):
    return HttpResponseServerError('Ой, ошибка сервера... Простите извините!')


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure):
        return render(request, self.template_name)


class TourView(View):
    template_name = 'tour.html'

    def get(self, request, id):
        return render(request, self.template_name)
