class FileManager:
    READ_MODE = "r"
    WRITE_MODE = "w"
    ENCODING = "utf-8"
    DEFAULT_INPUT = "input.txt"
    DEFAULT_OUTPUT = "output.txt"
    
    def __init__(self, input_path:str = "input.txt", output_path:str= "output.txt"):
        self.input_path = input_path
        self.output_path = output_path
        self.input_handler = None
        self.output_handler = None

    @classmethod
    def creator(cls):
        open(cls.DEFAULT_INPUT, cls.WRITE_MODE)

    def __enter__(self):
        self.input_handler = open(self.input_path, self.READ_MODE, encoding=self.ENCODING)
        self.output_handler = open(self.output_path, self.WRITE_MODE, encoding=self.ENCODING)
        return (self.input_handler, self.output_handler)

    def __exit__(self, *args):
        self.output_handler.close()
        self.input_handler.close()

FileManager.creator() 
with FileManager(input_path="input.txt", output_path="output.txt") as handlers:
    inp, outp = handlers

print("ALLES")
    
    