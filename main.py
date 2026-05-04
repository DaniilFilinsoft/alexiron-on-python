import random as rm

splitter = "⌂"

print("запуск Железкин 2.0 Python...")

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
        if int(choice_builder) < int(inputs[d]) + int(addit1):
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
                probty = int(len(a_l_b1) / a_l_b1.count(a_l_b1[g]) * 100)
                a_l_b2.append(a_l_b1[g])
                a_l_b2.append(probty)
        answer_list1.append(encode_list(a_l_b2))
        a_l_b1 = []
        a_l_b2 = []
    return answer_list1

def say(input_list1, len1):
    start_word = rm.randint(0,len(input_list1))
    print(start_word,"sw")
    print(len(input_list1),"lenn")
    start_word_str = decode_word(input_list1[start_word-1])[0]
    start_word_list = decode_word(input_list1[start_word])
    start_word_list.pop(0)
    print(start_word_list)
    answer_list2 = [start_word_str]
    print(answer_list2)
    list_builder1 = []
    word_list1 = start_word_list
    word = start_word
    for h in range(len1):
        for i in range(int(len(word_list1)/2)):
            list_builder1.append(word_list1[i*2+1])
        print(list_builder1,"варианты")
        next_word = random_choice(list_builder1)
        next_word_str = word_list1[next_word - 1]
        print(str(next_word_str),"некст ворд")
        if next_word_str != "":
            for j in range(len(input_list1)):
                print(decode_word(input_list1[j])[0],"ищет слово в списке")
                if decode_word(input_list1[j])[0] == next_word_str:
                    next_word_a = j
        else:
            next_word_a = rm.randint(1,len(input_list1))
        next_word_str_a = decode_word(input_list1[next_word_a-1])[0]
        answer_list2.append(next_word_str)
        next_word_list_a = decode_word(input_list1[next_word_a]).pop(0)
        list_builder1 = []
        word_list1 = next_word_list_a
        word = next_word_a
    return answer_list2
        
    
print(encode_list(encode_word("привет", {"я":50,"ghbdtn":50})))
print(decode_word(encode_list(encode_word("привет", {"я":50,"ghbdtn":50}))))
print(encode_word("привет", {"я":50,"ghbdtn":50}))
print(random_choice([25,25,25,25]))
print(s_str("pupu pu"))
print(generate_data("vsem krevet vsem svo vsem"))
print(say(["привет⌂всем⌂50⌂даня⌂50⌂","всем⌂буплям⌂100⌂","даня⌂умный⌂50⌂привет⌂","буплям⌂привет⌂100","умный⌂даня⌂100"],8))

