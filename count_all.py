def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    key=["LETTERS","DIGITS"]
    letters=0;digits=0
    for i in txt:
        if i.isdigit():
            digits+=1
        elif i.isalpha():
            letters+=1
    value=[letters,digits]
    return dict(zip(key,value))