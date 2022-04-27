def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    out = ""

    for letter in phrase:
        if letter.lower() == to_swap:
            letter = letter.swapcase()
        out += letter
    return out
print((flip_case("Aaaahh","a")))
print((flip_case("Aaaahh","A")))
print((flip_case("Aaaahh","h")))