#main
import os
import csv
import statistics

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
    value_1 = pl_values[0]
    value_2 = pl_values[1]

    print(value_1)
    print(value_2)

    avg = (value_1 + value_2)/2









            #print(h)
            #print(v)

    #print(data)

    #for row in budget_data:
        #print(row)

#keeping main code seperate
def main():
    print("Financial Analysis")

main()
