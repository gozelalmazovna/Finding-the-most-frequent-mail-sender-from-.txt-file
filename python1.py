#From given .txt file find the most frequent mail sender
#and number of times mails were sent
#by gozel.almazovna

#open the file
fhand = open("mbox-short.txt" , "r")

#initialize variables
big_address = None
big_count = None
list_address = list()
counts = dict()

#Find lines with "From:" and save them in a list
for line in fhand:
    if not line.startswith("From:"):
        continue
    else:
        words = line.split()
        list_address.append(words[1])

#Make dictionary with senders and counts of mails
for each in list_address:
    counts[each] = counts.get(each,0) + 1

#Find the biggest in the dictionary
for key,value in counts.items():
    if big_address is None or value > big_count:
        big_address = key
        big_count = value

#Print the result to user
print("The most frequent sender is",big_address,", sent",big_count,"times")
