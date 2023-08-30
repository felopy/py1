def longest_increment(num):
    if not num:
        return []

    longest = []
    current = [num[0]]

    for i in range(1, len(num)):
        if num[i] == num[i - 1] + 1:
            current.append(num[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [num[i]]

    if len(current) > len(longest):
        longest = current

    return longest

input_str = input("Enter a sequence of numbers separated by spaces: ")
inputlist = [int(x) for x in input_str.split(",")]

result = longest_increment(inputlist)
print("Longest increment:", result)

