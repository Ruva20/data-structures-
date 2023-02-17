import numpy as np
L=12 # 
W=10 #load intensity 

#question a
#bending moment(M) and shear force (V), when X=0
X=0
M=(W*(-6*X**2 +6*L*X-L**2))/12

print("The bending moment at X=0 is "+" "+str(M)+"KN")

V=W*(L/2-X)
print("The shear force at X=0 is "+" "+str(V)+"KN")

#let bending moment at X=L be (M1) and shear force be V2
X=12 #when x=l calculating (M) and (V)
M1=(W*(-6*X**2+6*L*X-L**2))/12

print("AtX=L, the bending moment is "+ str(M1)+ "KN")
V1=W*(L/2-X)
print("Also at X=L,the shear force is "+str(V1)+"KN")

#question b
#write an expression to estimate the distanc at which the bending moment will be zero
#using the methods of completing of square X=L*sqrt(3)/6+L/2
#importing the sqrt function from the math module

from math import sqrt
X1=(L*sqrt(3))/6+L/2
X2=(-L*sqrt(3))/6+L/2
print("The distance at which bending moment will be zero(0) is "+" "+str(X1)+"m,"+" "+"or"+" "+str(X2))


#question c
#also determine the point at which the shear force will be zero
#at the midspan the shear force will be zero
#at the midspan X=L/2
#let D be the distance at which shear force will be zero

D=L/2
print("At a distance of"+" "+str(D)+", "+"the shear force will be zero")


#question d
#use numpy array to discrietize a span of L=12m, at a step of 10mm.Using the initialized variable,evaluable the bending moment at each in the array

#but 10mm is equivalent to 0.01m so the step woukd be 0.01
#let s_s be the span tep

s_s=np.arange(0,L+0.01,0.01)

#bending moment at each step
bm_each_step=W*(-6*s_s**2+6*L*s_s-L**2)/12

print("Bending Moment at each step",bm_each_step,"in KNm")


#question e
#also calculate the shear force for each force along the span 
#let shear force for each step to be represented by s_f

s_f=W*(L/2-s_s)

print("shear force at each step :"+str(s_f)+"KN")
abs_BM=np.abs(bm_each_step)


#question f 
#find points along L at which the absolute values of the bending moment array in d is minimum 

#absolue values of the bending moment in (d)
#point along L at which the absolute values of the bending moment is minimum

L_BM_min=s_s[abs_BM==abs_BM.min()]
print(L_BM_min[0],"m")

#question g
#determine the relative errrors between the estimated points of contra_flexure in (b) and (f)

#Relative Error=(Expected-Actual)/(Actual value)*100%
#expected =distance (X1,X2) at which the bending momnent will be maximum 
#Actual value =The value we had in question (f) i.e point along L at which the BM is minimum in (f)


#to convert the distance to an array
Expected=np.array([X1,X2])
Actual=L_BM_min

#Relative error in percent

Relative_Errors=((np.abs(Expected-Actual))/Actual)*100
print("Relative error :", Relative_Errors,"in percent(%)")


#question H
#The point at which maximum and minimum bending moment occurs,using discretized points  
#points along thw discretized points at which the maximum bending moment occur
print("points along which the bending moment is maximum :",s_s[bm_each_step==bm_each_step.max()][0],"in metres")

#points along the discretized points at which the minimum bending moment occur
print("points along which the bending moment is minimum :" ,s_s[ bm_each_step ==bm_each_step.min()][0], "in metres")










