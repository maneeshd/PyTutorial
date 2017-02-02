def tower_of_hanoi(disks, source, dest, aux):
    if disks == 1:
        print("Move disk 1 from " + source + " rod to " + dest + " rod.")
        return
    tower_of_hanoi(disks - 1, source, aux, dest)
    print(
        "Move disk " +
        str(disks) +
        " from " +
        source +
        " rod to " +
        dest +
        " rod.")
    tower_of_hanoi(disks - 1, aux, dest, source)


if __name__ == '__main__':
    num_of_disks = int(input("Enter the number of disks: "))
    tower_of_hanoi(num_of_disks, "A", "C", "B")
