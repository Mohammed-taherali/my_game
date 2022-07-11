import keyboard

while True:
    # print(keyboard.is_pressed('a'))
    if keyboard.is_pressed("a"):
        print("a pressed")
        break

while True:
    if keyboard.is_pressed("b"):
        print("B pressed")
        break

while True:
    if keyboard.is_pressed("right"):
        print("c pressed")
        break