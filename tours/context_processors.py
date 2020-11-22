from tours.data import departures


def menu(request):
    return {"menu": departures, "title_main": "Stepik Travel"}
