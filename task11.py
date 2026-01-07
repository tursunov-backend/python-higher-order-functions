nums = list(range(1, 21))

juft = filter(lambda x: x % 2 == 0, nums)

kv_juft = map(lambda x: x ** 2, juft)

print(list(kv_juft))
