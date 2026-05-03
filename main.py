import random as rm

splitter = "⌂"

def encode_word(base_word, next_words):
    answer1 = [base_word]
    for a in range(len(next_words)):
        answer1.append(list(next_words.keys())[a-1])
        answer1.append(next_words[list(next_words.keys())[a-1]])
    return answer1

def encode_list(base_list):
    answer2 = ""
    for b in range(len(base_list)):
        answer2 += (str(base_list[b]) + splitter)
    return answer2

def decode_word(base_string):
    answer3 = []
    answer3_builder = ""
    for c in range(len(base_string)):
        if not base_string[c] == splitter:
            answer3_builder += base_string[c]
        else:
            try:
                answer3.append(int(answer3_builder))
            except:
                answer3.append(str(answer3_builder))
            answer3_builder = ""
    return answer3

def random_choice(inputs):
    choice = rm.randint(1,100)
    choice_builder = choice
    addit1 = 0
    for d in range(len(inputs)):
        if choice_builder < inputs[d] + addit1:
            return d+1
        else: addit1 += inputs[d]
    return random_choice(inputs)

def s_str(input_string):
    return input_string.split( )

def f_n_o(lst, item, n):
    count = 0
    for index, value in enumerate(lst):
        if value == item:
            count += 1
            if count == n:
                return index
    return -1

def generate_data(input_string):
    answer_list1 = []
    a_l_b1 = []
    a_l_b2 = []
    data_f = s_str(input_string)
    for e in range(len(data_f)):
        a_l_b2.append(data_f[e])
        for f in range(data_f.count(data_f[e])):
            if not f_n_o(input_string, data_f[e], f) == len(data_f):
                a_l_b1.append(f_n_o(input_string, data_f[e], f) + 1)
        for g in range(len(a_l_b1)):
            if not a_l_b1[g] in a_l_b2:
                probty = len(a_l_b1) / a_l_b1.count(a_l_b1[g])
                a_l_b2.append(a_l_b1[g])
                a_l_b2.append(probty)
        answer_list1.append(encode_list(a_l_b2))
        a_l_b1 = []
        a_l_b2 = []
    return answer_list1

def say(input_list1):
    

print(encode_list(encode_word("привет", {"я":50,"ghbdtn":50})))
print(decode_word(encode_list(encode_word("привет", {"я":50,"ghbdtn":50}))))
print(encode_word("привет", {"я":50,"ghbdtn":50}))
print(random_choice([25,25,25,25]))
print(s_str("pupu pu"))
print(generate_data("vsem krevet vsem svo vsem"))
