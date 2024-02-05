my_str = " El's favorite "
my_multiline_str = '''Revvin' up your engine
Listen to her howlin' roar
Metal under tension
Beggin' you to touch and go'''

#Print individual letter 
for i in my_multiline_str:
    print(i)
    
print(my_multiline_str[-1]) #[-1] will print the last character of the string
    
# the len function will show the numbers of character in a string
print (len(my_multiline_str))

#.upper and .lower will print the code in all lower or upper case
print(my_str.upper())

#.strip will eliminate unnecessary space
print(my_str.strip())

#.replace('original','new') will replace the old word in a string
print(my_str.replace('favorite','worst enemy'))

#.split will split the string in a specific place
print (my_str.split(","))

#(+""+) will connect 2 strings together
print (my_str+""+ my_multiline_str)

# Format string is another form of concatenation string 
print  (f"I am {my_str}person on the whole wide world")

#escape character (\) will make code runs when theres a (')
print('I\'m el\'s favorite person')