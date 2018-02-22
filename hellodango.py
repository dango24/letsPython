def add_numbers(a, b):
    if a and b:
        return a + b

# print(int(add_numbers(2, 5)))

# print("hello".capitalize())
# print('hello'.replace("e", 'a'))
# print("hello".isalpha())
# print('123'.isdigit())
# print("lets,see,what,you,got".split(","))

# first_name = "Dango"
# last_name = "Golan"

# print("Let's dance Mr. {0} {1}".format(first_name, last_name))

# oren = 5 + 10
# dango = 5 + 2 + 8
#
# str2 = "dangoooo"
# # print(oren)
#
# if oren == dango:
#     print("Badok oren is None")
# else:
#     print("En matav".count())
#
# list = [43, 11 ,38 ,31]
# list.append(32)
#
# del list[1]
#
# list.append(32432)
#
# shorterList = list[1:-1]
#
# print(list)
# print(shorterList)
#
# if 32 in list:
#     print("YiPika ye")
#
# if oren:
#     print(len('Number is well defined'))

# str = 'Hello'
#
# print(str[-2:])
#
# def string_bits(str):
#     newString = ""
#
#     for index in range(0, len(str), 2):
#         newString = str[index]
#
#     return newString

# string_bits(str)
#
# def last2(str):
#     count = 0
#
#     if (len(str) < 2):
#         return 0
#
#     subString = str[-2:]
#
#     for index in range(len(str) - 2):
#         if (str[index:index + 2] == subString):
#             count +=1
#
#     return count
#
#
# def rotate_left(nums):
#     tmp = nums[-1]
#
#     for i in range(len(nums) - 1, 0, -1):
#         nums[i] = nums[i - 1]
#
#     nums[0] = tmp
#     return nums
#
#
# print(rotate_left([1, 2, 3]))


def make_bricks(small, big, goal):
    if goal == 0:
        return True
    elif goal < 0:
        return False
    elif big > 0 and big*5 >= goal and goal > 5:
        return make_bricks(small, big - big/5, goal - (goal/5)*5)
    elif big > 0 and big*5 <= goal:
        return make_bricks(small, 0, goal - big*5)
    elif small > 0 and small >= goal:
        return make_bricks(small-goal, big, 0)
    elif small > 0 and big > 0:
        return make_bricks(small-1, big, goal - 1) or make_bricks(small, big-1, goal - 5)
    elif small > 0:
        return make_bricks(small-1, big, goal - 1)
    elif big > 0:
        return make_bricks(small, big-1, goal - 5)
    else:
        return False


print(make_bricks(2, 1000000, 100003))


def make_chocolate(small, big, goal):
    if goal < 0:
        return -1
    elif big > 0 and big * 5 <= goal:
        return make_chocolate(small, 0, goal - big * 5)
    elif big > 0 and goal >= 5 and big * 5 > goal:
        totalBig = goal / 5
        return make_chocolate(small, big - totalBig, goal - 5 * totalBig)
    elif goal <= small:
        return goal
    else:
        return -1

# make_chocolate(5, 4, 9)


map = {
    "reality": "is only an illusion",
    "mind": "is everything"
}

try:
    num = 3 + map["mind"]
    print(map["dango"])
except KeyError, e:
    print("KeyError: {0}".format(e))
except TypeError, e:
    print("TypeError: {0}".format(e))
except Exception, e:
    print("Exception: {0}".format(e))


def add_student(name, s_id=2):
    print "Student name: {0}, id: {1}".format(name, s_id)


add_student(name="dango", s_id=321)

def python_stuff(name, **args):
    print(name)
    print(args["mind"], args["reality"])


python_stuff("dango", reality="is only an illusion", mind="is everything")


def python_stuff2(name, *args):
    print(name)

    for value in args:
        print(value)


print(python_stuff2("dango", 1 ,2 ,3))


