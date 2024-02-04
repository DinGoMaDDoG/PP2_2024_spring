def Hist(histogram):
  for i in histogram:
    cat=""
    for j in range (0, i):
      cat+="*"
    print (cat)
  



print("Enter list:")
histogram0=input()
histogram=[]
for x in histogram0.split():
  histogram.append(int(x))
Hist(histogram)