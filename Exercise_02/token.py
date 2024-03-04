class Token():
    def __init__(self, type: str, value):
        self.type = type
        self.value = value

    def __str__(self):
        if self.value:
            return f"{self.type}: {self.value}"
        else:
            return f"{self.type}"