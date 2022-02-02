from typing import List

def row_organizer(black_uniform_heights: List[int], orange_uniform_heights: List[int]) -> bool:
    
    if sum(black_uniform_heights) > sum(orange_uniform_heights):

        bigger = sorted(black_uniform_heights)
        smaller = sorted(orange_uniform_heights)

    else:

        bigger = sorted(orange_uniform_heights)
        smaller = sorted(black_uniform_heights)
    
    for index, student in enumerate(bigger):
              
        if student > smaller[index]:
            continue
        else:
            return False

    return True

result = row_organizer(black_uniform_heights=[150, 179, 149, 152, 154], orange_uniform_heights=[162, 181, 151, 160, 170])
print(result)
