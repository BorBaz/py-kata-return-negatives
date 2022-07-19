# My case
def make_negative(number):
    return_value = number

    if (return_value > 0):
        return_value = return_value * -1
    return return_value


# Best case
def make_negative_bc(number):
    return -abs(number)


# Test
print(make_negative(4))
print(make_negative(45))
print(make_negative(-1))
print(make_negative(0))
