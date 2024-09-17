class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    if user == None or user == "" or group == None or group == "":
        return False
    
    if user in group.get_users():
        return True
    
    for next_group in group.get_groups():
        return is_user_in_group(user, next_group)
    
    return False



    

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1: Basic Functionality
assert is_user_in_group("sub_child_user", parent) == True
assert is_user_in_group("some_other_user", parent) == False
assert is_user_in_group("sub_child_user", child) == True
assert is_user_in_group("sub_child_user", sub_child) == True

## Test Case 2
assert is_user_in_group(None, parent) == False
assert is_user_in_group("sub_child_user", None) == False

## Test Case 3
child.add_user(800)
parent.add_user(543543.543534)
sub_child.add_user("")

assert is_user_in_group(800, parent) == True
assert is_user_in_group(800, child) == True
assert is_user_in_group(800, sub_child) == False

assert is_user_in_group(543543.543534, parent) == True
assert is_user_in_group(543543.543534, child) == False
assert is_user_in_group(543543.543534, sub_child) == False

assert is_user_in_group("", parent) == False
assert is_user_in_group("", child) == False
assert is_user_in_group("", sub_child) == False