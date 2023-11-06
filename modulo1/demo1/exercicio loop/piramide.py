
num_blocks = int(input("numero de blocos: "))
height = 0
layer_blocks = 1

while num_blocks >= layer_blocks:
    height += 1
    num_blocks -= layer_blocks
    layer_blocks += 1

print("a altura dos blocos é:", height)

