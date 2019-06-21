#main
#main
import os
import csv
import statistics
import numpy as np

#importing the CSV file
csvpath = "../data/eflection_data.csv"
with open ("../data/election_data.csv", "r") as csvfile:
    election_data = csv.reader (csvfile, delimiter=",")
    print(type(election_data))

    #getting headers
    headers = next(election_data)
    #print(headers)

    data = {}
    for h in headers:
        data[h] = []

    print(data)
    print(election_data)


    counter = 0
    for row in election_data:
        counter += 1
        #print(row)
        #two headers under one loop (double loop)
        for h,v in zip(headers, row):
            data[h].append(v)
    total_votes = counter

    #answer to number one
    #print(total_votes)

    ca_original = data["Candidate"]
    cand = set(ca_original)
    #Question number 2 answer
    #print(cand)

    Li = 0
    Oto = 0
    Kha = 0
    Cor = 0

    for cand in ca_original:
        if cand == "Li":
            Li += 1

        elif cand == "Khan":
            Kha += 1

        elif cand == "O'Tooley":
            Oto += 1

        else:
            Cor += 1

    print("Li")
    print(Li)
    print("Khan")
    print(Kha)
    print("O'Tooley")
    print(Oto)
    print("Correy")
    print(Cor)

    li_percent = Li/total_votes
    print(li_percent)

    khan_percent = Kha/total_votes
    print(khan_percent)

    otooley_percent = Oto/total_votes
    print(otooley_percent)

    correy_percent = Cor/total_votes
    print(correy_percent)


 ##Question 5
    max = max(total_percentages)
    print(max)


#keeping main code seperate
def main():
    print("Election Results")
    print("--------------------------------------------------------")

    #print sosmememehrrht
    print("--------------------------------------------------------")


main()
