# Madlib Using String concatenation (aka how to put strings together)
# Suppose we want to create  a string that says "subscribe to____"

# youtuber = "Ashis Sardar" #some string variable
#
# # a few ways to do this
# print("Subscribe to " + youtuber)
# # 2nd way
# print("subscribe to {}".format(youtuber))
# # 3rd way
# print(f"Subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = (f"""Computer Programing is {adj}! It makes me so excited all the time because 
I love to {verb1}. Stay hydrated and {verb2} like you are a {famous_person}!""")
print(madlib)
