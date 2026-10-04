#name = "ugomma mmebo"
#print(name.title())
#print(name.upper())
#print(name.lower())

#CONCATENATING STRINGS
Firstname = "ugomma"
Lastname = "mmebo"
fullname = Firstname + " " + Lastname
#print(fullname)

#print("Hello, " + fullname.title() + "!" + " Lovely to have you here!") #uncheck to run the code

#You can add whitespace or "extra space" before the print result by adding "\t"

print("\t" + fullname.title())

#You can also print names per role instead of in a line

print("\t" + Firstname.title() + "\n" + "\t" + Lastname.title())

#To ensure that no whitespace exists at the right end of a string, use the .rstrip() method.
# for left use .lstrip() and from both sides using .strip()

fav_language = "Python "
fav_language = fav_language.rstrip()
print(fav_language)

fav_food = " Oha "
fav_food = fav_food.strip()
print(fav_food)

#The .strip() method is mostly used to clean up  user input sections

