#main
import os
import csv

#importing the CSV file
csvpath = "../data/budget_data.csv"
with open ("../data/budget_data.csv", "r") as csvfile:
    budget_data = csv.reader (csvfile, delimiter=",")

    #getting headers
    headers = next(budget_data)

    data = {}

    for h in headers:
        data[h] = []

    print(data)

    #for row in budget_data:
        #print(row)

#keeping main code seperate
def main():
    print("this is the main file")
    print("Financial Analysis")

main()
