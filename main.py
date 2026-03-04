# 21-m
def baho(i):
    if 90 <= i <= 100:
        return "A"
    elif 70 < i <= 89:
        return "B"
    elif 50 < i <= 69:
        return "C"
    else:
        return "Yiqildi"

x = baho(92)
print(x)


# 22-m
def oy(i):
    if i == 12 or i == 1 or i == 2:
        return "Qish"

    return "Qish emas"

x = oy(14)
print(x)


# 23
def son(a, b):
    if a > b:
        return "1- son katta"

    return "2- son kichik"

x = son(2, 3)
print(x)


# 24-m
def matn(i):
    if i == i[::-1]:
        return "Palindrom"

    return "Palindrom emas"

p = matn("alla")
print(p)


# 25-m
def foyda(a, b):
    if a == "User" and b == 1234:
        return "Tizimga kirdi"

    return "Xato ma'lumot"

x = foyda("User", 1234)
print(x)


# 26-m
def son(i):
    if i > 0 and i % 2 == 0:
        return "Musbat juft"

    return "Boshqa son"

x = son(32)
print(x)


# 27-m
def h(i):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == "o'":
        return "Unli"

    return "undosh"

x = h("a")
print(x)


# 28-m
def matn(i):
    if i.lower():
        return "Faqat kichik harf"

    return "Boshqa belgilar bor"

x = matn("SHFGD,ASHKGF,HKSDF,SAH")
print(x)


# 29-m
def son(i):
    if i <  0:
        return "Ikkalasi ham musbat"

    return "Kamida bittasi manfiy yoki nol"

x = son(10)
print(x)


# 30-m
def matn(a):
    if a > 0:
        return "musbat"
    elif a == 0:
        return "nol"

    return "manfiy"

w = matn(2)
print(w)
