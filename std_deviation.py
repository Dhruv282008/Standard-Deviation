import csv
import math
import statistics

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    
    mean = total / n
    return mean

#Squaring and getting values
squaredlist = []
for n in data:
    a = int(n) - mean(data)
    a = a**2 
    squaredlist.append(a)

#Getting SUM 
sum = 0

for i in squaredlist:
    sum += i
#Dividing the sum by the total values
result = sum/len(data) - 1

#Getting the deviation by getting the SQUARE ROOT of the result
std_deviation = math.sqrt(result)
print(std_deviation)
#print("Derived using Predefined functions through statistics module ", statistics.stdev(data))
print("derived using predefined function ",statistics.stdev(data))

