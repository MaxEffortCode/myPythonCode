
import random
import time

rand_arr = []
for x in range(200):
    rand_arr.append(random.randrange(9))

class node_n():
    next = None
    prev = None
    value = None



def fill_node_list(head): 
    node = head
    head.next = node_n()
    head.value = rand_arr[0]
    head.next.prev = head
    node = head.next
    
    
    for x in range(len(rand_arr)):
        node.value = rand_arr[x]
        node.next = node_n()
        node.next.prev = node
        node.prev.next = node
        node = node.next
    
    return head

def print_node_list(head_node):
    head = head_node
    if (head_node == None ) or (head_node.next == None):
        print("empty_list")
        return("empty list")
        
    while head_node.next != None:
        print(head_node.value)
        head_node = head_node.next

def del_duplicates_in_node_list(head):
    if head == None or head.next == None:
        return("empty list")
    
    buff_list = []
    cur_node = head
    while cur_node.value != None:
        print(f"\ncur node = {cur_node.value}")
        
        if cur_node.value in buff_list:
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
            print(f"\ndeleting node = {cur_node.value}")
            print(f"prev node = {cur_node.prev.value} prev node next = {cur_node.prev.next.value}")
            print(f"next node = {cur_node.next.value} next node prev = {cur_node.next.prev.value}")
            
            cur_node = cur_node.next
            
            
        else:
            if cur_node.prev != None:
               # print(f"\nsaving node = {cur_node.value}")
                #print(f"prev node = {cur_node.prev.value} next node = {cur_node.next.value}")
                pass

            buff_list.append(cur_node.value)
            cur_node = cur_node.next

    for item in buff_list:
        print(f"buff list = {item}")
    
    while cur_node.prev != None:
        #print(f"back node = {cur_node.prev.value}")
        cur_node = cur_node.prev
    return cur_node

head = node_n()
print("printing empty head")
print_node_list(head)

print("filling unsorted list")
head_node = fill_node_list(head)

print("printing filled node list")
print_node_list(head_node)

print("deleting duplicates")
head = del_duplicates_in_node_list(head_node)

print("unduplicated list")
print_node_list(head)