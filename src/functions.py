def inc(x):
    if isinstance(x, (int, float)):
        return x + 1
    else:
        return "Please use an integer or float input"


def evenodd(n):
    if n == 0:
        return "https://www.britannica.com/story/is-zero-an-even-or-an-odd-number"
    elif isinstance(n, int):
        remainder = n % 2
        if remainder == 0:
            return "even"
        else:
            return "odd"
    else:
        return "yellow"
