def request_tuple(file):
    some_file = open(file, 'r', encoding='utf-8')
    some_list = []
    for line in some_file:
        remote_addr = line[:line.find('-') - 1]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('/d'):line.find('_') + 2]
        some_tuple = (remote_addr, request_type, requested_resource)
        # print(some_tuple)
        some_list.append(some_tuple)
    print(some_list)
    some_file.close()

request_tuple('nginx_logs.txt')