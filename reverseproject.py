def reverse_list(girdi):
    for i in girdi:
        if isinstance(i,list):
            i.reverse()
    girdi.reverse()    
    return girdi
l = [1,2,3,4]
print(reverse_list(l))

