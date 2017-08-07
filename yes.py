print ("\n#1")
def isEven(integer):

  if (integer %2 == 0):
    return True

  else:
    return False

print (isEven(45))

#2 short version to display the 1
print("\n#2")

def even(number):
  return bool (number %2 == 0)

print even(20)

#3 another odd ans even stuff
print("\n#3")

def isEgide(x,python = False):
  i = x %2 == 0

  if python == True:
    if i:
      print "number", x, "is even"

    else:
      print "number",x, "is odd"

    return i

x = int(raw_input("Enter an integer:"))

isEgide(x, True)
isEgide(x, False)

print("\n#4")
#it counts 1 to 9 after display Launch

def countup():
  n = 0
  while n <= 9:
    print n+1
    n=n+1
  print"Launch"

#it counts reversed from 11 to 1
def countdown ():
  n = 11
  while n >= 2:
    print n-1
    n=n-1
  print"Egide le Karma"

countup() #when you created a function , you have to call the function by typing the function name
print("\n")
countdown()#when you created a function , you have to call the function by typing the function name

print("\n")


#it asks next object in the content with next(i) until an error message will display cause nothing will remain
i = iter([1, 2, 3])
next(i)
next(i)
next(i)

for E in ([1,2,3,4,]):
 print E

print ("\n")

# display 1 to 4
for x in  range(4):
 print x

print ("\n")

for x in "google":
  print x



#write a function named alternate() that has a string ad a parameter.The function should alternate capitalazing and
#lowercasing the elements of the string

def alternate():
    s = raw_input("Enter a world: ")

    n = ""

    for x in range(0,len(s)):
        if x % 2 == 0:
         n = n + s[x].upper()

        else:
         n = n + s[x].lower()

    print (n)

print ("\n")


# Version 2


def alternate2():
  s = raw_input("Enter a world: ")
  n2 = []

  for x in range(0,len(s),2):
   n2.append(s[x].upper())
  if x+1 < len(s):
     n2.append(s[x+1].lower())
  print("".join(n2))

alternate()
print ("\n")
alternate2()

print ("#5\n")


students = {
    "10005776":"Elvis",
    "10007543":"Abigail",
    "10008712":"Nusrath",
    "10005151":"Olawale",
    "10006570":"olivia",
    "10003570":"Rayona",
    "10002576":"Egide",
    "10005789":"Zanif",
    "10002213":"Rahid",
    "10003207":"Imran",

  }


#write a function studentLookUp() that takes a dictionary and a string as parameters. It should return the key of
#the dictionary entry whose value matches the string parameter.Otherwise , it retuns a string stating 'Invalid Stuent Name'

def studentLookUp(dic,name):
 for x in dic:
  if name == dic[x].lower():
   return x

 return "Invalid Student Name"

name = raw_input("Enter a name:")

print studentLookUp(students,name)
