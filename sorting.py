import random as r
import time as t

def bubble_sort(original_list):
  # Creates new list so that the original, unorganized list is preserved
  new_list = []
  # to store the element that is going to be switched
  memo = 0
  # The following two variables are used to check if the list is still unorganized after a loop.
  unordered = True
  n_unordered_elements = 0

  # This loop clones the original list for preserving purposes
  for i in original_list:
    new_list.append(i)

  while unordered:
    n_unordered_elements = 0
    for i in range(len(new_list)):
      if i != len(new_list) - 1:
        # If the left element is bigger than the right, they are switched
        if new_list[i] > new_list[i+1]:
          memo = new_list[i+1]
          new_list[i+1] = new_list[i]
          new_list[i] = memo
          n_unordered_elements += 1
    # Checks if list is still unorganized. If it still is, the loop continues 
    if n_unordered_elements == 0:
      unordered = False
  return new_list


def selection_sort(original_list):
  new_list = []
  for i in original_list:
    new_list.append(i)

  for w in range(len(new_list)):
    smallest_element = new_list[w]
    smallest_element_index = w
    for i in range(len(new_list)):
      if i >= w:
        if new_list[i] < smallest_element:
          smallest_element = new_list[i]
          smallest_element_index = i
    memo = new_list[w]
    new_list[w] = smallest_element
    new_list[smallest_element_index] = memo
  return new_list


def insertion_sort(original_list):
  print("hi")
      







original_list = [103, 53, 53, 92, 17, 5, -1, 49, 81, 76, 14, 23, 67, 45, 900, 10, 98, 0]
#original_list = [103, 53, 92, 17, 5, -1]
menu = True

print("This is the sorting algorythm tester. To compare the speeds of each sorting algorythm.")

while menu:
  
  print("\n--- Which sorting function you want to use ---")
  print("\n [1] Bubble Sort")
  print(" [2] Selection Sort")
  print(" [3] Insertion Sort")
  print("\n Click enter without typing nothing to generate an unordered list")
  option = input("\nType here:")

  start_time = t.time()
  
  if option == "":
    original_list = []
    size = int(input("Size of your list: "))
    for i in range(size):
      original_list.append(r.randint(1,500))
    print("List generated!")
    
  elif option == "1":
    new_list = bubble_sort(original_list)
    end_time = t.time()
    print("\n" + str(new_list))
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))

  elif option == "2":
    new_list = selection_sort(original_list)
    end_time = t.time()
    print("\n" + str(new_list))
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))

  elif option == "3":
    new_list = insertion_sort(original_list)
    end_time = t.time()
    print("\n" + str(new_list))
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))


