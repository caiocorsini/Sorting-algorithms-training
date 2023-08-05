import random as r
import time as t


def bubble_sort(original_list):

  # Creates new list so that the original, unorganized list is preserved
  new_list = []
  for i in original_list:
    new_list.append(i)
    
  # Checks if list is still unorganized. If it still is, the loop continues
  unordered = True
  while unordered:
    unordered = False
    for i in range(len(new_list)):
      if i != len(new_list) - 1:
        if new_list[i] > new_list[i+1]:
          # Switches elements
          new_list[i],new_list[i+1] = new_list[i+1],new_list[i]
          unordered = True
  return new_list


def selection_sort(original_list):

  # Creates new list so that the original, unorganized list is preserved
  new_list = []
  for i in original_list:
    new_list.append(i)

  for w in range(len(new_list)):
    smallest_element = new_list[w]
    smallest_element_index = w
    for i in range(len(new_list)):
      # Condition so that already sorted part is skipped from iteration
      if i >= w:
        if new_list[i] < smallest_element:
          smallest_element = new_list[i]
          smallest_element_index = i
    # Switches elements between unsorted and sorted lists
    new_list[w] , new_list[smallest_element_index] = smallest_element , new_list[w]
  return new_list



def insertion_sort(original_list):

  # Creates new list so that the original, unorganized list is preserved
  new_list = []
  for i in original_list:
    new_list.append(i)
    
  for i in range(len(new_list)):
    # There are no elements at the left of index zero, so this condition is needed.
    if i != 0:
      if new_list[i] < new_list[i-1]:
        unordered = True
        # Switches elements
        new_list[i] , new_list[i-1] = new_list[i-1] , new_list[i]
        # Continues iterating backwards as long as the sorted slice of the list is still unsorted
        
        while unordered:
          unordered = False
          # Iterates backwards to insert the element in its correct position
          for j in range(i,0,-1):
            if new_list[j] < new_list[j-1]:
              unordered = True
              # Switches elements
              new_list[j] , new_list[j-1] = new_list[j-1], new_list[j]
  return new_list



def merge_sort(original_list):
    def merge(list1,list2):
        # this section merges the splitted parts of the original list
        # This function only works as long as both lists are sorted
        # i is the pointer of list1. j is the pointer of list2
        merged = []
        i,j = 0,0

        while i < len(list1) and j < len(list2):
            # First it compares elements from index zero
            # Whoever is the smallest gets its pointer to move one element while the other pointer stays in the same place
            # The respective elements from each pointer positions are compared
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        # 'Extend' is a built-in Python function that appends elements from one list into another
        # Here, I am adding all the remaining elements from the list that wasn't fully iterated
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged




    if len(original_list) <= 1:
        return original_list

    # Separating by the middle. Has to be // in case of odd numbered lengths.
    left = original_list[:len(original_list) // 2]
    right = original_list[len(original_list) // 2:]

    # Recursion is required for merge sorting. The function calls itself.
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# Simple function to show sorted list
# It is not worth it to print such huge lists in the terminal, so they are not printed when they are longer than 50 elements.
def show_results(result):
  if len(result) <= 50:
    print("\n" + str(new_list))
  else:
    print("This list is very long.")


original_list = [3,7,8,8,4,2,6,1]
original_list_clone = []
#original_list = [103, 53, 92, 17, 5, -1]
menu = True

print("This is the sorting algorythm tester. To compare the speeds of each sorting algorythm.")

while menu:
  
  print("\n--- Which sorting function you want to use ---")
  print("\n [1] Bubble Sort")
  print(" [2] Selection Sort")
  print(" [3] Insertion Sort")
  print(" [4] Merge Sort")
  print(" [9] Generate random list")
  print("\nClick enter without typing nothing to generate an unordered list")
  option = input("\nType here:")

  
  if option == "9":
    original_list = []
    size = int(input("Size of your list: "))
    min = int(input("Smaller possible number: "))
    max = int(input("Biggest possible number: "))
    for i in range(size):
      original_list.append(r.randint(min,max))
    print("List generated!")
    
  elif option == "1":
    start_time = t.time()
    new_list = bubble_sort(original_list)
    end_time = t.time()
    show_results(new_list)
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))

  elif option == "2":
    start_time = t.time()
    new_list = selection_sort(original_list)
    end_time = t.time()
    show_results(new_list)
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))

  elif option == "3":
    start_time = t.time()
    new_list = insertion_sort(original_list)
    end_time = t.time()
    show_results(new_list)
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))

  elif option == "4":
    # Loop for preserving original list
    # Hasn't been done in the same way as the other functions due to the recursivity of Merge Sort
    for i in range(len(original_list)):
        original_list_clone.append(original_list[i])
    start_time = t.time()
    new_list = merge_sort(original_list)
    end_time = t.time()
    for i in range(len(original_list_clone)):
        original_list.append(original_list_clone[i])
    show_results(new_list)
    print("\nExecution time (in seconds) = " + str(round(end_time - start_time, 3)))
