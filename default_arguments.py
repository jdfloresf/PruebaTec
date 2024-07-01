class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        next_value = self.current
        self.current += 2
        return next_value


class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        next_value = self.current
        self.current += 2
        return next_value


def print_from_stream(n, stream=EvenStream()):

    for _ in range(n):
        print(stream.get_next())


n = int(input())

for _ in range(n):
    data = input().split()

    stream_name = data[0]
    n = int(data[1])
    
    if stream_name == "even":
        print_from_stream(n)
    
    elif stream_name == "odd":
        print_from_stream(n, OddStream())
