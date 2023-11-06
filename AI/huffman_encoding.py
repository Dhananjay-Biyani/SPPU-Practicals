import heapq

# class to create a node 
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""
    
# method to compare the frequency of current node
    def __lt__(self, other):
        return self.freq < other.freq
    
# function to print the huffman code ofr all the symbols recursively by traversing then tree
def printNodes(node, val=""):
    newval = val + node.huff
    if node.left:
        printNodes(node.left, newval)
    if node.right:
        printNodes(node.right, newval)
    else:
        print(f"{node.symbol} -> {newval}")

chars = ["a", "b", "c", "d", "e", "f"]
freqs = [5, 9, 12, 13, 16, 45]
# list to store all the nodes
nodes = []
# converting the chars and frequ into nodes 
for i in range(len(chars)):
    heapq.heappush(nodes, node(freqs[i], chars[i]))

# building the huffman tree
while len(nodes) > 1:

    # sorting the nodes in ascending order based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = "0"
    right.huff = "1"
    # combining two smallest node to create a newnode as their parent
    newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newnode)

printNodes(nodes[0])