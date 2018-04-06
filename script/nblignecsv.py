def csvcount(filename):
    with open(filename, 'r') as f:
        i = 0
        for ligne in f:
            i += 1
    print i

#
# csvcount("data_output.csv")
csvcount("data_lyon.csv")