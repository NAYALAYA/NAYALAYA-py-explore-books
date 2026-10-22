import matplotlib.pyplot as plt
import csv

with open("YA_Books.csv", mode = "r", encoding = "utf-8") as bookfile:

    books = csv.reader(bookfile)
    next(books)

    x = []
    y = []

    for row in books :

        y.append(row[0])
        x.append(row[6])

plt.bar(x,y)
plt.show()