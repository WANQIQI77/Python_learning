import pickle

mydict = {'001': ('张三', '18'), '002': ('李四', '20'), '003': ('Mike', '14'), '004': ('Sara', '23'),
          '005': ('White', '20')}

file = open('data\\pickle.txt', 'wb')
pickle.dump(mydict, file)
