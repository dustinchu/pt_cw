import requests
import sys
import json
import time
def post(page_num):
    with open(r'C:\品凱digikey\json\{}.json'.format(page_num), 'r') as openfile: 
        json_object = json.load(openfile) 
    page = 0
    for i  in json_object:

        tStart = time.time() 
        aa = json.loads(i['price'].replace("'", '"'))
        i['price']=aa

        a = json.dumps(i)
        print(a)
        break
        while True:
            try:
                url_contents = 'http://34.80.244.160/path_load.php'
                post_status = requests.post(url_contents, json=i, timeout=2)
                print(post_status)
                break
            except requests.Timeout:
                print("----timeout----")
                pass
        tEnd = time.time()  # 計時結束
        print("product %f sec" % (tEnd - tStart))  # 會自動做近位
if __name__ == '__main__': 

    # i = sys.argv[1]
    post(1)