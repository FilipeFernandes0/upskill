


def add_password(website, username, password):
    if website not in web:
        web[website] = {}
    web[website][username] = password



def get_password(website, username):
    if website in web and username in web[website]:
        return web[website][username]
    else:
        return "password not found"


web = {}



add_password("example.com", "user1", "password123") 

add_password("example.com", "user2", "abc123") 

add_password("test.com", "testuser", "testpassword") 

print("Password for user1 on example.com:", get_password("example.com", "user1")) 

print("Password for user2 on example.com:", get_password("example.com", "user2")) 

print("Password for testuser on test.com:", get_password("test.com", "testuser")) 

print("Password for user3 on example.com:", get_password("example.com", "user3")) 
print(web)