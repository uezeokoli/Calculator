# author: Ugonna Ezeokoli
# date: March 2, 2023
# file: tree.py a Python program that implements an abstract data type, tree
# input: takes in put of a postfix string and creates an expression tree from it
# output: outputs the expression tree in various forms depending on function called on the object

from stack import Stack

class BinaryTree:

    def __init__(self,rootObj=None, left = None, right = None): 
        self.key = rootObj
        self.leftChild = right
        self.rightChild = left
        self.order = ""

    # turns left child into its own tree with an assigned root val
    def insertLeft(self,newNodeVal):       
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t

    # turns right child into its own tree with an assigned root val
    def insertRight(self, newNodeVal):      
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t

    #returns the left child
    def getLeftChild(self):     
        return self.leftChild
    
    # returns the right child
    def getRightChild(self):    
        return self.rightChild
    
    # returns the value of the root
    def getRootVal(self):       
        return self.key
    
    # Gives a new value to root
    def setRootVal(self, obj):    
        self.key = obj

    #Overrides str function so that when object can be printed in a specific way
    def __str__(self):      
        if (self.leftChild == None) and (self.rightChild == None):
            return f"{self.key}()()"
        elif self.rightChild == None:
            return f"{self.key}({self.getLeftChild()})()"
        elif self.leftChild == None:
            return f"{self.key}()({self.getRightChild()})"
        else:    
            return f"{self.key}({self.getLeftChild()})({self.getRightChild()})"


class ExpTree(BinaryTree):

    # creates expression tree based on postifix input
    def make_tree(postfix): 
        nodestack = Stack()
        nodes = []

        #Creates a list of indiviudal roots that are not yet connected
        for val in postfix:
            nodes.append(ExpTree(val))
        
        inc = 0
        # increments until length of nodes is reached
        while len(nodes) > inc:
            #if root in node is an operator, it will take the two most recent nodes from nodestack which will turn into children of operator root node
            if (not nodes[inc].key.isnumeric()) and ("." not in nodes[inc].key):
                nodes[inc].leftChild = nodestack.pop()
                nodes[inc].rightChild = nodestack.pop()
                nodestack.push(nodes[inc])
                inc += 1
            #if root in node is a float or number, the node will be added to nodestack
            else:
                nodestack.push(nodes[inc])
                inc += 1
        return nodes[-1]

    # same as inorder function
    def __str__(self):
        return ExpTree.inorder(self)
        
    #traveses the expression tree in root, right, left order
    def preorder(self):
            
            
        # First get the data of node

            self.order = self.key


            # then recur on right child
            if self.rightChild != None:
                self.order = self.order + self.rightChild.preorder()
            # Finally recur on left child
            if self.leftChild != None:
                self.order = self.order + self.leftChild.preorder() 
            
            return self.order
            
    # traverses expression tree in right, left, root order
    def postorder(self):
        if (self.leftChild == None) and (self.rightChild == None):
            return f"{self.key}"
        elif self.rightChild == None:
            return f"{self.key}{self.getLeftChild()}"
        elif self.leftChild == None:
            return f"{self.key}{self.getRightChild()}"
        else:    
            return f"{self.getRightChild().postorder()}{self.getLeftChild().postorder()}{self.key}"
        
    #Travereses expression tree in left, root, right order
    def inorder(self):
        if self.leftChild.leftChild == None:    #recursive base call
            left_val = self.leftChild.key   
        else:
            left_val = self.leftChild
            left_val = left_val.inorder()         # recursion
        if self.rightChild.rightChild == None:      # recursive base call
            right_val = self.rightChild.key
        else:
            right_val = self.rightChild
            right_val = right_val.inorder()     # recursion
        root_val = self.key
        if root_val == "+":
            return f"({right_val}+{left_val})"
        if root_val == "-":
            return f"({right_val}-{left_val})"
        if root_val == "*":
            return f"({right_val}*{left_val})"
        if root_val == "/":
            return f"({right_val}/{left_val})"
        if root_val == "^":
            return f"({right_val}^{left_val})"
        
    # travereses expression tree and evaluates it
    def evaluate(tree):
        if tree.leftChild.leftChild == None:        #recursive base call
            left_val = tree.leftChild.key       
        else:
            left_val = tree.leftChild
            left_val = left_val.evaluate()         # recursion
        if tree.rightChild.rightChild == None:      #recursive base call
            right_val = tree.rightChild.key
        else:
            right_val = tree.rightChild
            right_val = right_val.evaluate()        #recursion
        root_val = tree.key
        if root_val == "+":
            return float(right_val) + float(left_val)
        if root_val == "-":
            return float(right_val) - float(left_val)
        if root_val == "*":
            return float(right_val) * float(left_val)
        if root_val == "/":
            return float(right_val) / float(left_val)
        if root_val == "^":
            return float(right_val) ** float(left_val)


if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
        
        

