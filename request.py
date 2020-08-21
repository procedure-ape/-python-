from fake_useragent import UserAgent
import requests
import ast

ua = UserAgent()

# 请求的网址
url="https://music.163.com/weapi/v6/playlist/detail?csrf_token=fe701fbec082bda0c11c51807c00251e"

# 请求头
headers={
    'User-Agent':str(UserAgent().random),
    'authority': 'music.163.com',
    'method': 'POST'
}

data={
    'params': 'j66NtkfvtL42Z1CoLSdRru6ujINmE0HBqan3yF6EMSIYnz5135cA4w/X0Xn7U3qljUOGyzDO6tkQQu3UwdrbuTDOkxu1aj/J7Hwmeg4nIUPX1oq/CN6t4kX2II/uCdw9F+FC9GHcvllJyqe0Si3fc/N4b7h4Ibmlnxtugt5p94qvNj5qfc3MOriHbkw0t4UlrHlGJunZEr2hvjN3KxiY41MKzk8RzC91rBFPKp6qcUI=',
    'encSecKey': '1c8c8d5251b27bc11b134131d404411a6196baa1e5abeeb470b615f773123a3df09f2826148341a13b496d857cbd12187712ce14113d277a243fd3d93f6038815b49e05912d408684506f394b179136b1716a9128fe84dcf594f731a915ecc352473f4bffd180e398ed6080409e5d40e2da45ead358d6181460dc91d0e7c3492'
}

# 发送请求
response=requests.post(url=url,headers=headers,data=data)
# 响应体内容
tracks=response.json()['playlist']['tracks']
for i in tracks:
    print(i['name'])