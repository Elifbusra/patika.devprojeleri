list2 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten_list(list1):
  for i in list1:
    if (type(list1) == list):
      flatten(i)
    else:
      list.append(i)
  return list
flatten(list1)

