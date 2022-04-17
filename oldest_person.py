def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    oldest_per=0;oldest_per_nam=''
    for i,j in people.items():
        if j>oldest_per:
            oldest_per=j
            oldest_per_nam=i
    return oldest_per_nam