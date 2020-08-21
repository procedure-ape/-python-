import re
import requests
import json
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

def get_all_hotsongs():
    """抓取歌单中所有歌曲"""
    url="https://music.163.com/weapi/v6/playlist/detail?csrf_token=fe701fbec082bda0c11c51807c00251e"

    # 构造模拟请求信息
    headers = {
        'Cookie':'P_INFO=m18482101759@163.com|1591085794|0|mail163|00&99|fuj&1590532325&mail_client2#sic&510100#10#0#0|184759&1|mail_client2&mail163|18482101759@163.com; nts_mail_user=undefined:-1:0; mail_psc_fingerprint=25c73fa7aa4818345f0e90ae38eaa270; _iuqxldmzr_=32; _ntes_nnid=1393e57f653f9d0e4fecce52097bb241,1591085809504; _ntes_nuid=1393e57f653f9d0e4fecce52097bb241; WM_TID=xcOKo3yK7i1AFUAUAEI7CHpwB5yO%2FslY; MUSIC_U=b094f8588db91978446615886cd62a0dfb29448afdd5949642051d425b38b96eef81e6984ce9c6ac28e6a4f7dff34bee09869d258b30a315e381395bf06ec255; __csrf=fe701fbec082bda0c11c51807c00251e; ntes_kaola_ad=1; WM_NI=hjDyzcp%2B6HDZhRPtKMqLRnSmXZv8j3RaKNx61jxsOOkfSfbzBG4DRnbGRWUrRi9QpmFyRCQJx9WewiL05Cl9%2BKeUXzq3t7u%2FTWAkivjcwoOZKkNzxqVE4EoUmaW85%2BXrWEE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea4c163f1b39e86d848bcef8bb3d84b979b8baab544f693f8b2f96ba68eb885b72af0fea7c3b92aacb68c9af969b4f5faa9c752ac8ea095ca47b3949e8fd2679c86bad9e93992bf85affb3ef3b6b894ce45a9ba9d87e1728299fca5d166a2999eb8d87a92b7f7b2f36786a79ea4d442bce79986f66390f0fba4ef33e995abb6db72b3edbcd8f82598898f8cec7eaabdb990ce5289b5829bfb7b969bfca6ee5fafbf99d9b8219cae99a6c837e2a3; JSESSIONID-WYYY=23u5B9msraaqUz%2Fj8jRaRw6x8vd%2FVFIwg2Fp8%5C1pRg2GTQMPDPphP8lPwWEc%2BdJgnxWj1ocsHWtTjCxI0zco%2F%5CmsCGhIsPBwSd6uPoBu1819mR0KVjog7cdfhuZhRyAxFA%5CFW9KE2pHzU0vOevjB2usJ4b8hyaIvtArFqiRXHwChFJAm%3A1597050793897',
        'Host':'music.163.com',
        'Refere':'http://music.163.com/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
    }
    r = requests.get(url,headers=headers)

    #使用正则表达式匹配正文响应，获取歌名及歌曲ID
    reg1 = r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>'
    result_contain_songs_ul = re.compile(reg1).findall(r.text)
    result_contain_songs_ul = result_contain_songs_ul[0]

    reg2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'
    reg3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>'
    hot_songs_name = re.compile(reg2).findall(result_contain_songs_ul)
    hot_songs_id = re.compile(reg3).findall(result_contain_songs_ul)

    #返回歌曲名 歌曲id
    return hot_songs_name,hot_songs_id

def get_hotcommnets(hot_songs_name,hot_songs_id):
    """抓取歌曲热评"""
    #评论请求url
    url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'+hot_songs_id+'?csrf_token='
    #请求头构造
    headers = {
        'Host':'music.163.com',
        'Proxy-Connection':'keep-alive',
        'Origin':'http://music.163.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept':'*/*',
        'Referer':'http://music.163.com/song?id='+hot_songs_id+'',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie':'__e_=1515461191756; _ntes_nnid=af802a7dd2cafc9fef605185da6e73fb,1515461190617; _ntes_nuid=af802a7dd2cafc9fef605185da6e73fb; _iuqxldmzr_=32; __utmc=94650624; __utmz=94650624.1515628584.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=TO%2BtUvrTWONNwB%2BgzDpfjFDiggKiS%2FfpMYNam%2BWGooHNka%2BwMhdsT%5CY%2Fn%2FpSMJwo4skFIK1T%2FNjd95lbGHWMQr5d5qcMRPB9SVKWK8UuBs1OGugZ4lFwipwjwWbCepSw%5CjWv31i1Qt%5CWWwtrFzzktj8CdCzniAw%5CgFCElUJnsQygY0MA%3A1515635604215; __utma=94650624.61181594.1515583507.1515630648.1515633862.4; __utmb=94650624.2.10.1515633862'
    }
    #评论第一页请求表单提交参数
    data = {
        'params':'cG5yxYo1s0E9Eqv4QWJLM0fdPiJr0+GfKwqcGPulhOtGJ16gEBopaMhe6XeVNKDigMlpCaV7vrDNQLIOPIaTpAjlcJv+hjdCek6nL0ODfHt9ZEmtkTmU4r/+SA6Vno+o+c4EaPvhghNUXRMdVM/LltKvVanwOSvVhcqUPw9qij1d1akcxweLOWf1hKh2/q/m',
        'encSecKey':'a6c21ac04a44dca0e68174f9dfa85537a2694ecf7b43bdcd46a90836209a3d68008b430b54751bc0f56b12b6da38a265afcef1edbf687d70d1eb853144e920fea28e19a8c6145b7bad33e40d077e8a689b4bf67b367db815278af4ef227b02d85e609007106b7fc4a547bf96a1b90b0eda85bca6cc79ca6fc6559d00060d4184'
    }
    #获取响应  
    response = requests.post(url,data=data,headers=headers)   
 
    #格式化响应正文hotComments热评节点
    hotcomments = json.loads(response.text)['hotComments']
  
    #遍历热评内容 保存到当前excel
       
    for i in range(len(hotcomments)):           
        user_name = hotcomments[i]['user']['nickname'] #获取用户昵称
        comment = hotcomments[i]['content']            #获取热评内容
        like_num = hotcomments[i]['likedCount']        #获取点赞数
        x=[hot_songs_name,hot_songs_id,user_name,comment,like_num]
        #将上述信息连续按行写入excel
        sheet.append(x)

#调用方法 获得歌曲名 歌曲id
hot_songs_name,hot_songs_id = get_all_hotsongs()

#循环遍历抓取所有热评
num = 0
while num < len(hot_songs_name):
    print('正在抓取网易云音乐第%d首歌曲热评...'%(num+1))
    get_hotcommnets(hot_songs_name[num],hot_songs_id[num])
    print('第%d首歌曲热评抓取成功'%(num+1))
    num+=1

wb.save(filename = 'Formular.xlsx')