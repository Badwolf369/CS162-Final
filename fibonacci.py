"""Helper function to generate fibonacci numbers."""


def fibonacci(n):
    """Quick function to generate n values of fibonacci."""

    sequence = []

    def iter_fibo(a, b, i=0):
        """Recursive function to generate the fibonacci numbers."""

        # End when you generate n numbers
        if i >= n:
            return
        # Recursively generate then save fibonacci numbers
        sequence.append(b)
        iter_fibo(b, a + b, i + 1)

    # Start the recursion
    iter_fibo(0, 1)
    return sequence
