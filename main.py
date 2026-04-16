# 1-mashq
class Auth:
    def __init__(self):
        self.tokens = {}

    def login(self, user):
        token = user + "_token"
        self.tokens[token] = user
        return token
# 2-mashq
class Permission:
    def check(self, role):
        return role == "admin"
# 3-mashq
class Audit:
    def log(self, action):
        print("LOG:", action)
# 4-mashq
class Tenant:
    def __init__(self, name):
        self.name = name
        self.data = []
# 5-mashq
class App:
    def __init__(self):
        self.users = []

    def register(self, name):
        self.users.append(name)

    def list_users(self):
        return self.users
