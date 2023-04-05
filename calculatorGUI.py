# author: Ugonna Ezeokoli
# date: March 2, 2023
# file: calculatorGUI.py a Python program that imitates the functionality of a calculator
# input: Takes in GUI which is responsible for the display of the calculator and takes objects like stack and ExpTree
# output: Displays the calculator and functions with buttons. Also displays the evaluation of the expression entered


from stack import Stack
from tree import BinaryTree, ExpTree
from tkinter import *


def calculator(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')

    # add buttons to the grid
    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

def clickButton(entrybox, value):
    # the function clickButton() is not implemented!!!


    length = len(entrybox.get())

    if '.' in entrybox.get():
        entrybox.delete(0, length)

    if value == 'c':
        entrybox.delete(0, length)
    elif value == '=':
        result = calculate(entrybox.get())
        entrybox.delete(0, length)
        entrybox.insert(0,result)
    elif value != 'c':
        entrybox.insert(length, value)



# Function will return the evaluation of equation given
def calculate(equation):
    postfix = infix_to_postfix(equation).split()   # turns equation from infix to postfix and makes postfix a list 
    tree = ExpTree.make_tree(postfix)       #Turns the postfix into a expression tree
    result = ExpTree.evaluate(tree)     # Traverses through the tree to find evaluation
    return result
    # return result

def infix_to_postfix(infix):
    # This loop makes it so that even if user does not add spaces between operands and operator, space will be added
    for val in infix:
        if (not val.isnumeric()) and (val != " ") and (val != "."):
            infix = infix.replace(val, " " + val + " ")
    infix = infix.split()
    infix = " ".join(infix)

    # Gives precedence to each operator
    worth = {}
    worth["("] = 1
    worth["-"] = 2
    worth["+"] = 2
    worth["*"] = 3
    worth["/"] = 3
    worth["^"] = 4

    opStack = Stack()
    postfixList = []
    elements = infix.split()

    for element in elements:
        if element.isalpha(): # Will say invalid if given any alphabet chars in expression, should only be non-negative floats or integers
            print("Invalid expression")
            return "invalid"
        if element.isnumeric() or ("." in element): # adds to postfix list if a number or float
            postfixList.append(element)
        elif element == '(':       #adds ( to opstack
            opStack.push(element)   
        elif element == ')':    
            topElement = opStack.pop()
            while topElement != '(':    
                postfixList.append(topElement)
                topElement = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (worth[opStack.peek()] >= worth[element]):  # this adds operator from opstack to postfix list if it has more precedence then elemnent 
                  postfixList.append(opStack.pop())
            opStack.push(element)   # adds element operator to opstack 

    while not opStack.isEmpty():    #Adds the rest of operations until stack is empty
        postfixList.append(opStack.pop())   
    postfix =  " ".join(postfixList)
    return postfix
    
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()