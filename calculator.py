# author: Ugonna Ezeokoli
# date: March 2, 2023
# file: calculator.py a Python program that imitates the functionality of a calculator
# input: takes in objects such as stack and ExpTree
# output: Returns the evaluation of the expression given

from stack import Stack
from tree import BinaryTree, ExpTree


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



print("Welcome to Calculator Program!")

# Loop that will not stop until user decides to quit by typing quit or q
while True:
    expression = input("Please enter your expression here. To quit enter 'quit' or 'q':\n").lower()
    if expression == 'q' or expression == "quit":  #This is how user decides to quit 
        print("Goodbye!")
        break
    elif infix_to_postfix(expression) == "invalid":  #Expression will equal invalid if letter in expression and will restart loop
        continue
    else:
        print(calculate(expression))        #Displays the result of expression

# if __name__ == '__main__':
#     # test infix_to_postfix function
#     assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
#     assert infix_to_postfix('5+2*3') == '5 2 3 * +'
#     # test calculate function
#     assert calculate('(5+2)*3') == 21.0
#     assert calculate('5+2*3') == 11.0




