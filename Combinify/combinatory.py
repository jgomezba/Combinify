import itertools

class Combinatory:
    """
    A class to generate all possible groupings (permutations or combinations) 
    from a given list of elements, based on specified group size and order significance.

    Attributes:
        elements (list): The list of elements to group.
        group_elements_by (int): The size of each group.
        order_matters (bool): Whether the order in the grouping matters.
    """
    
    def __init__(self, elements: list, group_elements_by: int, order_matters: bool):
        self.elements = elements
        self.group_elements_by = group_elements_by
        self.order_matters = order_matters
        self.number_of_groupings = 0
        self.groups = []

    def get_permutations(self) -> list:
        """
        Generate all permutations of the specified group size where order matters.

        Returns:
            list of tuples: Each tuple is a permutation of the specified group size.
        """
        permutations = list(set(itertools.permutations(self.elements, self.group_elements_by)))
        self.number_of_groupings = len(permutations)
        self.groups = permutations
        return self.groups

    def get_combinations(self) -> list:
        """
        Generate all combinations of the specified group size where order does not matter.

        Returns:
            list of tuples: Each tuple is a combination of the specified group size.
        """
        combinations = list(set(itertools.combinations(self.elements, self.group_elements_by)))
        self.number_of_groupings = len(combinations)
        self.groups = combinations
        return self.groups

    def get_groupings(self) -> list:
        """
        Generate all groupings based on whether order is significant or not.

        Returns:
            list of tuples: The resulting groupings (permutations or combinations).
        """
        if self.order_matters:
            return self.get_permutations()
        else:
            return self.get_combinations()

    def __repr__(self) -> str:
        return f"Found {self.number_of_groupings} possible groups. Groups are:\n{self.groups}"
    