#Name: Shezan Alam
#Email: shezan.alam48@myhunter.cuny.edu
#Date: September 17th, 2019
template = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."
noun = input("Enter a noun: ")
template = template.replace("NOUN", noun)
verb1 = input("Enter a verb: ")
template = template.replace("VERB1", verb1)
verb2 = input("Enter another verb: ")
template = template.replace("VERB2", verb2)
print('\nNew sentence: ')
print(template)
