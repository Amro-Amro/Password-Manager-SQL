import psycopg2

try:
  connection = psycopg2.connect(user= 'Gaffr', password = 'gaffr', host = '127.0.0.1', database= 'password_manager')
  cursor = connection.cursor()
  postgres_insert_query = """ Insert into accounts (password, email, username, url, app_name) """
  record_to_insert = ('password123', 'gaffr@gmail.com', 'gaffr', 'https://gaffrabu.com/', 'gaffrabu')
  cursor.execute(postgres_insert_query, record_to_insert)
  
  connection.commit()
  count = cursor.rowcount()
  print(count, 'record inserted!')
except (Exception, psycopg2.Error) as error:
  print(error)
  
