ls = [1,2,3,2,5,1,2,4,6,2,7,8,6]
unique_ls=list(set(ls))

greater_count = []
for j in unique_ls:
    if ls.count(j)>1:
        greater_count+=[j]

distance_list = {}
for ele in greater_count:
    start_index = None
    end_index =0 
    for i in range(len(ls)):
        if type(start_index)!=int:
            if ele ==ls[i]:
                start_index = i
        elif ele == ls[i]:
            if ele ==ls[i]:
                end_index = i
    distance_list[ele]=end_index-start_index
    
print(distance_list)
print(max(distance_list.values()))