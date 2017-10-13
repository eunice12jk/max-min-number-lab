def findMaxMin(new_list):
    array = []
    if min(new_list) == max(new_list):
        array.append(len(new_list))
        return array
        
    else:
        array.append(min(new_list))
        array.append(max(new_list))
    
        return array