text = ["apple", "34", "banana", "100", "abc", "75"]

nums = filter( lambda x: x.isdigit(), text)

print(list(nums))