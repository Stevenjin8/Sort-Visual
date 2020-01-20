from turtle import Turtle, Screen
import time
import random

#setting screen constants
screen = Screen()
screen_height = screen.window_height()-40
screen_width = screen.window_width()-40
screen.tracer(False)

#creates array and array other constants
array = [((random.random())) for _ in range(300)]
array_max = max(array)
array_min = min(array)
bar_width = screen_width//len(array)
bar_height_unit = screen_height//array_max

#creates turtle objects for each bar
turtles = [Turtle() for _ in range(len(array))]

#moves turtles to their corresoponding positions
for i,t in enumerate(turtles):
    t.goto(i*bar_width - screen_width//2,-screen_height//2)
    t.ht()
    
#draws a bar
def draw(t,height, color="black"):
    t.clear()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(bar_width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

#binary insert, not used
def binary_insert(arr, val):
    print(arr)
    if val <= min(arr):
        return 0
    #inserts val into arr where arr is a sorted list
    elif len(arr) <=1:
        return 1
    else:
        midpoint = len(arr)//2
        if val > arr[midpoint]:
            return midpoint + binary_insert(arr[midpoint:], val)
        else:
            return binary_insert(arr[:midpoint], val)

#merges two sorted arrays into one sorted array
def merge(arr1, arr2, index):
    i=0
    for x in arr2:
        if x > max(arr1):
            arr1.append(x)
        else:
            for i in range(i,len(arr1)):#binary serach here?
                if x <= arr1[i]:
                    arr1.insert(i, x)
                    #draws the bars that have changed
                    for x, t in zip(arr1[i:], turtles[index+i:]):
                        draw(t, x*bar_height_unit)
                    screen.update()
                    break
    return arr1

#implements merge recursively
def merge_sort(arr, index=0):
    if len(arr) == 1:
        return arr
    else:
        midpoint = len(arr)//2
        arr1 = arr[:midpoint]
        arr2 = arr[midpoint:]
        
        return merge(merge_sort(arr1, index),merge_sort(arr2, index + midpoint), index)

#draws the initial graph
for t, obj in zip(turtles,array):
    draw(t,obj * bar_height_unit)

#does the thing
d=merge_sort(array)
