from tags_extraction.DOC import docx_to_text
import re
import os
import fnmatch
import json

# main_file = {}
#
# count_error = 0
#
# num_dir = 135
#
# ind = 0
# for dir in os.listdir('../data/Новая разметка'):
#     files_docx = []
#     for root, dirs, files in os.walk(f"../data/Новая разметка/{dir}"):
#         for file_name in files:
#             if (fnmatch.fnmatch(file_name, "*.docx") or fnmatch.fnmatch(file_name, "*.doc")):
#                 patern_date = re.compile(r"<дата.*?>", re.DOTALL)
#                 patern_per = re.compile(r"<персона.*?>", re.DOTALL)
#
#                 # print(f"{root}/{file_name}")
#                 text = docx_to_text(f"{root}/{file_name}")
#
#                 if ((not re.search(patern_date, text) is None) and (not re.search(patern_per, text) is None)):
#                     files_docx.append(os.path.join(root, file_name))
#     # print(dir)
#     if (len(files_docx) != 1):
#         # print('ERROR')
#         count_error += 1
#     for path in files_docx:
#         #print(path)
#         pass
#     main_file[dir] = files_docx
#     # print("****")
#     ind += 1
#     print((ind / num_dir) * 100, '%')
#
# print("COUNT_ERROR: ", count_error)
#
# with open('data/main_file_ver_1.txt', 'w') as file:
#     json.dump(main_file, file, ensure_ascii=False)

# main_file = {}
#
# total_ans = 146
# count_ans = 0
# with open('data/main_file_ver_1.txt') as file:
#     main_file_ver_1 = json.load(file)
#     for key, value in main_file_ver_1.items():
#         if (len(value) <= 1):
#             main_file[key] = value
#         else:
#             print(key)
#             new_value = []
#             for file_name in value:
#                 print(file_name)
#                 s = input().strip()
#                 if (s == 'Y'):
#                     new_value.append(file_name)
#                 count_ans += 1
#                 if (count_ans % 10 == 0):
#                     print((count_ans / total_ans) * 100, "%")
#             main_file[key] = new_value
#             print("*****")
#
# with open('data/main_file.txt', 'w') as file:
#      json.dump(main_file, file, ensure_ascii=False)