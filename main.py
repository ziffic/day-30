# ------------------------------------------------------------------------------
# try: (Something that might cause an exception)
# except: (Do this if there WAS an exception)
# else: (Do this if there were NO exception)
# finally: (Do this no matter what happens)
# ------------------------------------------------------------------------------

# File Not Found
# try:
#     file = open("test.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("test.txt", "w")
#     file.write("New test file.")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up!")
#     file.close()
#     print("File was closed!")

# ------------------------------------------------------------------------------
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

# ------------------------------------------------------------------------------
# Code Challenge #1
# ------------------------------------------------------------------------------

# fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)

# ------------------------------------------------------------------------------
# Code Challenge #2
# ------------------------------------------------------------------------------
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes)
