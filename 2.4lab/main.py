# а)
def word_count(text, separator=' '):
    words = text.split(separator)
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict

# б)
def filter_numbers(numbers, exclude_multiples_of=2):
    return [num for num in numbers if num % exclude_multiples_of != 0]

# в)
def merge_and_sort_keys(*dicts):
    merged = {}
    for d in dicts:
        for k, v in d.items():
            if k not in merged or v > merged[k]:
                merged[k] = v
    return sorted(merged.keys(), key=lambda x: merged[x], reverse=True)

# г)
def sum_non_negative(*args):
    return sum(num for num in args if num >= 0)
