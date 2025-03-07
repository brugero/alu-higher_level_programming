class MyList(list):
    """A subclass of list with a method to print sorted elements."""
    
    def print_sorted(self):
        """Prints the list elements in ascending order without modifying the original list."""
        print(sorted(self))
