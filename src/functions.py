def inc(x):
    if isinstance(x, (int, float)):
        return x + 1
    else:
        return "Please use an integer or float input"
