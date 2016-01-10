#!/usr/bin/env python
#Check your powerball numbers!
#created by Brandon I.


import sys

input_winning_numbers = open("winningnumbers.txt", "r") #opens winning numbers text file in same directory as script file.
#format the file with a comma delimeter, for example: 19,25,29,36,48,12
#the first five should be the white numbers and the last (sixth) should be the powerball
input_your_numbers = open("yournumbers.txt", "r") #opens the text file containing your numbers on your ticket in the same directory as script file.
#format the file with a comma delimeter as above, but a semicolon between sets of numbers on the ticket
#for example: 19,25,29,36,48,12;5,6,29,35,51,21;34,39,42,44,59,8



initial_winning_numbers = input_winning_numbers.read() #reads the text file
initial_your_numbers = input_your_numbers.read() #reads the text file


winning_numbers = initial_winning_numbers.split(',') #splits the winning numbers into a list
#now we will make sure our inputted numbers are actually integers. it will try what is in try, but if there is an error (or what python calls an exception), run the code under except
try:
    sanitized_win = []
    for number in winning_numbers:
        tempwin = int(number)
        sanitized_win.append(tempwin)
except:
    print "There seems to be an error with the winning numbers file. Are they numbers?"
    raw_input("Press Enter to Exit")
    sys.exit()

#this will be how we check our numbers
def checknumbers(sanitized_nums):
    global sanitized_win
    whiteballs = 0 #will count how many white balls we match
    if sanitized_nums[5] == sanitized_win[5]: #checks winningness of powerball
        matchpowerball = True
        print "You matched the powerball"
    else:
        matchpowerball = False
        print "You did not match the powerball"
    mynumbers = [sanitized_nums[0],sanitized_nums[1],sanitized_nums[2],sanitized_nums[3],sanitized_nums[4]]
    winwhites = [sanitized_win[0],sanitized_win[1],sanitized_win[2],sanitized_win[3],sanitized_win[4]]
    for mynumber in mynumbers: #will check numbers for matches
        for winnumber in winwhites:
            if mynumber == winnumber:
                whiteballs = whiteballs + 1
    print "You matched",whiteballs,"White Balls"
    #check for prizes
    if matchpowerball == True:
        if whiteballs == 0:
            prize = 4
        if whiteballs == 1:
            prize = 4
        if whiteballs == 2:
            prize = 7
        if whiteballs == 3:
            prize = 100
        if whiteballs == 4:
            prize = 10000
        if whiteballs == 5:
            prize = "Jackpot"
    if matchpowerball == False:
        if whiteballs == 0:
            prize = 0
        if whiteballs == 1:
            prize = 0
        if whiteballs == 2:
            prize = 0
        if whiteballs == 3:
            prize = 7
        if whiteballs == 4:
            prize = 100
        if whiteballs == 5:
            prize = 1000000
    return str(prize)

separate_tickets = initial_your_numbers.split(';') #splits tickets via the semicolon delimeter

ticketcounter = 0

for ticket in separate_tickets: #run this for each ticket in our list
    
    ticketcounter = ticketcounter + 1 #will identify our ticket by number
    numbers = ticket.split(',') #separates the ticket's numbers
    print "Ticket",ticketcounter
    #this works the same as the try except above, pulling from the list of 'numbers'
   # try:
    sanitized_nums = []
    for number in numbers:
        tempwin = int(number)
        sanitized_nums.append(tempwin)
        #this sends the numbers to my check 'function' above and returns the prize amount
    ticketprize = checknumbers(sanitized_nums)
    print "The prize for ticket",ticketcounter, "is $"+ticketprize
    #except:
        #print "There seems to be an error with ticket",ticketcounter,". Are they numbers?"
    print ""

#closes the files correctly
input_winning_numbers.close()
input_your_numbers.close()
print ""
print "Prizes differ in California. See powerball.com for CA prize info. This program and its developer are not related in any way to Powerball or the Multistate Lottery Association (MUSL). Numbers not official until verified."
print ""
# raw_input("Press enter to exit")


