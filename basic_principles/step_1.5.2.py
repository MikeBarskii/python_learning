# https://stepik.org/lesson/24461/step/9?unit=6767
class Buffer:
    def __init__(self):
        self.sequence = []

    def add(self, *a):
        for value in a:
            self.sequence.append(value)
            if len(self.sequence) == 5:
                print(self.sum_buffer_elements())
                self.sequence.clear()

    def get_current_part(self):
        return self.sequence

    def sum_buffer_elements(self):
        sum_of_sequence = 0
        for value in self.sequence:
            sum_of_sequence += value
        return sum_of_sequence


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # return [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – output the sum of the first five elements
print(buf.get_current_part())  # return [6]
buf.add(7, 8, 9, 10)  # print(40) – output the sum of the second five elements
print(buf.get_current_part())  # return []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – output of the amounts of the third and fourth five
print(buf.get_current_part())  # return [1]
