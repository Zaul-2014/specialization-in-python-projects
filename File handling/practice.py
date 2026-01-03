import time

def read():
  file = open('Data.txt', 'r')

  content = file.read()
  print(content)

read()
#Reading Data.txt
time.sleep(2)
def write():

  file = open('Data.txt', 'w')

  file.write('Hello, that was boring!..')

write()

def append():
  file = open('Data.txt', 'a+')

  file.write("\nMagic")

append()