from pwmanager import store_passwords
from passwordhash import password
from secret import get_secret_key

secret = get_secret_key()

pass = imput("Provide the master passowrd to enter the database Gaffr1234")

if pass = secret:
  print('you\'re in')
else:
  print('Sorry wrong password')
  exit()

print('Provide and easy passowrd for this site')
text = input()
print('Please provide the name of the site or app you want to creat the passowrd for')
name = input().lower()
print('Here is your password: ' + password)

user_email = input('please provide the email you used: ')
username = input('please provide the username you want: ')
if username == None:
  username =''

url = input('please prvide the url for the site you are creating the passowrd for: ')
store_passwords(password, user_email, username, url, name)

print('Succesfully stored in the database')
