#ten program się wita i pyta o imię

print('Hello')
print('What is your name?') #zapytaj o imię
myName = input() #wprowadza imię
print('it is good to meet you,' + myName)
print('The length of your name is:')
print(len(myName)) #pisze ile liter ma imię
print('What is your age?') #zapytaj o wiek
myAge = input() #wprowadza wiek
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
