from typing import List

def array_sum_test(array: List[int], target_sum: int) -> List:
    
    current_int = 0
    
    for each_num in array:
        current_int = each_num
        
        for int in array:
            if current_int == int:
                continue
            
            elif current_int + int == target_sum:
                return [current_int, int]
    return []

result = array_sum_test(array=[3, 5, 4, 8, 11, 1, -1, 5], target_sum=10)
print(result)
