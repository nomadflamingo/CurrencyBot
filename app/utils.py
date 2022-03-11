def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
