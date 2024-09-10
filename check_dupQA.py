import re
import json


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_file(file, qa):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(qa, f, ensure_ascii=False, indent=4)


def count_character(context):
    if len(re.findall('[a-zA-Z0-9]\\"[a-zA-Z0-9]|\S\\"\S', context)):
        return re.findall('[a-zA-Z0-9]\\"[a-zA-Z0-9]|\S\\"\S', context)
    return None


def repair_sequence(sequence):
    punctuation = '.!\/|;:,()–-−+“’”%?=_*'
    for i in range(len(punctuation)):
        sequence = sequence.replace(punctuation[i], '')
    return sequence


def check_dup_options(l_qa, id_1, id_2):
    for i in range(len(l_qa[id_1]['answer_options'])):
        if repair_sequence(l_qa[id_1]['answer_options'][i]).lower() != repair_sequence(l_qa[id_2]['answer_options'][i]).lower():
            return False
    return True


def check_duplicate(l_qa, sub_class) -> set:
    l_id_duplicate_ques_exp_opt = set()
    l_id_duplicate_ques_exp = set()
    l_id_duplicate_ques = set()
    l_id_qa = list(l_qa.keys())
    for i in range(len(l_id_qa) - 1):
        if (l_id_qa[i][:3] == sub_class) and (l_id_qa[i] not in l_id_duplicate_ques):
            for j in range(i+1, len(l_id_qa)):
                if l_id_qa[j][:3] != sub_class:
                    break
                if (repair_sequence(l_qa[l_id_qa[i]]['question']).lower() == repair_sequence(l_qa[l_id_qa[j]]['question']).lower()) and (l_id_qa[j] not in l_id_duplicate_ques):
                    l_id_duplicate_ques.add(l_id_qa[j])
        if (l_id_qa[i][:3] == sub_class) and (l_id_qa[i] not in l_id_duplicate_ques_exp):
            for j in range(i+1, len(l_id_qa)):
                if l_id_qa[j][:3] != sub_class:
                    break
                if (repair_sequence(l_qa[l_id_qa[i]]['question']).lower() == repair_sequence(l_qa[l_id_qa[j]]['question']).lower()) and (repair_sequence(l_qa[l_id_qa[i]]['explanation']).lower() == repair_sequence(l_qa[l_id_qa[j]]['explanation']).lower()) and (l_id_qa[j] not in l_id_duplicate_ques_exp):
                    l_id_duplicate_ques_exp.add(l_id_qa[j])
        if (l_id_qa[i][:3] == sub_class) and (l_id_qa[i] not in l_id_duplicate_ques_exp_opt):
            for j in range(i+1, len(l_id_qa)):
                if l_id_qa[j][:3] != sub_class:
                    break
                if (repair_sequence(l_qa[l_id_qa[i]]['question']).lower() == repair_sequence(l_qa[l_id_qa[j]]['question']).lower()) and (repair_sequence(l_qa[l_id_qa[i]]['explanation']).lower() == repair_sequence(l_qa[l_id_qa[j]]['explanation']).lower()) and (l_id_qa[j] not in l_id_duplicate_ques_exp_opt) and check_dup_options(l_qa, l_id_qa[i], l_id_qa[j]):
                    l_id_duplicate_ques_exp_opt.add(l_id_qa[j])
    return l_id_duplicate_ques, l_id_duplicate_ques_exp, l_id_duplicate_ques_exp_opt


def check_error_pair_year(sequence):
    if re.findall('[0-9]{1,4}\s[0-9]{1,4}|[0-9]{1,4}\.[0-9]{1,4}', sequence):
        print(re.findall('[0-9]{1,4}\s[0-9]{1,4}|[0-9]{1,4}\.[0-9]{1,4}', sequence))


def check_error(file_qa, subclass):
    for id in file_qa.keys():
        if id[:3] == subclass:
            check_error_pair_year(file_qa[id]['question'])
            for option in file_qa[id]['answer_options']:
                check_error_pair_year(option)
            check_error_pair_year(file_qa[id]['explanation'])


if __name__ == '__main__':
    id_subclass = input()
    QA_file = read_file('QAs_final_upd_4.json')
    check_error(QA_file, id_subclass)
    # dup_ques = check_duplicate(QA_file, id_subclass)[0]
    # dup_ques_exp = check_duplicate(QA_file, id_subclass)[1]
    # dup_ques_exp_opt = check_duplicate(QA_file, id_subclass)[2]
    # print(dup_ques, len(dup_ques), sep='\n')
    # print(dup_ques_exp, len(dup_ques_exp), sep='\n')
    # print(dup_ques_exp_opt, len(dup_ques_exp_opt), sep='\n')
    # print(dup_ques_exp.difference(dup_ques_exp_opt))
    # QA_file_update = erase_qa(QA_file, dup_ques_exp_opt)
    #
    # write_file('QAs_final_upd_4.json', QA_file_update)

