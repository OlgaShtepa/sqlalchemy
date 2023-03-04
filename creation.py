from sqlalchemy import create_engine

engine = create_engine('sqlite:///bazatest.db')

print(engine.driver)

print(engine.table_names())

print(engine.execute("SELECT * FROM measures"))

results = engine.execute("SELECT * FROM measures")

for r in results:
   print(r)
