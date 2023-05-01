with open('wer.txt') as file1, open('wup.txt') as file2:
    codes1 = set(file1.readlines())
    codes2 = set(file2.readlines())

matching_codes = codes2.intersection(codes1)

print("Matching codes:")
print(matching_codes)
#print(codes2)
print(len(codes2))
