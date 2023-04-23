class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as f:
            f.write(msg + "\n")
        super().__init__(msg)

try:
    # some code that might raise CustomException
    raise CustomException("An error occurred")
except CustomException as e:
    print("An error occurred:", e.msg)

