import re

re_url = re.compile(r'\d+\.\d+\.\d+\.\d+')
re_datetime = re.compile(r'\[.+\]')
re_type = re.compile(r'\"([A-Z]{3})')
re_resource = re.compile(r'\s(\/[\w\/]+)')
re_code = re.compile(r'\s(\d{3})')
re_size= re.compile(r'\s\d{3}\s(\d+)')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = re.findall(re_url, line)
        request_datetime = re.findall(re_datetime, line)
        request_type = re.findall(re_type, line)
        requested_resource = re.findall(re_resource, line)
        response_code = re.findall(re_code, line)
        response_size = re.findall(re_size, line)
        parsed_raw = *remote_addr, *request_datetime, *request_type, *requested_resource, *response_code, *response_size
        print(parsed_raw)




