class FileManager:
    def __init__(self, input_path:str, output_path:str):
        self.input_path = input_path
        self.output_path = output_path
        self.input_handler = None
        self.output_handler = None

    def __enter__(self):
        self.output_handler = open(self.output_path, "w", encoding="utf-8")
        self.input_handler = open(self.input_path, "r", encoding="utf-8")
        return (self.input_handler, self.output_handler)

    def __exit__(self, *args):
        self.output_handler.close()
        self.input_handler.close()

    def __str__(self):
        return f"FM<Input:{self.input_path}, Output:{self.output_path}>"

def main():
    """
    Start
    """
    with FileManager("input.txt", "output.txt") as handlers:
        input_handler, output_handler = handlers
        output_handler.write(input_handler.read())
    

if __name__ == "__main__":
    main()
