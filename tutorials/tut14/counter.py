class Counter:
    # prefix __ will make the data private
    __count = 0

    def Count(self):
        Counter.__count += 1
        print(Counter.__count)