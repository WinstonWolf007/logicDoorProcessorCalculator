class LogicDoor:
    def logic_or(self, num1, num2):
        if num1 == 1 or num2 == 1:
            return 1
        else:
            return 0

    def logic_and(self, num1, num2):
        if num1 == 1 and num2 == 1:
            return 1
        else:
            return 0

    def logic_xor(self, num1, num2):
        if num1 == 1 and num2 == 0:
            return 1
        elif num1 == 0 and num2 == 1:
            return 1
        else:
            return 0
