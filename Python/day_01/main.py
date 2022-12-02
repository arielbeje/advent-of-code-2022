with open("input.txt") as f:
    day_input = f.read()

per_elf_calories = [sum(map(int, block.rstrip("\n").split("\n"))) for block in day_input.split("\n\n")]
print(sum(sorted(per_elf_calories)[-3:]))
