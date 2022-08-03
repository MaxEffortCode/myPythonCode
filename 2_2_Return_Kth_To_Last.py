from distutils.command.build_scripts import first_line_re
import random
import time


class node_n():
    def __init__(self, value):
        self.next_node = None
        self.value = value


def create_nodes(head, count=0):
    if count < 10:
        head.next_node = node_n(random.randint(0, 50))
        head = head.next_node
        count += 1
        head = create_nodes(head=head, count=count)

    else:
        head.value = None

    return head


def print_linked_list(node):
    if node.value != None:
        time.sleep(1/15)
        print(f"node val: {node.value}")
        print_linked_list(node=node.next_node)


def get_Kth_elem(head_node, kth, count=0):
    if (count <= kth) and (head_node.value != None):
        print(f"going past: {head_node.value} kth: {kth} count: {count}")
        head_node = head_node.next_node
        time.sleep(1/10)
        get_Kth_elem(head_node=head_node, kth=kth, count=count+1)

    if head_node.value == None:
        print("Not found")
        return

    if kth == count:
        print(f"found {kth} element with value; {head_node.value}")
        return head_node.value


if __name__ == "__main__":
    head_node = node_n(1)
    create_nodes(head_node)
    print_linked_list(head_node)
    get_Kth_elem(head_node=head_node, kth=3)
    get_Kth_elem(head_node=head_node, kth=30)
