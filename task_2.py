some_file = open('nginx_logs.txt', 'r', encoding='utf-8')
remote_addr = [line[:line.find('-') - 1] for line in some_file]
max_count_addres = max(set(remote_addr), key=remote_addr.count)
count_of_max_count_addres = remote_addr.count(max_count_addres)
print(max_count_addres, count_of_max_count_addres)




