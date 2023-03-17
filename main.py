# try: (Something that might cause an exception)
# except: (Do this if there WAS an exception)
# else: (Do this if there were NO exception)
# finally: (Do this no matter what happens)

# File Not Found
try:
    file = open("test.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("test.txt", "w")
    file.write("New test file.")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed!")

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["some_wrong_key"]

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)
