from example2 import students, engine

ins = students.insert()

ins = students.insert().values(name='John', lastname='Silver')

conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
   {'name': 'John', 'lastname': 'Cleese'},
   {'name': 'Graham', 'lastname': 'Chapman'},
])





