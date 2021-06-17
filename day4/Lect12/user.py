class User:
    tablename = "Users"
    def __init__(self, login:str, password_hash:str):
        self.login = login
        self.password_hash = password_hash

    def __str__(self):
        return f"User:<Login:{self.login}, PasswordHash:{self.password_hash}>"

    @staticmethod
    def passw_ecnoder(password:str) -> str:
        """
        Шифрование пароля password
        """
        return password[::-1] * 5 + password[::-2] * 3 + password[3:]

pswd = User.passw_ecnoder(
    password = input()
)

u = User(login="admin", password_hash=pswd)
print(u)