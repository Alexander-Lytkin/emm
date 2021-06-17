class A:
    word = "AAAAAAAAA"
    def say(self):
        print(self.word)

class B(A):
    word = "BBBBBBBBB"

def main():
    """
    """
    b = B()
    b.say()

if __name__ == "__main__":
    main()