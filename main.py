
db_password = "mySuperSecretPassword123"
def add_user(username, user_list=[]):
    user_list.append(username)
    return user_list

users1 = add_user("user_a")
users2 = add_user("user_b")
