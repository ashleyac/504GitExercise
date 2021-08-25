def base_count(sequence):
    count_dict = dict()
    for base in sequence:
        if base not in count_dict:
            count_dict[base] = 1
        else:
            count_dict[base] += 1
    return count_dict

def base_freq(count_dict):
    print('freqs')
    total = float(sum([count_dict[base] for base in count_dict.keys()]))
    for base in count_dict.keys():
        print(base + ':' + str(count_dict[base]/total))

base_freq(base_count('ATCTGACGCGCGCCGC'))
