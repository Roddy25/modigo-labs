def build_countdown(start):
    if start == 0:
        return []
    countdown = []
    for i in range(start, 0, -1):
        countdown.append(i)
    return countdown
print (build_countdown(5))
print(build_countdown(1))
print(build_countdown(0))
print(build_countdown(3))