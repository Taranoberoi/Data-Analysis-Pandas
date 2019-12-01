# # Solution
# count = 1
# val = ""
# while count <= 10:
#     val = val + str(count)
#     print(val)
#     count = count + 1
# # Solution 2
# for i in range(2, 7):
#     print(''.join(map(str, range(1, i))))
#

# Solution which could not udnerstood.
for i in range(2,7):
    a = ''.join(next(map(str,range(1,i))))
    print(a)