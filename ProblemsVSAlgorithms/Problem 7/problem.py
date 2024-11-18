## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode("root handler")

    def insert(self, path, handler):
        path_parts = path.split('/')
        current_node = self.root

        for path_part in path_parts:
            current_node.insert(path_part)
            current_node = current_node.children[path_part]

        current_node.handler = handler


    def find(self, path):

        if path == "/":
            return self.root.handler
        
        if path.endswith('/'):
            path = path[:-1]

        path_parts = path.split('/')
        current_node = self.root

        for path_part in path_parts:

            if path_part in current_node.children:
                current_node = current_node.children[path_part]
            else:
                return None
        
        return current_node.handler

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, not_found_handler = "404 Not Found"):
        self.router = RouteTrie()
        self.not_found = not_found_handler
        
    def add_handler(self, path, handler):
        self.router.insert(path, handler)
        
    def lookup(self, path):
        handler = self.router.find(path)

        if handler == None:
            return self.not_found
        
        return handler

## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one