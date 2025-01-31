def fill_the_box(height, length, width, *args):
    box_volume = height * length * width

    cubes = 0

    for items in args:
        if items == "Finish":
            break
        cubes += items

    if box_volume > cubes:
        return f"There is free space in the box. You could put {box_volume - cubes} more cubes."
    return f"No more free space! You have {cubes - box_volume} more cubes."
