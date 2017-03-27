class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class tree(object):
    def __init__(self):
        self.root = None
        
    def insert(self,root,value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value < root.data:
                if root.left is None:
                    root.left = Node(value)
                else:
                     self.insert(root.left,value)
            elif value > root.data:
                if root.right is None:
                    root.right = Node(value)
                else:
                     self.insert(root.right,value)
        return root 
    def delete(self,root,data,parent):
        if root is None:
            return root
        if root.data < data:
            parent = root
            root.right = self.delete(root.right,data,parent)
        elif root.data > data :
            parent = root
            root.left = self.delete(root.left,data,parent)
        else:
            if root is None or root.data != data:
                return False
            elif root.left is None and root.right is None:
                 if data > parent.data:
                     parent.right = None
                     root = None
                 else:
                     parent.left = None
                     root = None
            elif root.left is None:
                if data > parent.data:
                    parent.right = root.right
                    root = parent.right
                else:
                    parent.left = root.right
                    root = parent.left
                    
            elif root.right is None:
                if data > parent.data:
                    parent.right = root.right
                    root = parent.right
                else:
                    parent.left = root.right
                    root = parent.right
            else:
                temp = self.successor(root.right)
                root.data = temp.data
                root.right = self.delete(root.right,temp.data,parent)
        
        return root
            
    def successor(self,root):
        temp = root
        if root.right:
            while temp.left:
                temp = temp.left
        return temp
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
def main():
    Tree = tree()
    l =[50,30,20,40,70,60,80]
    for item in l:
        Tree.insert(Tree.root,item)
    print(Tree.delete(Tree.root,20,None))
    print("inorder after deleting 20:")
    print(Tree.inorder(Tree.root))
    print(Tree.delete(Tree.root,30,None))
    print(Tree.delete(Tree.root,50,None))
    print(Tree.inorder(Tree.root))
    
main()
                
                
                
                    
                
            
