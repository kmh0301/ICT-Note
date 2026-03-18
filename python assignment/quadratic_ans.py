print("Please input a:")
a = float(input())
print("Please input b:")
b = float(input())
print("Please input c:")
c = float(input())

# 計算判別式 (Discriminant)
delta = b**2 - 4*a*c

if delta > 0:
    # 使用 ** 0.5 計算平方根
    x1 = (-b + (delta ** 0.5)) / (2*a)
    x2 = (-b - (delta ** 0.5)) / (2*a)
    print(f"Two real roots: {x1} and {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"One real root: {x}")
else:
    print("No real roots")



# #print("Please input a:")
# a = float(input())
# print("Please input b:")
# b = float(input())
# print("Please input c:")
# c = float(input())

# # 在下方編寫判別式計算與 if 判斷邏輯
# Delta = b**2-4*a*c
# # 提示：使用 ** 0.5 來計算平方根
# x1 = (-b+(Delta)**0.5)/2*a
# x2 = (-b-(Delta)**0.5)/2*a

# if (Delta > 0):
#     print('Two real roots: ' +str(x1)+' and '+str(x2))
# elif (Delta == 0 ):
#     print('One real root: ' +str(x1))
# else : 
#     print("No real roots")

