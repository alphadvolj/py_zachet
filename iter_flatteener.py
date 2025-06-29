class iter_flatteener:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, list):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration

nested_list = [1, [2, [3, 4], 5], 6]
flat = iter_flatteener(nested_list)
for num in flat:
    print(num)
