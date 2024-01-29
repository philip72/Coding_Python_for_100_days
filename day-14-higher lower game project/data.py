import get_data
data=[]
for person in get_data.nested_list_with_faker:
    #print(person)
    data.append(person)

#print(data)

# key_to_count = 'name'

# # Count occurrences of the key in the nested list
# occurrences_count = sum(1 for d in data if key_to_count in d)

# # for d in data:
# #     if key_to_count in d:
# #         sum(occurrences_count)

# print(f"The key '{key_to_count}' appears {occurrences_count} times.")