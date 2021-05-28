from typing import Counter


class Vertex():
    def __init__(self, parent=None , pch = " "):
        self.parent = parent
        self.pch = pch
        self.failureLink = -1
        self.child = [ -1 for _ in range(26)]
        self.go = [ -1 for _ in range( 26 )]
        self.outLink = []
        self.endLink = -1
        self.leaf = False
    def __repr__(self):
        #and chilren {self.child}
        return  f"---------{self.pch}----{self.leaf}------- {self.endLink} -----------having words {self.outLink} ------with failureLink as {self.failureLink} \n"
trie= [Vertex(0)]
def add_string(string):
    currentNode= 0 
    for char in string.lower():

        intValueOfChar= ord(char)- ord('a')
        
        if trie[currentNode].child[intValueOfChar] == -1 :
           trie[currentNode].child[intValueOfChar] = len(trie)
           trie.append(Vertex(currentNode  , char)) 
        currentNode = trie[currentNode].child[intValueOfChar]
    trie[currentNode].outLink.append(string)  
    trie[currentNode].leaf=True
strings= ["his", "her", "she","he"]
for string in strings:
    add_string(string)
def failureLinks(v):
    if trie[v].failureLink == -1:
        if trie[v].parent == 0 or v == 0 :
            trie[v].failureLink = 0 
        else:
            trie[v].failureLink =  getNode(failureLinks(trie[v].parent) , trie[v].pch)
    
    return trie[v].failureLink
def outputLinks(v):
    if trie[v].endLink == -1:
        u = trie[v].failureLink 
        if trie[u].leaf:
            trie[v].endLink = u
        else:
         trie[v].endLink    =  trie[u].failureLink
    
def getNode(node , edgeValue):
     c  = ord(edgeValue) - ord('a')
     if trie[node].go[c] == -1:
         
         if trie[node].child[c] != -1:
             trie[node].go[c] = trie[node].child[c]       
         else:
             if  node == 0  :
                    trie[node].go[c] = 0 
             else:
                 trie[node].go[c] = getNode(failureLinks(node) , edgeValue)
     return trie[node].go[c]    
for v in range(len(trie)):
    failureLinks(v)

for v in range(len(trie)):
    outputLinks(v)

print(trie)
def traverseAhoCTrie(txt):
    #for simplicity i will use only loer case letters
    words=[]
    prepare=set()
    txt = txt.lower()
    currentNode = 0 
    for char in txt:
        c= ord(char) - ord('a')
        print(f"{currentNode} ----------- {char}------{trie[currentNode].leaf}")
        if trie[currentNode].child[c] != -1:
            currentNode = trie[currentNode].child[c]
        else:
            currentNode = trie[currentNode].failureLink
            currentNode = getNode(currentNode , char)
        if trie[currentNode].leaf:
            words.append(trie[currentNode].outLink)
            print("here")
        travel = trie[trie[currentNode].endLink].leaf
        node = trie[currentNode].endLink
        while travel:
            words.append(trie[node].outLink)
            node = trie[node].endLink
            travel = trie[node].leaf
    for x in words:
        for y in x:
            prepare.add(y)
    return prepare    
print(traverseAhoCTrie("ahissher")) 