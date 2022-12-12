from queue import Queue


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.end = False

    def __str__(self):
        return f"{self.value}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, astring):
        node = self.root
        for c in astring:
            if c in node.children:
                node = node.children[c]
            else:
                node.children.update({c: TrieNode(c)})
                node = node.children[c]
        node.end = True

    def level_traversal(self):
        aqueue = Queue()
        aqueue.put(self.root)
        while not aqueue.empty():
            node = aqueue.get()
            print(node)
            for c in node.children:
                aqueue.put(node.children[c])

    def search(self, string):
        node = self.root
        for c in string:
            if c in node.children:
                node = node.children[c]
            else:
                print(f"{string} not in Trie")
                return False
        if node.end == True:
            print("String exists")
            return True
        else:
            print(f"{string} not in Trie")
            return False

    def delete_string(self, string):
        node = self.root
        node_to_del = node
        for c in string:
            if c in node.children:
                if len(node.children) > 1 or node.end == True:
                    node_to_del = node
                    char_to_del = c
                    node = node.children[c]
                else:
                    node = node.children[c]
            else:
                print(f"{string} not in Trie")
                return False
        if node.end == True:
            if node.children:
                node.end = False
                print('node end switched to False')
            else:
                print("deleting string")
                node_to_del.children.pop(char_to_del)
            return True
        else:
            print(f"{string} not in Trie")
            return False


atrie = Trie()

atrie.insert('cat')
atrie.insert('cats')
atrie.insert('car')
atrie.insert('coat')
atrie.level_traversal()
atrie.search("co")
# atrie.delete_string('cat')
atrie.search("cat")
atrie.level_traversal()
atrie.delete_string('cats')
atrie.level_traversal()
