def connection(**kwargs):
  type(kwargs)
  for key in kwargs:
    print(f"{key} = {kwargs[key]} \n")
  return kwargs.items()

config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

print(connection(**config))
