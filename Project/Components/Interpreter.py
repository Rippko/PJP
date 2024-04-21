class Interpreter:
    def __init__(self, filename: str):
        self.instruction_pointer = 0
        self.stack = []
        self.variables = {}
        self.instructions = []
        
        with open(filename, "r") as file:
            self.instructions = file.readlines()
            self.instructions = [line.strip() for line in self.instructions]

    def interpret(self):
        while self.instruction_pointer != len(self.instructions):
            line = self.instructions[self.instruction_pointer]
            splitted_line = line.split(" ", 1)
            match splitted_line[0]:
                case "add":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 + value1)
                case "sub":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 - value1)
                case "mul":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 * value1)
                case "div":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    if isinstance(value1, float) or isinstance(value2, float):
                        self.stack.append(value2 / value1)
                    self.stack.append(value2 // value1)
                case "mod":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 % value1)
                case "concat":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 + value1)
                case "uminus":
                    self.stack.append(self.stack.pop() * -1)
                case "not":
                    self.stack.append(not self.stack.pop())
                case "and":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 and value1)
                case "or":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 or value1)
                case "gt":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 > value1)
                case "lt":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 < value1)
                case "eq":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 == value1)
                case "lte":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 <= value1)
                case "gte":
                    value1 = self.stack.pop()
                    value2 = self.stack.pop()
                    self.stack.append(value2 >= value1)
                case "itof":
                    self.stack.append(float(self.stack.pop()))
                case "fjmp":
                    if not self.stack.pop():
                        self.instruction_pointer = self.instructions.index(f"label {splitted_line[1]}")
                case "jmp":
                    self.instruction_pointer = self.instructions.index(f"label {splitted_line[1]}")
                case "push":
                    vType, value = splitted_line[1].split(" ", 1)
                    self.stack.append(self.get_value_type(vType,value))
                case "pop":
                    self.stack.pop()
                case "load":
                    self.stack.append(self.variables[splitted_line[1]])
                case "save":
                    vName = splitted_line[1]
                    self.variables[vName] = self.stack.pop()
                case "print":
                    out = []
                    for i in range(int(splitted_line[1])):
                        value = self.stack.pop()
                        if isinstance(value, bool):
                            value = str(value).lower()
                        out.append(str(value))
                    out.reverse()
                    print(f"Output: ", "".join(out))
                case "read":
                    while True:
                        try:
                            value = self.get_value_type(splitted_line[1], input(f"Waiting for {splitted_line[1]} input:"))
                            if splitted_line[1] == "B":
                                value = str(value).lower()
                            self.stack.append(self.get_value_type(splitted_line[1], value))
                            break
                        except Exception:
                            print(f"Invalid input type, expected {splitted_line[1]}")
            self.instruction_pointer += 1
            

    def get_value_type(self, value_type, value):
        match value_type:
            case "I":
                return int(value)
            case "F":
                return float(value)
            case "B":
                return value == "true"
            case "S":
                if value[0] == '"' and value[len(value) - 1] == '"':
                    return value[1:len(value) - 1].strip()
                return value.strip()