# а)
n = int(input())
result_dict = {i: i*i for i in range(1, n+1)}
print(result_dict)

# б)
dicts_list = eval(input())
result_list = [list(d.values())[0] for d in dicts_list]
print(result_list)

# в)
input_dict = eval(input())
result_dict = {k: v for k, v in input_dict.items() if v not in [None, '']}
print(result_dict)
