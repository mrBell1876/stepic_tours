import random

from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render
from django.views import View

from tours.data import tours, departures, title, subtitle, description


def custom_handler404(request, exception):
    return HttpResponseNotFound(' Ой, страницы не существует... Простите извините!')


def custom_handler500(request, *args, **argv):
    return HttpResponseServerError('Ой, ошибка сервера... Простите извините!')


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        random_tours = {}
        list_id = random.sample([id for id in tours.keys()], 6)
        for tour in list_id:
            random_tours[tour] = tours[tour]
        context = {
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "tours": random_tours
        }
        return render(request, self.template_name, context)


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure):
        filtered_tours = {}
        price_min = 0
        price_max = 0
        prices_tours = []
        nights_tours = []
        nights_min = 0
        nights_max = 0
        if departure in departures:
            for tour in tours:
                if departure == tours[tour]['departure']:
                    filtered_tours[tour] = tours[tour]

            for tour_values in filtered_tours.values():
                prices_tours.append(tour_values['price'])
                nights_tours.append(tour_values['nights'])
                price_min = min(prices_tours)
                price_max = max(prices_tours)
                nights_min = min(nights_tours)
                nights_max = max(nights_tours)

            context = {
                "tours": filtered_tours,
                "pricemin": price_min,
                "pricemax": price_max,
                "nightsmax": nights_max,
                "nightsmin": nights_min,
                "departure": departures[departure]
            }

            return render(request, self.template_name, context)
        else:
            raise Http404


class TourView(View):
    template_name = 'tour.html'

    def get(self, request, id):
        if id in tours:
            context = {
                "tour": tours[id],
                "departure": departures[tours[id]['departure']]
            }
            return render(request, self.template_name, context)
        else:
            raise Http404
