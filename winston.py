import life360

key = open("C:\\Users\\ek\\Desktop\\key.txt")

username = key.readline()
password = key.readline()
authorization_token = key.readline()

api = life360.Life360()

api.get_authorization(username, password)

circles =  api.get_circles()
print(circles)
'''
id = circles[0]['id']

circle = api.get_circle(id)
'''












































