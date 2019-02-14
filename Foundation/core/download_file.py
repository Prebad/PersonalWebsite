import requests
import os

def get_urls(root):
    start = False
    curfname = None
    record_path = '../resources/record.txt'
    if os.path.exists(record_path):
        curfname = native_read(record_path)
    else:
        start = True
        f = open(record_path, 'w', encoding='utf-8')
        f.write('')
        f.close()

    s = requests.Session()
    count = 1
    imagedir = '../images/'
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if not start and curfname and curfname == filename:
                start = True
            if start:
                if filename.endswith('.txt'):
                    native_replace_write(record_path, filename)
                    data = native_read(dirpath+"/"+filename)
                    for k in data.split('\n'):
                        try:
                            if 'redd' in k:
                                continue
                            response = s.get(k, verify=False, stream=True, timeout=20)
                            with open(imagedir + str(count)+'.png', 'wb+') as img_file:
                                img_file.write(response.content)
                            count += 1
                            img_file.close()
                        except Exception as e:
                            print(str(e))

def native_read(path):
    f = open(path,'r',encoding='utf-8')
    data = f.read()
    f.close()
    return data

def native_replace_write(path, content):
    f = open(path, 'w', encoding='utf-8')
    f.write(content)
    f.close()

get_urls('../resources')