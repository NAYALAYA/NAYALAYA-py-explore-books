import csv
# comma separated value

with open("YA_Books.csv", mode = "r", encoding = "utf-8") as bookfile:
# mode "r" means read 
# as file means alias/nickname   
    
    books = csv.reader(bookfile)
    # skip the header row
    next(books)

    # author col is at indext 1
    min_year = 0
    max_rating = 5
    min_rating = 0
    max_pages = 1000
    min_pages = 0

    for row in books:
        # print out only authors that start with "M"
        if (row[1].startswith("M")):
            print(row[1])

        # print out last names (slice em up)
        authorname = row[1]
        lastindex = authorname.rfind(" ")
        lastname = authorname[lastindex + 1:]
        if lastname.startswith("J"):
            print(authorname)

        # find most recent book (highest number)
        year = int(row[2])
        if min_year < year:
            min_year = year
            most_recent_book = row


        # get the book with the worst rating (lowest number)

        rating = float(row[6])
        if max_rating > rating:
            max_rating = rating
            worst_rating = row


         # highest rating (highest number)

        rating2 = float(row[6])
        if min_rating < rating2:
            min_rating = rating2
            highest_rating = row


    # page difference between the longest and shortest book
        # smaller number of pages
        pages = int(row[5])
        if max_pages > pages:
            max_pages = pages
            shortest_num_pages = row

            small = row[5]
        # larger number of pages
        pages2 = int(row[5])
        if min_pages < pages2:
            min_pages = pages2
            longest_num_pages = row

            large = row[5]

    x = int(large) - int(small)

    print(f"Most recent book: \n{most_recent_book}")
    print(f"The worst rating: \n{worst_rating}")
    print(f"The highest rating: \n{highest_rating}")
    print(x)
