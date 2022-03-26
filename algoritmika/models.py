

class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        self.token = 'bG9naW46cGFzc3dvcmQ='


user = User(name='Alex', login='login', password='password')

