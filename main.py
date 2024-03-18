# all_S = [1, 2, 3, 4, 5, "Hello World!", "Hi Bro!"]  # list

# servis = iter(all_S)    # iterator

# print(next(servis))
# print(next(servis))
# print(next(servis))
# print(next(servis))
# print(next(servis))
# print(next(servis))
# print(next(servis))

##################################################################

# try:
#     print(next(servis))
#     print(next(servis))
#     print(next(servis))
#     print(next(servis))
#     print(next(servis))
#     print(next(servis))
#     print(next(servis))
# except StopIteration:
#     print("StopIteration <- so'zini qaytaradi")

##################################################################

# try:
#     while 1:
#         print(next(servis))
# except StopIteration:
#     print("StopIteration <- so'zini qaytaradi")

##################################################################

# class PowTwo:
#     def __init__(self, limit=0):
#         self.limit = limit
#
#     def __iter__(self):
#         self.n = 1
#         return self
#
#     def __next__(self):
#         if self.n <= self.limit:
#             pow_number = 2 ** self.n
#             self.n += 1
#             return pow_number
#         else:
#             raise StopIteration
#
#
# numbers = PowTwo(5)
# iterator = iter(numbers)
#
# try:
#     while True:
#         print(next(iterator))
#
# except StopIteration:
#     print("Xatolik turi : StopIteration")

##################################################################

# import timeit
#
#
# def generators():
#     for x in range(10_000):
#         yield x
#
#
# def generator_return():
#     temp = []
#     for i in generators():
#         if i == 1_000:
#             break
#     return temp
#
#
# def for_loop():
#     temp_list: list[int] = []
#     for x in range(10_000):
#         temp_list.append(x)
#
#     return temp_list
#
#
# if __name__ == '__main__':
#     time_for = timeit.timeit(stmt=for_loop, number=10_000)
#     time_yield = timeit.timeit(stmt=generators, number=10_000)
#
#     print("For loop", round(time_for, 5))
#     print("Yield   ", round(time_yield, 5))
#     faster = (time_for / time_yield) * 100
#     print(f"{(round(faster, 2))} % tez")

#####################################################################

# class PowTwo:
#     def __init__(self, limit=0):
#         self.limit = limit
#
#     def __iter__(self):
#         self.n = 1
#         return self
#
#     def __next__(self):
#         if self.n <= self.limit:
#             pow_number = 2 ** self.n
#             self.n += 1
#             return pow_number
#         else:
#             raise StopIteration
#
# numbers = PowTwo(5)
# iterator = iter(numbers)
#
# try:
#     while True:
#         print(next(iterator))
#
# except StopIteration:
#     print("StopIteration xatoligini qaytadi")
#
#

# class PowTwo:
#     def __init__(self, limit=0):
#         self.limit = limit
#
#     def __iter__(self):
#         self.n = 2
#         return self
#
#     def __next__(self):
#         if self.n <= self.limit:
#             pow_number = 0 + self.n
#             self.n += 2
#             return pow_number
#         else:
#             raise StopIteration
#
#
# numbers = PowTwo(10)
# iterator = iter(numbers)
#
# try:
#     while True:
#         print(next(iterator))
#
# except StopIteration:
#     print("Xatolik turi : StopIteration")
#
#

# def generator() -> None:
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# gen = generator()
# try:
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except StopIteration:
#     print("StopIteration")


