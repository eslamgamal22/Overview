print("Welcome to our feiled")
feild = [["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"]]
print(f"{feild[0]}\n{feild[1]}\n{feild[2]}")
print("Where should to put 🦨")
postion = input("Enter the number of raw and culumn ")
raw = int(postion[0])
cul = int(postion[1])
feild[raw - 1][cul - 1] = "🦨"
print(f"{feild[0]}\n{feild[1]}\n{feild[2]}")
