pokemon = tuple((  # HW part 1
  'pikachu',
  'charmander',
  'bulbasaur'
  ))

print(pokemon[1])  # HW part 2
starter1 = pokemon[0]
starter2 = pokemon[1]
starter3 = pokemon[2]

name_letters = tuple(('A','n','d','r','e','s')) #HW part 3

i=0
search_char = ('i')  # The letter that will get searched in the following loop.
letter_flag = bool(False)

for i in range((len(name_letters)-1)):  # HW part 4
  if search_char in name_letters[i]:
    letter_flag = True
    index = i

if letter_flag == True:  
  print("The '%s' exists in %s at index %d." %(search_char, name_letters,index))
else:
   if letter_flag == False:
        print(f"The letter '{search_char}' does not exist in {name_letters}.")

  # Hw part 5
for x in range(2,11):
  print(x)
  

x = 2  # HW part 6
while x < 11:
  print(x)
  x += 1
  

x = 0  # HW part 7
simple_string = "This is a simple string"
for x in range(len(simple_string)):
  print(simple_string[x], end = '')
print()

tuple_iterate = tuple(("This","is","a","simple","set"))  # HW part 8
tup_length = len(tuple_iterate)
for j in range(tup_length):
  for k in range(3):
    print(tuple_iterate[j],end = ' ')
  print()