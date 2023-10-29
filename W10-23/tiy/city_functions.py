# def city_country(city, country):
#     place = f"{city.title()}, {country.title()}"
#     return place

# def city_country(city, country, population):
#     place = f"{city.title()}, {country.title()} - population {population}"
#     return place

def city_country(city, country, population=""):
    if population:
        place = f"{city.title()}, {country.title()} - population {population}"
        return place
    else:
        place = f"{city.title()}, {country.title()}"
        return place
