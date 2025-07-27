# def load_file(path):
#     with open(path) as f:
#         doc_name = path.replace("\\", '/').split('/')[-1]
#         doc_lines_list = f.readlines()
#         lines = len(doc_lines_list)
#
# # with open('../doc/final.txt', 'w') as f:
# #     f.writelines(doc_lines_list)
#
# load_file('../doc/1.txt')

def load_and_sort_files(paths, output_file):
    files_data = []

    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            doc_name = path.replace('\\', '/').split('/')[-1]
            doc_lines_list = f.readlines()
            num_lines = len(doc_lines_list)
            files_data.append((doc_name, num_lines, doc_lines_list))

    # Сортируем файлы по количеству строк (возрастающий порядок)
    sorted_files = sorted(files_data, key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as f:
        for doc_name, num_lines, lines in sorted_files:
            f.write(f'{doc_name}\n')
            f.write(f'{num_lines}\n')
            f.writelines(lines)
            f.write('\n')

doc_paths = ['../doc/1.txt', '../doc/2.txt', '../doc/3.txt']
load_and_sort_files(doc_paths,'../doc/final.txt')