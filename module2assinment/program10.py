def test_numbers(x,y):
    if( x == y or abs(x-y)==5 or (x+y)==5):
        return True
    else:
        return False

print(test_numbers(7,2))
print(test_numbers(3,2))
print(test_numbers(2,2))
print(test_numbers(7,2))
print(test_numbers(27,2))
