USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(15)]

class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    
def bad_usage_of_iteration(dbrows) -> list:
    """A bad case (non-pythonic) of creating ´´Úser´´ from DB rows"""
    return [User(row[0], row[1], row[2]) for row in dbrows]

def good_example_of_iteration(dbrows) -> list:
    """Create User from DB rows"""
    return[User(user_id, first_name, last_name) for (user_id, first_name, last_name) in dbrows]

# results_bad = bad_usage_of_iteration(USERS)
# print(results_bad)
results_good = good_example_of_iteration(USERS[0:2])
print(results_good[0].user_id)
print(results_good[0].first_name)
print(results_good[0].last_name)

def show_user_first_name(user: list, position: int) -> str:
    print("user name {0}".format(list(user[position])[1]))

show_user_first_name(USERS, 10)

print(list(USERS[0])[1])
for u, f, l in USERS:
    print(u)