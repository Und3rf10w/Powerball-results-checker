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
    win1 = int(winning_numbers[0]) #remember lists start at 0!
    win2 = int(winning_numbers[1])
    win3 = int(winning_numbers[2])
    win4 = int(winning_numbers[3])
    win5 = int(winning_numbers[4])
    winpowerball = int(winning_numbers[5])
except:
    print "There seems to be an error with the winning numbers file. Are they numbers?"
    raw_input("Press Enter to Exit")
    sys.exit()

#this will be how we check our numbers
def checknumbers(my1, my2, my3, my4, my5, mypowerball):
    global win1
    global win2
    global win3
    global win4
    global win5
    global winpowerball
    global prize

    mynumbers = [my1, my2, my3, my4, my5]
    whiteballs = 0 #will count how many white balls we match
    if mypowerball == winpowerball: #checks winningness of powerball
        matchpowerball = True
        print "You matched the powerball"
    else:
        matchpowerball = False
        print "You did not match the powerball"
    for mynumber in mynumbers: #will check numbers for matches
        if mynumber == win1:
            whiteballs = whiteballs + 1
        elif mynumber == win2:
            whiteballs = whiteballs + 1
        elif mynumber == win3:
            whiteballs = whiteballs + 1
        elif mynumber == win4:
            whiteballs = whiteballs + 1
        elif mynumber == win5:
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
    try:
        my1 = int(numbers[0])
        my2 = int(numbers[1])
        my3 = int(numbers[2])
        my4 = int(numbers[3])
        my5 = int(numbers[4])
        mypowerball = int(numbers[5])
        #this sends the numbers to my check 'function' above and returns the prize amount
        ticketprize = checknumbers(my1, my2, my3, my4, my5, mypowerball)
        print "The prize for ticket",ticketcounter, "is $"+ticketprize
    except:
        print "There seems to be an error with ticket",ticketcounter,". Are they numbers?"
    print ""

#closes the files correctly
input_winning_numbers.close()
input_your_numbers.close()
print ""
print "And now the legals..."
print ""
print "Numbers not official until verified. All winning tickets must be redeemed in the state/jurisdiction in which they are sold."
print "Prizes subject to change. Prize amounts differ in california. visit http://www.powerball.com/pb_terms.asp for full terms"
print "This program and its developer are not related in any way to Powerball or the Multistate Lottery Association (MUSL)"
print ""
raw_input("Press enter to exit")


