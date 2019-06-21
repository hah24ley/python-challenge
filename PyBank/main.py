#main
import os
import csv
import statistics
import numpy as np

#importing the CSV file
csvpath = "../data/budget_data.csv"
with open ("../data/budget_data.csv", "r") as csvfile:
    budget_data = csv.reader (csvfile, delimiter=",")
    print(type(budget_data))

    #getting headers
    headers = next(budget_data)

    data = {}

    for h in headers:
        data[h] = []

    counter = 0
    for row in budget_data:
        counter += 1
        #print(row)
        #two headers under one loop (double loop)
        for h,v in zip(headers, row):
            data[h].append(v)

    pl_values = data["Profit/Losses"]
    sum = 0
    for value in pl_values:
        value = int(value)
        sum = sum + value

    #Question number two -- answer to total profit loss
    #print(sum)
    #Question number one -- answer to total in dates
    #print(counter)

#get average of first and second
#map is changing the type of one data structure to another
    pl_values = list(map(int, pl_values))
    avg1 = 0
    changes = []
    while avg1 < len(pl_values):
        avg2 = avg1 + 1
        if avg2 == 86:
            break
        #print(pl_values[avg1])
        pl1 = pl_values[avg1]
#stroing averages within different to pull and minipulate
        #print(pl_values[avg2])
        pl2 = pl_values[avg2]

        change = pl2 - pl1
        changes.append(int(change))

        avg1 += 1

    avg_of_change = np.mean(changes)
    #answer to number 4 change in profit with the biggest increase --
    #print(avg_of_change)

    max = max(changes)
    print(max)

    min = min(changes)
    print(min)
    
    #answer to number three
    #print(avg_of_change)
    #print(averages)
#add break to get while loop to stop at the right point

#averages of averages - https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list



    #print(data)

    #for row in budget_data:
        #print(row)

#keeping main code seperate
def main():
    print("Financial Analysis")

main()
