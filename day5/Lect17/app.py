from models.user import User


def main():
    """Start."""
    # u = User(login="Bob", password="adhjoaskdj12312", about="About Bob")
    # print(u.login, u.about, u)
    # #u.save()

    # users = [
    #     +,
    #     User(login="Derek", password="Derekadhjoaskdj12312", about="About Derek"),
    #     User(login="Josh", password="Joshadhjoaskdj12312", about="About Josh"),
    # ]
    # # print(users)

    # for u in users:
    #     u.save()

    users = User.all()  # [User(), User(),...]
    print(users)


if __name__ == "__main__":
    main()
