#imports
from time import sleep
from decimal import Decimal

#vars
modeLoopinc = 0 #determines the increment of the loop used in the mode section
numList = 0 #where the data set is stored
meanVar = 0 #finalized mean of the data set
medianVar = 0 #finalized median of the data set
medianLocate = 0 #where the median should be
splitMedian = 0 #boolean, whether the median is split between two numbers or not
median1 = 0 #used to get the median using calculations if splitMedian is True, along with median2 and median3
median2 = 0
median3 = 0
QLocate = 0
Q3Locate = 0
Q1 = 0
numQ1 = []
Q3 = 0 
numQ3 = []
modeVar = 0 #finalized mode of the data set
modeLow = 0 #this and modeHigh will determin how long the loop in the mode section will go
modeHigh = 0
modeArray = [] #array for storing the values of how many of what numbers there are
rangeVar = 0 #finalized range of the data set
loop = 0 #used for loops

#classes
class numberCount: #this will be used to organize objects in the mode section during array creation 
 def __init__(self,number,count):
  self.number = number #the current number
  self.count = count #the count of the current number

 def __lt__(self, other):
  return self.count > other.count #supposedly should sort by the count, we'll see tho ¯\_(ツ)_/¯
  #this did work, gonna try switching this '<' for this '>'

numList = input('data set(put spaces between numbers):')
numList = numList.split()

modeLoopinc = input('how many Decimal places will there be at most(use an example ending in a 1 with every other number being 0):')

modeLoopinc = Decimal(modeLoopinc)


#sorting and printing array
numList.sort(key=Decimal)
print('sorted array :',str(numList))

#converting to Decimals
while loop < len(numList):
 numList[loop] = Decimal(numList[loop])
 loop += 1

#mean section
#calculation
loop = 0
while loop < len(numList):
 meanVar += numList[loop]
 loop += 1
meanVar /= len(numList)
print('mean :',meanVar)
#the mean was actually one of the easier ones to make, really easy to add and divide in code, brain is a lot
#better at recognising where the middle numbers are, median was pretty hard.

#median section, this if statement checks whether there are an even or odd amount of numbers in the array
if (len(numList) % 2) == 0:
 splitMedian = True
else:
 splitMedian = False

#getting the location of the median
medianLocate = len(numList) / 2

#rounding the median location
if isinstance(medianLocate, float) == True:
 round(medianLocate)

#final calculations
medianLocate = int(medianLocate)
if splitMedian == True:
 #calculations for a split median
 median1 = numList[medianLocate]
 median2 = numList[medianLocate-1]
 median3 = median1 - median2
 median3 /= 2
 medianVar = median3 + median2
else:
 #not much calculation needed for an odd data set
 medianVar = numList[medianLocate]
print('median :',medianVar)

#quartile subsection:median

#Q1 calculation
#gonna reuse some vars and we'll have some pretty similar stuff happening to median
numQ1 = numList[:len(numList)//2]

if (len(numQ1) % 2) == 0:
 splitMedian = True
else:
 splitMedian = False

#getting the location of the median
medianLocate = len(numQ1) / 2

#rounding the median location
if isinstance(medianLocate, float) == True:
 round(medianLocate)

#final calculations
medianLocate = int(medianLocate)
if splitMedian == True:
 #calculations for a split median
 median1 = numQ1[medianLocate]
 median2 = numQ1[medianLocate-1]
 median3 = median1 - median2
 median3 /= 2
 Q1 = median3 + median2
else:
 #not much calculation needed for an odd data set
 Q1 = numQ1[medianLocate]
print('quartile 1 :',Q1)

#quartile subsection:median
#testing for a split median in quartiles
if (len(numList) % 4) == 0:
 splitMedian = True
else:
 splitMedian = False

#Q3 calculation
#gonna reuse some vars and we'll have some pretty similar stuff happening to median
numQ3 = numList[len(numList)//2:]

numQ3.pop(0)

if (len(numQ3) % 2) == 0:
 splitMedian = True
else:
 splitMedian = False

#getting the location of the median
medianLocate = len(numQ3) / 2

#rounding the median location
if isinstance(medianLocate, float) == True:
 round(medianLocate)

#final calculations
medianLocate = int(medianLocate)
if splitMedian == True:
 #calculations for a split median
 median1 = numQ3[medianLocate]
 median2 = numQ3[medianLocate-1]
 median3 = median1 - median2
 median3 /= 2
 Q1 = median3 + median2
else:
 #not much calculation needed for an odd data set
 Q1 = numQ3[medianLocate]
print('quartile 3 :',Q1)

loop = 0

#mode section
modeLow = Decimal(numList[0]) #finding the lowest number on the list
modeHigh = Decimal(numList[len(numList) - 1]) #finding the highest number
modeLow -= Decimal('0.5')
modeLow = round(modeLow)
loop = modeLow
while loop <= modeHigh:
 modeArray.append(numberCount(loop,numList.count(loop))) #this sticks the objects in the array, first is the 
 loop += modeLoopinc                                     #current number, using loop to put that in, then
                                                         #we use the count of how many of the current number
modeArray.sort()                                         #appears in numList

loop = 0
#while loop < Decimal(len(modeArray)):
# try:
#  print(modeArray[loop].number, ':' ,modeArray[loop].count, ' ' , modeArray[loop+1].number, ':' ,modeArray[loop+1].count, ' ' , modeArray[loop+2].number, ':' ,modeArray[loop+2].count)
#  loop += 3
# except:
#  print(modeArray[loop].number, ':' ,modeArray[loop].count)
#  loop += 1
#use these to print out what the mode array looks like
broke = False
try:
 modeVar = modeArray[0].number
except:
 try:
  print(modeArray[0].number)
 except:
  try:
   print(modeArray[0])
  except:
   print('not working ¯\_(ツ)_/¯')
   broke = True
if broke != True:
 print('mode :', modeVar, ', with', modeArray[0].count, 'instances')
else:
 print('fricken code doesn\'t work')
#and that's the mode done

#range section, this is really easy, gonna reuse the modeHigh and modeLow variables
rangeVar = modeHigh - modeLow
print('range :',rangeVar)