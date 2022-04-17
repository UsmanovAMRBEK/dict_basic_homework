def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    cities_dict = {}
    indx=0
    for city in cities:
        cities_dict[indx] = city
        indx+=1
    return cities_dict
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))
