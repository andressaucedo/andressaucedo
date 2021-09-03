import statistics

food = ['rice', 'beans']  # Part 1
print(food)
food.append('broccoli')  # Part 2
print(food)
food.extend(['bread','pizza'])  # Part 3
print(food)
print(food[:2])  # Part 4
print(food[(len(food) -1)])  # Part 5
breakfast = list("eggs, fruit, orange juice".split(", "))  # Part 6
print(breakfast)
print(len(breakfast))  # Part 7

index = 0   
number_list = []
print("Type 'stop' to end.")
number = input("Enter a floating point number: ")  # Part 8
while 1:
  if number == 'stop':
    break
  else:
    try:
      number = float(number)
      number_list.append(number)
    except ValueError:
      print("Error: invalid input. Enter a number or 'stop' to end.")
          
    print(number_list)
  number = input("Enter a number: ")

list_average = statistics.mean(number_list)
list_min = min(number_list)
list_max = max(number_list)
print(f"Your list is complete.\n\tThe average is: {list_average}\n\tThe minimum value is: {list_min}\n\tThe maximum value is: {list_max}")
