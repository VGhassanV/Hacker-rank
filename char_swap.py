def swap_case(s):
    char_swp=[]
    for char in s:
        if char.islower():
            char_swp.append(char.upper())
        elif char.isupper():
            char_swp.append(char.lower())
        else:
            char_swp.append(char)
    return ''.join(char_swp)    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)