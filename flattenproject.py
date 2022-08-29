listnew = []
def flatten_list(liste):
    for i in liste:
        if type(i) == list:
            flatten_list(i)
        else:
            listnew.append(i)
    return listnew
print(listnew)
