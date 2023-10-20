def city_country(city, country, population=""):
    if population == "":
        fullname = f"{city}, {country}"
        return fullname.title()
    else:
        fullname = f"{city}, {country}".title()
        fullname += f" - population {population}"
    return fullname


print(city_country("miami", "united states", 9000))
