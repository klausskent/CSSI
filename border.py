def custumBox (width,height):
  box =""
  for i in range(width): #range(0,width)
   box = box ="#"

  for i in range(height):
    print(box)

custumBox(8,10)

#----------------------------------------------------------------------------------------------

tbborder= "########"
lrborder="##    ##"

for i in range(0,8):
     if i in [2,3,4,5]:
       print lrborder
     else:
        print tbborder
print

#----------------------------------------------------------------------------------------------
def custumBox3(width,height):

  tbborder= "#"* width
  lrborder='##'+' '*(width-4)+ '##'


  for i in range(2):
   print tbborder
  for i in range(height-4):
   print lrborder
  for i in range(2):
   print tbborder
custumBox3(80,30)


#Prof Version
#----------------------------------------------------------------------------------------------
def customBoxZ():

  tbgborder_height="########"
  tbgborder_width= "##    ##"

  for i in range(2):
    print tbgborder_height

  for i in range(4):
    print tbgborder_width


  for i in range(2):
    print tbgborder_height


print customBoxZ()
#------------------------------------------------------------------------------------------------

info =""

info =("#" * 27) + '\n'
for j in range(8):
  info = info + "# "
  for i in range(1,9):
   info = info + chr(65+j) + str(i)
   info = info + " "
   #if i !=8
  info = info + '#\n'
info = info +("#" * 27)

print (info)  
