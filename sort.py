def sort_dictionary(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
    sorted_list = [(k, v[0]) for k, v in sorted_dict]
    return sorted_list


my_dict = {"Tom":(5464512, 24), "Sara":(5446987, 32), "Mary":(1557896,
20)}
sorted_list = sort_dictionary(my_dict)

output = [tup for tup in reversed(sorted_list)]
