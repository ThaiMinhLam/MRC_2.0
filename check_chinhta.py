import json
import re


def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_context_sgk(sgk_json, subject, grade) -> dict:
    sgk = {}
    for id_chuong, nd_chuong in sgk_json[subject][grade].items():
        for id_bai in nd_chuong.keys():
            if id_bai != 'name':
                sgk[id_bai] = sgk_json[subject][grade][id_chuong][id_bai]
    return sgk


def check_char_regex(context):
    chars_regrex = 'àảãáạăằẳẵắặâầẩẫấậÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬđĐòỏõóọôồổỗốộơờởỡớợÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢèẻẽéẹêềểễếệÈẺẼÉẸÊỀỂỄẾỆùủũúụưừửữứựÙỦŨÚỤƯỪỬỮỨỰìỉĩíịÌỈĨÍỊỳỷỹýỵỲỶỸÝỴ'
    punctuation = '木²~$^.!\|";:,()+“’”%?=_*'
    l_van = ['ương', 'ường', 'ưởng', 'ượng', 'ưỡng', 'ƯỜNG', 'ƯỞNG', 'ƯỠNG', 'ƯỢNG', 'ƯƠNG', 'ướng', 'ười', 'ước', 'ược', 'uống', 'uyên', 'ướt','ươm', 'ƯỜI']
    for sentence in context.split("."):
        l_word = sentence.split()
        for word in l_word:
            new_word = word.lower()
            for index in range(len(punctuation)):
                new_word = new_word.replace(punctuation[index], '')
            if re.search('[0-9]{1,4}\-[0-9]{1,4}', new_word):
                continue
            if len(new_word) > 7:
                print(word)


def find_error_context(context):
    if re.findall('\s+[a-zA-Z]\s+[a-zA-Z]\s+', context):
        print(re.findall('\s+[a-zA-Z]\s+[a-zA-Z]\s+', context))
    if re.findall('([0-9]{1,2}°C)+|([0-9]{1,2}°B)+', context):
        print(re.findall('([0-9]{1,2}°C)+|([0-9]{1,2}°B)+', context))
    if re.findall('\d+[àảãáạăằẳẵắặâầẩẫấậÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬđĐòỏõóọôồổỗốộơờởỡớợÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢèẻẽéẹêềểễếệÈẺẼÉẸÊỀỂỄẾỆùủũúụưừửữứựÙỦŨÚỤƯỪỬỮỨỰìỉĩíịÌỈĨÍỊỳỷỹýỵỲỶỸÝỴ]|\d+[a-zA-Z]{1,...}', context):
        print(re.findall('\d+[àảãáạăằẳẵắặâầẩẫấậÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬđĐòỏõóọôồổỗốộơờởỡớợÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢèẻẽéẹêềểễếệÈẺẼÉẸÊỀỂỄẾỆùủũúụưừửữứựÙỦŨÚỤƯỪỬỮỨỰìỉĩíịÌỈĨÍỊỳỷỹýỵỲỶỸÝỴ]|\d+[a-zA-Z]{1,...}', context))
    check_temp = re.search('^([a-zA-Z]{1,5}[àảãáạăằẳẵắặâầẩẫấậÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬđĐòỏõóọôồổỗốộơờởỡớợÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢèẻẽéẹêềểễếệÈẺẼÉẸÊỀỂỄẾỆùủũúụưừửữứựÙỦŨÚỤƯỪỬỮỨỰìỉĩíịÌỈĨÍỊỳỷỹýỵỲỶỸÝỴ][a-z]{1,2})*$', context)
    if check_temp:
        print(check_temp.group())
    check_char_regex(context)


if __name__ == '__main__':
    # sgk_file = read_file('sgk_social_subject_new.json')
    # subject, grade = input().split(" ")
    # sgk_content = get_context_sgk(sgk_file, subject, grade)
    # for id_lesson, nd_lesson in sgk_content.items():
    #     find_error_context(nd_lesson['context'])

    QA_file = read_file('QAs_final_upd_4.json')
    id_request = input()
    for id_qa in QA_file.keys():
        if id_qa[:3] == id_request:
            for option in QA_file[id_qa]['answer_options']:
                find_error_context(option)


