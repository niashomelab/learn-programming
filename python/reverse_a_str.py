# TITLE: Reverse a string

class Stack:
    def __init__(self):
        self.items = [] # create a empty list for the stack

    def is_empty(self):
        # check if the stack is empty
        return self.items == []

    def push(self, item):
        # add items to the stack
        self.items.append(item)

    def pop(self):
        # remove the item from the stack
        return self.items.pop()

    def peek(self):
        # show the last item in the stack
        last = len(self.items)-1 # 1st item [0], then the last item = [len - 1]
        return self.items[last]

    def size(self):
        # check the size of the stack; How many items?
        return len(self.items)


stack = Stack() # create a new stack

for char in "Hello":
    # push every single character in the word "Hello" in to the stack
    stack.push(char)


reversed_string = "" # result; still empty


for i in range(len(stack.items)):
    # print the result
    reversed_string += stack.pop() # add every single word from the stack to empty string "reversed_string"


print(reversed_string)
print("\nSize of the stack: {}".format(stack.size()))
