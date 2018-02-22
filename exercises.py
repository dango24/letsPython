def numbers_are_different(*args):
    nums = set()

    for value in args:
        if value in nums:
            return False
        else:
            nums.add(value)

    return True

def create_all_possible_strings(letters):
    return create_all_possible_strings_gil(letters, 0, "")


def create_all_possible_strings_gil(letters, index, str):
    if index == len(letters):
        print str
    elif index < len(letters):
        create_all_possible_strings_gil(letters, index+1, str + letters[index])
        create_all_possible_strings_gil(letters, index+1, str)


# print(numbers_are_different(1,2,3,6,4,5,6,7,8,9))
# create_all_possible_strings(['a', 'b', 'c']) #, 'e', 'i', 'o', 'u']))

oren_efes = lambda name: "Oren mega efes: {0}".format(name)

print(oren_efes("Tal"))