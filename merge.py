def merge(st1, st2):
    merged_list = [] #mergelist initialized


    i = j = 0

    while i < len(st1) and j < len(st2):
        if st1[i] < st2[j]:
            merged_list.append(st1[i])
            i += 1
        else:
            merged_list.append(st2[j])
            j += 1

 
    merged_list.extend(st1[i:])
    merged_list.extend(st2[j:])
    return merged_list
