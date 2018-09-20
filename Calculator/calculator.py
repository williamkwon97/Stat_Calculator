import math
import statistics
# Description: calulator for lazy people who need to online HW
# You can always modified the code to caculate diffeernt stuff
# How to use this Caclulator
#1.Just copy and paste the numbers from the problem
#2 emove Hashtag if you want to use that specific function
# For example you copy the list of numbers with comma init than instead of add comma one by one use a=a.replace.
# a is list and b is list 2 so you can calculate convariance of coffiencent of variation
a = "   7 20  24  17  11  9  6  8  3 2"
#a = a.replace(',', '')

a=a.split()
#a=sorted(a) #use when you want sort by ascending order for a

b= "0.102803738317757 0.1588785046728972 0.018691588785046728 0.18691588785046728 "
b=b.split()
#b=b.split() #use when you want sort by ascending order for a
list=[]
list2=[]
list=[float(i) for i in a]
list2=[float(i) for i in b]

mean=(statistics.mean(list))     #print this when you want mean for a
stdev= (statistics.stdev(list))  #print this when you want standard deviation for a
median=statistics.median(list)   #print this when you want median for b
mean2=(statistics.mean(list2))   #print this when you want mean for for b
stdev2=(statistics.stdev(list2)) #print this when you want standard deviation for b
var=statistics.variance(list)    #print this when you want variance for a
var2=statistics.variance(list2)  #print this when you want variance for a
stdev2rule = mean+2*stdev        #Standard deviation second Rule
range=max(a)-min(a)              #print this when you want range of a
range2=max(b)-min(b)             #print this when you want range of b
mode=statistics.mode(a)          #print this when you want mode for a
mode2=statistics.mode(b)         #print this when you want mode for b

sum1=sum(list)+(.23*.5)+(3.07*.5)
new=max(list)-1.0245
for i in list:
    print(i/sum(list))
print(sum(list2))
newlista=[]
newlistb=[]
for item in list:                   #modified the code if you want to use calculate for each numbs item
    newlista.append((item/60))
for item in list2:
    newlistb.append(math.sqrt(item))
stdev= (statistics.stdev(newlista))
var=statistics.variance(newlista)

#credit William Kwon