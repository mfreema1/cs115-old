def pascal_row(n):
    """computes the list of numbers in a particular row of pascal's triangle"""
    def add_two(lst):
        """adds two numbers in the above row in pascals table, moving one block to the right each time.
        In the end, this returns every number in that row after the initial 1."""
        if len(lst) > 1:
            return [lst[0] + lst[1]] + add_two(lst[1:])
        return lst

    if n == 0:
        return [1]
    return [1] + add_two(pascal_row(n - 1))

def pascal_triangle(n):
    """returns every row up to a given row number in pascal's triangle"""
    if n < 0:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]
