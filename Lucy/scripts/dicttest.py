x = [{"key":1,"value":2},{"key":3,"value":4},{"key":1,"value":33}]

for i in x:
    print i["key"]

# if (x["key"]==1):
#     x["value"]+=1
# else:
#     x["value"]+=2

# print x

# y = (item for item in x if item["key"] == 2).next()
# y["value"]+=1
# print y

z = filter(lambda thing: thing['key'] == 1, x)
w = filter(lambda thing2: thing2['value']==33,z)
w[0]["value"]+=1
print w
print x

# my_dicts = [ 
#     { 'key1' : 'value1',
#       'key2' : 'value2' },

#     { 'key1' : 'value1',  
#       'key2' : 'value2' },

#     { 'key1' : 'value1',  
#       'key2' : 'value2' }]

# for d in my_dicts:
#     d.update((k, "value3") for k, v in d.iteritems() if v == "value2")