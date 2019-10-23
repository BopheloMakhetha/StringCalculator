import re

class Calculator():

    def add(self, input_string):
        if not input_string:
            return 0
        if input_string.isdigit() and int(input_string) > 0:
            return int(input_string)
        input_list = self.extract_list(input_string)
        return self.sum_list(input_list)

    def sum_list(self, input_list):
        total = 0
        negatives = []
        for num in input_list:
            num = int(num)
            if num < 0:
                negatives.append(num)
            if num > 1000 or num < 0:
                continue
            total += int(num)
        if len(negatives) > 0:
            raise Exception("negatives not allowed " + str(negatives))
        return total

    def extract_list(self, input_string):
        if input_string[0:2] == "//":
            input_string = input_string.split("\n")[1]
        return re.split("[^0-9-]+", input_string)