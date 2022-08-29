def reverse_list(liste):
    for i in liste:
        if type(i) == list:
            i.reverse()
        else:
            liste.reverse()
    return liste
