# Write a function that counts the number of people who were born later than a given date.
# For that we will use Binary Search Tree (BST) to store the people's birthdays.
# The Person class is already implemented for you.
# You need to finish the implementation of the BinarySearchTree class.
# By implementing:
# - The _insert function that will insert a person into the BST.
# - The count_later function that will count the number of people who were born later than a given date.
#

import datetime
import random


class Person:
    def __init__(self, name: str, birthday: datetime.date):
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f"{self.name} {self.birthday}"

    def __lt__(self, other): # less than
        return self.birthday < other.birthday 

    def __gt__(self, other):
        return self.birthday > other.birthday # greater than

    def __eq__(self, other):
        return self.birthday == other.birthday

    def __le__(self, other): # less equal
        return self.birthday <= other.birthday

    def __ge__(self, other): # greater equal
        return self.birthday >= other.birthday

    def __ne__(self, other):
        return self.birthday != other.birthday


class BinaryTreeNode:
    def __init__(self, data: Person):
        self.data = data  # type: Person
        self.left = None
        self.right = None
        # This is a small hint for the possible solution :)
        # This will store the number of nodes in the subtree rooted at this node
        self.count_in_subtree = 1


# Binary Search Tree (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # TODO: Implement the _insert function
    # Note: if we are trying to insert a person with the same birthday, we should insert it.
    def _insert(self, root, value: Person):
        if root is None:
            return BinaryTreeNode(value)
        
        if value < root.data:
            root.left = self._insert(root.left, value)
        
        else:
            root.right = self._insert(root.right, value)
        # number of nodes in the tree, number of nodes in each subtree
        root.count_in_subtree = 1 + (root.left.count_in_subtree if root.left else 0) + (root.right.count_in_subtree if root.right else 0) 

        return root
        

    # Note: if we are trying to insert a person with the same birthday, we should insert it.
    def insert(self, value: Person):
        self.root = self._insert(self.root, value)


    # TODO: Implement the count_later function
    # Small hint: take a look at count_in_subtree field in the BinaryTreeNode class, can we reuse it somehow for your problem?
    def count_later(self, value: datetime.date):
        return self._count_later(self.root, value)
    
    def _count_later(self, root, value):
        if root is None:
            return 0

        if root.data.birthday > value: #later
            return (root.count_in_subtree - (root.left.count_in_subtree if root.left else 0)) + self._count_later(root.left, value)
        else: # if earlier -> go to later
            return self._count_later(root.right, value)



def SetupPeople(extra_data=0):
    people = [
        Person("Alice", datetime.date(year=2000, month=1, day=1)),
        Person("Bob", datetime.date(year=2000, month=2, day=2)),
        Person("Charlie", datetime.date(year=2000, month=11, day=3)),
        Person("David", datetime.date(year=2002, month=1, day=4)),
        Person("Eve", datetime.date(year=1999, month=1, day=5)),
        Person("Frank", datetime.date(year=2000, month=6, day=28)),
    ]

    # Add some random people
    for iteration in range(extra_data):
        day = random.randint(1, 28)  # Let's assume all months have 28 days
        month = random.randint(1, 12)
        year = random.randint(1900, 2024)
        date = datetime.date(year=year, month=month, day=day)
        name = f"Person_{iteration}"
        people.append(Person(name, date))

    return people


def Test(people):
    random_dates = [
        datetime.date(year=2000, month=1, day=1),
        datetime.date(year=2000, month=1, day=4),
        datetime.date(year=2000, month=11, day=5),
        datetime.date(year=2000, month=6, day=28),
        datetime.date(year=1999, month=1, day=1),
        datetime.date(year=1900, month=1, day=1),
        datetime.date(year=2024, month=12, day=28),
    ]

    for iteration in range(100):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1900, 2024)
        date = datetime.date(year=year, month=month, day=day)
        random_dates.append(date)

    # Modify if needed
    bst = BinarySearchTree()
    for person in people:
        bst.insert(person)

    for date in random_dates:
        actual = bst.count_later(date)
        expected = sum(1 for person in people if person.birthday > date) # O(n)
        assert actual == expected, f"Expected {expected}, but got {actual} for date {date}"


def main():
    sample_size = [0, 10, 100, 10000, 100000]
    for size in sample_size:
        people = SetupPeople(size)
        start_time = datetime.datetime.now()
        Test(people)
        end_time = datetime.datetime.now()
        print(f"Test with {size} people took: {end_time - start_time}")

    print("\033[92mAll tests passed\033[0m")


if __name__ == "__main__":
    main()

# Task 3. Name: