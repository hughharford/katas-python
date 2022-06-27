
import csv
# BAD SYNTAX ERROR _______ DO NOT USE: can corrupt etc
# csvfile = open('data/addresses.csv')
# # print(type(csvfile))
# readfile = csv.reader(csvfile)
# print(type(readfile))
# print(dir(readfile)) # output the methods available
# for row in readfile:
#     print(readfile.line_num, ' - ', row)
#     print(row)


# GOOD SYNTAX to list

# with open('data/addresses.csv') as csvfile:
#     reader = csv.reader(csvfile, skipinitialspace=True)
#     for row in reader:
#         # row is a `list`
#         print(row)

# GOOD SYNTAX to dict - to get the headers

# with open('data/biostats.csv') as csvfile:
#     reader = csv.DictReader(csvfile, skipinitialspace=True)
#     for row in reader:
#          # row is a collections.OrderedDict
#         print(row['Name'], row['Sex'], int(row['Age']))

# WRITING A CSV...

# define something to write:
beatles = [
    { 'first_name': 'John', 'last_name': 'lennon', 'instrument': 'guitar'},
    { 'first_name': 'Ringo', 'last_name': 'Starr', 'instrument': 'drums'}
]

# write with 'w' open, 'a' to append
with open('data/beatles.csv', 'w') as csvfile:
    # write, and set the headers:
    ##NOTE: use this only once at the start of the file, of course
    writer = csv.DictWriter(csvfile, fieldnames=beatles[0].keys())
    writer.writeheader()

    # now write the rows
    for beatle in beatles:
          writer.writerow(beatle)
