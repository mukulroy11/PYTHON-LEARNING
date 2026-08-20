#Characters as Numbers: Computers can't store actual letters (like 'H' or 'e'). Instead, every character is stored as a number between 0 and 255.
#1 Byte = 1 Character: Each character takes up 8 bits (which is 1 byte) of computer memory.
#The ord() Function: In Python, calling ord('letter') tells you the numeric code for that character:
# ord('H') -> 72
# ord('e') -> 101
# ord('\n') -> 10 (the newline character)

print(ord('a'))
print(ord('0'))