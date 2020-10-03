poem_path = "/Users/joelthomas/dev/courses/CS 1.0/Assignments/PoetrySlam/PunnyPoem.txt"
read_poem = open(poem_path, "r")

def get_file_lines(filename):
    
    lineNum = 0
    original_order = []
    
    print("\nOriginal Version\n----------------")
    for currentLine in filename:
        lineNum += 1
        formatted_line = f"{lineNum}: {currentLine}"
        original_order.append(formatted_line)
        print(original_order[lineNum-1], end="")
    
    return original_order

def lines_printed_backwards(lines_list):

    reverse_order = []

    for currentLine in lines_list:
        if currentLine == lines_list[0]:
            reverse_order.append(currentLine)
        else:
            reverse_order.insert(0, currentLine)
    
    print("\nRead Backwards\n--------------")
    for currentLine in reverse_order:
        print(currentLine, end="")

def lines_printed_random(lines_list):
    from random import randint
    print("\nRandomized\n----------")
    for iteration in lines_list:
        print(lines_list[randint(0,7)],end="")

def lines_printed_custom(lines_list):
    iteration = 0
    even_lines = []
    odd_lines = []
    for currentLine in lines_list:
        iteration += 1
        if iteration % 2 == 0:
            even_lines.append(currentLine)
        else:
            odd_lines.append(currentLine)

    print("\nCustomized\n----------")
    
    even_length = len(even_lines)
    for index in range(even_length):
        print(even_lines[index],end="")
    
    odd_length = len(odd_lines)
    for index in range(odd_length):
        print(odd_lines[index],end="")

lines_list = get_file_lines(read_poem)
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
lines_printed_custom(lines_list)

read_poem.close()
