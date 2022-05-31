#天津石化系统登录
def login():
    import requests
    import re
    from tools import tool
    import json
    #访问1-主页
    url = 'https://tjsh.ushayden.com/'

    #访问主页的header
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-ch-ua": "\"Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
        "sec-ch-ua-mobile": "\?0",
        "sec-ch-ua-platform": "Windows"
    }
    session = requests.Session()
    print("url-1=",url)
    res = session.get(url=url, headers=headers, allow_redirects=False,verify=False)

    #获取跳转地址，location
    location_url= res.headers['location']
    print("获取第二次跳转url",location_url)
    cookies = res.headers['Set-Cookie']

    #获取首次cookie，产品中也是最终访问cookie
    searchObj = re.search("jsessionid=(.+?);", cookies, re.M | re.I)
    if searchObj:

        cookies = searchObj.group(1)
        print("first cookies found!!", cookies)
    first_cookie = cookies
    b = {}
    b['Cookie'] = "TENANTCODE=hd; module=passports;JSESSIONID=" + cookies


    #访问2-302跳转访问(开始验证部分请求)
   #访问2-302的header
    # headers = {
    #     "Host": "v3-test-linux-passport.hd-cloud.com",
    #     "Connection": "keep-alive",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    #     "Cookie": "TENANTCODE=hd; module=passports"
    # }

    # 访问2-302跳转访问(开始验证部分请求)
    session = requests.Session()
    #url="http://v3-test-linux-passport.hd-cloud.com/login?service=http%3A%2F%2Fv3-test-linux-portal.hd-cloud.com%2Fcas&tenantCode=hd&trial=false"
    location_url ='https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false'
    url = location_url
    print("url-2",url)

    res = session.get(url=url, headers=headers, allow_redirects=False,verify=False)
    #print(res.headers['location'])
    print("2-res-heaher",res.headers)
    cookies = res.headers['Set-Cookie']
    #print("2-cookies=",cookies)
    #获取验证阶段的cookie
    searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        cookies = searchObj.group(1)
        print("sec cookies found!!", cookies)
    #按照产品header格式拼写验证cookie
    b = {}
    #Cookie": "TENANTCODE=tjsh; tenantCode=tjsh; prjidentify=tjsh; JSESSIONID=F5A7C35A915DB70BD3CFCFBC5A63238Bc2XNfs; module=passports; TGC=\"\"; CASPRIVACY=\""
    b['Cookie'] = "TENANTCODE=tjsh; tenantCode=tjsh; prjidentify=tjsh; JSESSIONID=" + first_cookie + "; module=passports; TGC=\"\"; CASPRIVACY=\"\""
    #print("2-b",b)
    print("it&excution",res.content)
    #获取验证it，为拼写密码串使用
    resb = res.content.decode('utf-8')
    searchObj = re.search("name=\"lt\" value=\"(.+?)\"/>", resb, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        it = searchObj.group(1)
        print("it was found!!", it)
    # 获取验证execution，为拼写密码串使用
    searchObj = re.search("name=\"execution\" value=\"(.+?)\"/>", resb, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        execution = searchObj.group(1)
        print("execution was found!!", execution)

    # # 访问2.1-访问验证图片
    # headers={
    #     "Host": "v3-test-linux-passport.hd-cloud.com",
    #     "Connection": "keep-alive",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    #     "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
		# "Referer": "http://v3-test-linux-passport.hd-cloud.com/login?service=http%3A%2F%2Fv3-test-linux-portal.hd-cloud.com%2Fcas&tenantCode=hd&trial=false",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    #     "Cookie": "TENANTCODE=hd; module=passports; JSESSIONID=3C40E9ADD7EB762495CD37882AB1E60F"
    # }
    # headers['Cookie'] = b['Cookie']
    # url = "http://v3-test-linux-portal.hd-cloud.com/themes/hayden/images/login/captcha.png"
    # res = session.get(url=url, headers=headers, allow_redirects=False)
    # #访问3-登录验证地址
    # url = "http://v3-test-linux-portal.hd-cloud.com/passports/login"
    # res = session.get(url=url, headers=headers, allow_redirects=False)
    # #print(res.headers)
    # #print("3-",res.content)
    # 访问4-获取公key
    headers={
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "*/*",
        "sec-ch-ua": "\"Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
        "sec-ch-ua-mobile": "\?0",
		"Content-type":"application/json",
        "sec-ch-ua-platform": "Windows"
    }
    url = 'https://tjsh.ushayden.com/preLogin/getPubKey'
    #https://tjsh.ushayden.com/preLogin/getPubKey
    res = session.get(url=url, headers=headers, allow_redirects=False,verify=False)
    #print("debug1",res.content)
    eq = res.content.decode('utf-8')
    eq = json.loads(eq)
    #print(eq)
    #设置登录账号名和密码
    USER_NAME = "zhai"
    password = "123456"
    # loginStoken = eq['data']['loginStoken']
    encryptType = eq['data']['encryptType']
    modulus = eq['data']['modulus']
    publicExponent = eq['data']['publicExponent']
    pwd = tool.getEntryPwd(encryptType, password, modulus, publicExponent)
    print("pwd",pwd)

    # 访问5-post密码到认证服务
    #url = 'http://v3-test-linux-passport.hd-cloud.com/login?service=http%3A%2F%2Fv3-test-linux-portal.hd-cloud.com%2Fcas&tenantCode=hd&trial=false'
    #https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false#
    location_url = 'https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false#'
    url = location_url
    print ("a-location_url",url)
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-ch-ua": "\"Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
        "sec-ch-ua-mobile": "\?0",
		"Content-type":"application/x-www-form-urlencoded",
        "sec-ch-ua-platform": "Windows",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-User": "?1",
		"Sec-Fetch-Dest": "document",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
		"Cookie": "TENANTCODE=tjsh; tenantCode=tjsh; prjidentify=tjsh; JSESSIONID=F5A7C35A915DB70BD3CFCFBC5A63238Bc2XNfs; module=passports; TGC=\"\"; CASPRIVACY=\"\""
    }
    print("b['Cookie']",b['Cookie'])
    headers['Cookie'] = b['Cookie']
    #print("5-headers",headers)
    # data = "username=clshadmin&pwd1=307530f148fa4f0f01ee69721f35408fda163097e64ec836e3a86e387ffa1d5b30a172c3364ee9ae37daacf513ab7e9260751765066a1266a1b8c7a2cfd459c0add917a00fbc3c94e64a85207dd59cb85fb19c50022137ffbeb864750d7171f43a63daef4cec6509ae8bb6efdf3361b5a3dea1a23b6cd7962a722425863e54cf&captcha=&rememberMe=false&lt=LT-8-Hioe1oQUJTh6v33bWIMLoDZZI5tQgm-passport.51gxc.com&execution=39daa5d3-2965-4657-8756-d0803f6f0d6b_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuUzBaNFowUlpaVlZtZDNGb05YbEZVamRqSzNVd01HTnJlSFpqVHpWbmVUaEZibmxHV0RWWk9USlBiRkJEWm5ZNFZVZE1jMk53ZGtGdU4zcFFSamRXYUcxQmFubGxja3R4V0dkaWRHTkxWVUZsY0hkWVJYSnNSVk53ZG1KRk1rMVFjWFpwWW1JcmIwbE9lVElyVmxBMFRUTkJjVmxtVmxKa2RYa3dVVFJtUjBweVdYaGxZekZIYm1OeVMzbEJla2xUVVU1WFltZENlRUV5Wml0dWFFc3ZOek5DS3pWbWVVOTVPR1pzU1d4bGRFNXpObE5aV1ZWblQwNW1aamRzV1hBeFNFZG5iRkF6WXpBeVUwRnRjWFZwTDBOdVJGTkhjRTAzUm5oelowSlBWazVQT0ZWS2NXNXdLMWc0TTJ0a2IzaFpjMGhpWkhGbVZWTndiRU5FVlhrMUx6UktUV1p1Ym5waWJVaG9ORFpOVFZCSlJteE9jSEl5UVhvd1NtUkNhV1l3YWtaR2QyZ3ZkVUZsYVd0M2N6ZGljbmhxWlZBMWQxUkpNWFpSYlZSRU4wNVFVbUZ5U21OblNpOW9jMnBFVUdKMmRGRnFhVmR3YlRKTWFGUXdPVEkwTmxONWVVWlNNM28xU1ZkVGNFMXhhMm94UlZwb2RtUkVSMDB6ZG5wQlZFOW1ha1ZSYWxwNGMxUmpNRzB5TDNob1ducFhNRUkwUkc1SmFtSkJiemxIV2tKeVFqUm1TalJyUjNwc05VSXZaR1psTTJFMmVIVlVaelp5VkhKTmNsSmlVRkV6UVZZdk1sQTBhWGQ0TUZaRmVtWlZaR3AxV20xNE9XcHFlVXBKVWxCRVNXMXpWR2RGTDFoV1ZUUkplVWdyTjNKSFVGZFNja0ZJT1ZKS1NVOW5aRUVyYm5oaVVHaHdLMUF5TlRWU1EybG5aVmMyZEUxU1ZqQktXRUpKUTNwS1owOUpSMlpYY1ZsaVVIcG9RVGRPTW5wWUswcGFaa0l3TVhoVVZsbFFWak51ZUdWS09XUlNTVkZKWnpsM2QwdzFXRzlZYkZnd1RHaEtWRkZCTms1UmFVTlVSRVpJVjBaRFoyWXlVbGxvZFhGWUx5OXRNR3haVlhOSVRXVlBaVFJvUlVvMU1HZFBRV1ZxUVVSVVFtdDZaVU5PWkZKNk4wRkxjMkpJVERRcmNFTnpPR2d4YlRkeGJESm9WRmwwTlcxaFNrWmFkamN6YjNkbmVGQjNTMDVrUWxCMlR6Qk1TR2RrTHpGMGRXMTBWRmRPWlc5UFpIWmxNRlpEVkZwS2F6RnFkM0JwZVhJeFVXRldjMFpTYXpSeWEzUnZaMEZWVG1FMVJVTXhNRGRUVFdkd1lWVkpaVmw2UTFSb2NURnpWMHgxWXpsV1oxazBaRGN4UzJ4Vk5uSkpabVJOTUdsUWFUWmhRV0ZuWldOM2IzaFdjWEp0VXpZNFEwUkpPRzk0UkRKNVNHUkpZV0phTmsxNVRWRkZSVEJ3UW1zMFRVMDVhMlpZWjI1eGFEQm5TV3QyTUc5U2JuSmtkM0EzTTBWd1VtVnBVMEpEU0ZOMldXbFpWVzVJTmxweFYxWnFjbk53V2s1dFFrbFNhbVp2TldvMWRqSnhhVmxKVGt0RFpWRkJNVWxvV1ZwTmF6TjVOV293VjBGck5uWXplVFI2YmxCUWN6ZDNPREpJYm1jMGVWUkVkV2RzT1dsd2QxRnJSRWxtYkdWR05rcHBVa1pWWm1acGVEUkdRMjlVWjBsMGVYaGlRVGRJV1hCTmNEWmtkbU14UlRjNVQwbzRiaXRWUTFRM1RGSTRUQzlqTlVsaFFuRm1aa0Y2WTFSUFJWcFJVamMzWmxOd2VFc3djMVYzT0ZGd1ozbFVWazVCVmtoQmRVWkNXVTVSV0dKWVFqZHdUVWx0VTNGV2EwZEdSSHBXZGxNdlRHbzVZVEU0WlZwWWQybFBkV1pNVEhvMFdEUk5Ua2xhYlc0NFpFRktjRlpIUkhKWFlVZ3hTbmRTU0dKNmQyeExRazFHWjJWMVpGZDJhbVpyY21Oc1dFZDBXbFZwVEhSNGMwOXpZVGd3YlRscGExRlFUMjgxWm5kdlJVOUdkR3R0ZWpsU1VrUnRiRmhVUjA5VGEwNWtkbmxVT0haUmVETXpNQzh2TlVGYVRHVkZiRmsxYWpBelpFRk9ZaXN6UzNabU1HMTZLMVJHUWtJNGFraEVUU3RDV0RnM2QzZEZOV05tU1RSNWNWcEZkVEpaTVV4bU1sVkdUMlpIVFRFd1FWSktZbWxEY1hOaGIzQnBhRkZsUTJoUmNXY3lRVXRWVWpKcFQwSlJjek54VVdjMFJtNWllVzFCYVZCVVRVOU5aR1YyV0doR1EwRlFaRXh6TDIwd1QyMXJUVkJTY21wb1IxcGFkbXhKT0RsaFNWcG9lRVJFWmxCMldUQnZWWGN5YTNNMFRYbDZUVE4zZERNMGFFMVNRV0kxTmpjM2NEWjRVRlJaUzBOWGRIUlljSGxWTlZReVJHWjFSbmd5U2podE1YaGxZa3d4Y1RGc1NrdFVMeXRpYmt0VWR6WTJTbVpYYkRsSlIxcFJkbXR2WWpsdWVXRkVXRnBwV0VKSWVtY3hVV1JFVFhvM1UwSlNRMWRyZDAxUVIxZ3pWbTEzUkZaNGFrTk5lR01yTUVweE9WUkxRMWhUVlZkalkyTTVla05OVlRSaVZqQkhOMFZQZUVJM1dHc3dRa3BUVmpGMFZWSlBWVzVoTjFNemJWQmFVMVpET1RSMU1WSldUMFpYWW1ZMkwwUkNjVmxuVW5SMGIyVndORFpEVFVKcFVsRkJTMnBVT0U5UWVFMVVMMUJOYURrcmVGVXlibTlMVUZvNFpIcFFZMHRLY2xWbGRIbGtaRWhHTlZOa1psaFVUM2RVZW5Sb2NFcHVVbEpoY1ZkYWVEaENVa1V4TVVKS05taHhaVlpWT0dJeVQzbFFjVGhSV0VKNVVscHBjRzl3VEdOMFZFWktjMXBwVkU5NVYxUXJXSGRFY2tOS00wZzBMMkpJU1VsUFRWZHNTVEZVTVRoWlprMDBTR051VVRsR1FYWmFiV2x1V1Zwa1YwUm5jRWhYUmpsb1VuRkRlbk51VFRZcmRsRkxkSEkwZGtwTGJtbHNSekZOUVhKWVVsWmtRbFl2THpSTWRFOVRZbGhEYVdwMldFa3hUa0ZVZW5STldFNVFOREZSZERWUVEzVkxiWEp2VkRSTlEwRnRWVkIwSzJ0SVZVRkNTM2xzYURKUVRWUXlRWG93TURsdVZFNWFOVGxLYjJJck9TOVVPSE5NY2tZM05ISm5UVFZ1YTNScFYyWk5WVVJIZFVoVmRGcDVXVlpNY2t3cmFXczFWMmxYUlVWc2NWbERiVlJsVUhBclNtSm1PRkE0VnpWT1RVa3liekIwVm5kemJUQlhaV04zWm1wT0szZEtTa2R6T1ZSalExSnhlVzExYzNGWlFXWTBhelk0Tm1oRFN5OXdTVUZaUjNGd1oyTkNjR1JzTW1OaFYzbHpkRzVPYTFsWFZuUktjMHBzUkVsT05YbHpkM05hUkU1RE0wWjZjVGh0VjBGalZEQXljMGt6YUc1VVlYWXJiM2R2ZWs4MVVFaHFhMDA0YjJNelpVWTFNbWQwYzNZMlNHMW9hVUpGTDBaV2FrUjZUVTUzV0ZOcmVuTkVNbEF3ZUd4YVIxRllkSFF6UVZweE5GaG1ibFp1YjFCM2JUVkpkMlIzTkRjM09ESXZUSEk0VEc5UWNFMUpZVFowVDFWYVdrNDFjbTVNWlVjNGNFWnlWbE0wZDNCcmJYQnlXalY0Tlc5UFJGTk1kbEYyWjA1MVdHMW1iR1JqUlhack9GRllRa2tyVHpVMU9VRnlOV2RPUzNSSVdtaHBNV1JUUVhWQ1REWjNRbmx4TDNjeFJETlZMM0ZQWjNRMlJubENhSFpJYXpNek9Ga3dURFF5V0hKWVMzSk9WamRIV1ZCb1dVbGhSV0ZOUW14bEsxVTNNMjFVWm1jNVYwTkJOWFV3WkhWeVZsZ3JWbk4zTnpKMmVYQXhTVEZQZGpSeFdtUk5PSE5zT0RKSE4xUlpPRmRySzNrMlprZGhUbnA0TjNoU1IzQlhVbXBOWkhGb1IzSkxZVFpoUjI1Sk4xVlRTMlpIVVhWNGNYaHBWR281VG5WWWQybFNWRUZJVVhwTVZrUkhTbkU0Vm5SeFJGUmtNRkZwZGpCQmQwOVBhRVJYYjJSSlZUVlJialJ5UkM5cWRsTnJVa1pXYlhkdVVGaEdVM0kyZDNWalYzTXdRME5LU1doT1ZrZDZZWEJGT0ZOa1UxVk9NMWw0Y21FeWVETnVVVzFvVTB0eGR6ZHRUa3A2U2xSNE1WSkRTekZQVlZScGFteDRZa2x5VEdKUmJURnlaekI1VURoamJWRTNORll4ZWxnNEwxbG1WR1oyT1VwVlVUSm9VWEF2THpOYWMyaHdSV2xHWW0weGVFVnlLMEk0ZFdKb2RsbEVVbWRNY214Wk5tcGpOMHBQUkdwR1pGWk5kVFk0TnpRemNrcDJNekJGVUhkMGJrMDVNM0pRZDBWMllWRm5VbTE2VlRkTVIxUkhWbTF3VkdGS2NFTXlOMGxVVGxaamR6QXlZbEl5ZW5WQmJtaEpiVWQyZVRGUlMzSTJUbkF5VTBnM2IxVnhUekJNVms1NGJIZDVTbFV2WmxkeFpsa3lVREFyVEd3dlZrVmxXa2wwTldsU1NqTXljMWt4UVhveVUwdFBUVVZaVldWTU9YZFFLell4V0hZNFZtMVpNbGx4VGpaalZ6ZDNPVFE0YldGVkwydGpNRkJhV205NEswNXRhM0J1UjI1U05YZEpVWGRGZDFsdWJtdzBOekl2ZWtwTWFuSnZjM2c0ZFV4R2VIVXlUSFZYZWxReVpXMVBaRVZ0UVVsMVdUTXZjVVptZGxWM1oxRlpWR2RFVUVWcE9UTXpXWGg1YnpZMGJHdzJaeTlzWTFCTlpHVXJPV1ZpZG5ocGNXMTZXbVJwUVhJNU5GWmphRVE1YmtnM00xcERVMG9yUkZGclVYaHpWVVphUlZWcVptUm5VVEZ2U205c05uVjRNakZoVTI1UFpUaFhibGRxZGk5akt5OVFSa1poVVVoSGJtSnNkMlppVUhkeGIwMUZUMGxuWmsxaE1VRnRhMlJMZWxnd1MyOUJUalpYUTFrNVZXdDRjVzlaY1ZwbWNUUnZWRTFsVFM5c1UwZ3llbk5vSzJsa1pVRlZTU3RJUW1Jd1dUSlViMnBEV1dGVlpEbHRXWEI1Tml0ek1pOUdWM0p2TkRSRFZYYzBkVE54UVRWYVozWjVNR2swVWs1cVkwWTFibko0VWtwMFJIcGFielZUVGtsSmRqRlJQVDAucHctY2V0RWZiT012UXU2X3Q0T3ozT29DVXEyZWMyYUtJS1NyNndmYUo1YmVxdDU3VHlDYjV6bnN5U25FLUFLdmZHcm1xWmx1bjRIQ19GekRGRjFIaEE%3D"&_eventId=submit&module=UNKNOWN&password=307530f148fa4f0f01ee69721f35408fda163097e64ec836e3a86e387ffa1d5b30a172c3364ee9ae37daacf513ab7e9260751765066a1266a1b8c7a2cfd459c0add917a00fbc3c94e64a85207dd59cb85fb19c50022137ffbeb864750d7171f43a63daef4cec6509ae8bb6efdf3361b5a3dea1a23b6cd7962a722425863e54cf"
    #username=hdtest09&pwd1=281fd69bfe1c8ca583b3de417a02bdc37a09da70e8fc03dcb13c6269998fe8148738163b2464847b6f4e5eea44f5944c0b1e4e8c7a379d87a319292d6ee9c14964b4b314d092b720cd441928bde396ed49a2fb07105ee55b27252e992140610be92337c80d6706e6250cddb3a07a95e7fb81c054f51a8e5cab91323e5b37098a&captcha=&rememberMe=false&lt=LT-22-eKRzkz4jdMbenjhHaBRtPmuyASKeHM-passport.51gxc.com&execution=88f36196-9453-4ded-8b42-b79bb495038d_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVXpGeFVIRTVORU16T0hoQlZHMXRaM0ZYUzJsRFduUk1kWFl6UmpNeVNHUTFVSGMzYm1WeFRXWnZNa1o2UkZsWlZFRlpVR1V3VjNkNU1TdFhWbmhpS3paUVpVaEdlRU5ITkZVemNXSlhkbFJoYnpkVGJURlJaRFpxVkdsNU5HaFFPR0Z2UVZZclducDFaSFJZYzJsT2NtbGhNRlppV0RWc2NpdFBTSGRpV201VU5URjVUMEZXWVdkaVRUWnFaRk5xUzNCQlRYSlJTMEZUTldoaE9USnhabkp4TnpoYVUwVkNWRGM1TUdJdlMwSlZSVlJuTDFSa1ltcFhjRk51U2xoVWFEQkNPR1pDVmtoRWIxbDFMM1pYVkdzMVVHdG5TbWdyU0VKcWRESllUMjVRWTBoWk9ITkpaSEZRVjA1MmJ6bHhjV2wwUVZGcVNYRkJTWGN6TlROWVJHTjZiRmt2Tlc1RGRtRm5Oa2hwY0dRMmFUZE9Ta1JwUmpWb2QwNUVNVWd5VmxadGRYVmhZM1ZaZERkc1dsTnNWVmgzUTFCdlNISlhjV3RtWVZCR1VsQjZaazlOWTBkMWJYaG5PWFU1YW5kU2JUUlVhM2NyTDJSdmRHMVRXRXBsY0RBMmNGZHBWMG8yZFUxeGIyaDRiblJOY1RVM1lXSklZVWRMT1c5elpuUnNhMVpzWmpad2JGcG5UVE5xU1RSWFUxTnZPRk5NYUcxMVZ6UkVhbVJoZFdwS1ZtOTZUVTAwZERseFVGaHdUMlpzUXpOak5reE9hM1ZtUml0MlRtOU9aRGRLTDJwblRXOWtPQ3RHZG5SSldXZzNhVkZsVWtkd2RrTldhWGhhV1hNeFJtcFFSRmh5T1hCTk1DODVRbFZJVFVKcldGbExLMWNyZWxKR2QzWnRaekJXTWtjeGMwNDRSbTlFWWtsYVZtSjVNbk41TTAxRk5IaEpaVGxwYTJSV1VEWm5iSEF6TlVWTGRGVlVURWxpTTNsSWRXcDZWSFppVjJ0bGVEUnljbXBLYkRGNE5YVnRjRVpzWkhkUlQzcGhTVGhXYVdOUVQwOWhNbFZSTVZaNlUzbENORXc0ZVVsb2JuVTJZbWd5VFVGcVpHb3hPWGhaYVVKWU1tTlNiVTVMTjFoQlNtSmxUbko1ZG1weU5tdDNRamgzTTJ4WVlVTTFiSGhRVDBGSlJtVm9NamhZUjJKMlFUSnRSbkZxYkV3NWNtVjBWak5DV0U5UE9VNUxhMk53TldwVmMyTldRbUp6WkZKWWJIRXJjelJJY2pCSGRFTlJObFJaYzFFeFkzWmpTM2hGWXpCUWJtdzBWazl0Y2tOSU56WllSV0ZGYjAxb016SlFSM1JCY0dSSFFuZERZWEJzWTJJMVNVczRXRzVWU2xSWVMwOTBjM1UzT1NzeldDOUtlR0ZHVFZOT05XRTVjWEo2VlUxeE9XRlRWREZ6WkU5blIwaDZNVlUyUlRoTVZ6aGtkbkoxYTBZek5WQmlUamhOWTI1T1MyMURRVGRNY1d0S1NFd3llRkozYjJwVFVVMHdORFJHZUhoelIxY3djVzlKY2l0bVkxbzBRVmxyTm1SNWJEYzRURlJuYVVKalZrWnBaRkZKUTI0NVIzZE1iV2hDUW5oTE5qRjZNSGxQY0UxclQxZEVjVk5zV0hOdmRrMUtVR0p3YjI5TlpDdEZWRk5xVjJzclRsbEphRTVNU0VwemJHdDZkUzlESzIwMVExTkZTbE5HTDJWVVprRXJaVnBtWVUxaFJFWk5jMWRzVkdkblpUVnpibEZPVVVaSU5FSjVVRlpuZEdWSmMwNDJPRzAwYTFFNVRHeHhTbGh6VGtvNUwzWXlkeXQyZG5SdlpWTTRRemRHVmpSb1R6SXZWRFpaV1ZaclUyNDRUamczVWxnMVEwdHJjMjVuUlhCUFJXSnllWEIxT0ZscmVXUmtPVTVLYzNSTmRrNHlhMGhYZEV4SGFtMXdZVE5OV1hGR1RUazVhbTkzUlZKMlpEWTVkeTlCZUdkTkswaHpkVFpOTUhKQmMzTnRWbkJoUTFaelJqUkNRVEE0ZUd3NWMySXJTMEl3Tm5BelVVSXJTRGxLUzBWVGJVbE1RaTh4Ym5OVWVIQmpZMFpYTXpodEsxSlpjV0ZzWW5wSU1VWmtOVFZRWjJSeGFHSjRSMUpHWkV0TVIzZGFXVTFVUzJ0V2NHUjZXVGg2WmxjMVNrTlVNbGhTTWs0M1NETkVXRlJyTUVkVUswTlBWMlJCYXk5blFUZGpSVEpFTlhjellVZFZNVGRrV1Uxb1oyaFVOVGxOWkZsTFEzSjRObVpLTjFsMU1XWm5Ua3BVV0ZjeE5YSnVOM0JKTjJJMGNYVmhlSEpqWWpoMU1taFlja2cwYVZGVVZFOXpXR1JsV0hsYVdFb3dkbXBoT0hoaFpIcFpVVTB3T0VnMVEzTjNaWEZyT1dKMWVUUjNRME5WTDFCTlZsVnhiblZYYkd4UVVuRnlWMmhvTkVSblFXdHBXV0ZHVDJzelMwVkVjMnN6TmxkdVYxTjNiWFZqYTNGeVRDdERSMGhKZDNocFJVNVhhSEU0UkRjM1duaDZNbmh1UTJ4TlZEYzBXR0ZTZGtJNU5GSkRZMlIzV2pGalNUZGtTRU5pUkZwc1dFWkdiVE13ZW5CYVpFRlBjM2Q2YXpONmRuQmpjVUZ4ZG5kVWFsa3hNams1TTFReU56UkhXQzlzV2taUGFpOXFNRFZyVVRnNUwyUXdkRGxyVTFoRU0zQnlORVJaVWtadVQyUXhiVTFZZVRoSloyZzNPVTFpUjNwcUswOTZaRmRxVWtSRU1GVndRalZxYmxkdVZGUnBTREkwVEM4MGJFbDJUbk5CYVRWVWFWbDFXbkpwUW5sS2VrUm5jRXhVSzBFdlJXRjRNMjlLWTI0NE1tUnFhVnBWUWxsNmNGUmpaRWg2ZWxGQ1MyZ3pNM1ZZTjBKMFdXWlJhbVFyZUdKVmFXNDRXbTVST1U1SlVXZDBUa2RsWTB4TVUxVkpURmRMVmpkRGR6UXZSM1JsT1RkSmJXVXdNa0ZMWmpWMWVYQnFNbTVvVmxocGFGaEVhSFl5VFM5U01XVnhWREJvVFdFclMyazNibFJJUkVSQmNFZ3JjSFZTTmxGb1IwYzBLME53UTFOMFQwTlplR0pRUVd0d1ZHNVFaa1ZDUjIxSmVrZG5WR3BuTkVwS1JFcEpTbmRaU3poVFpFNXdTRmdyVkhOc05YSjNVMkpGVkhNd1JUQXdVWFE1UVdOUlJERnFaMVp3YmxjMFZFMHZOVkl2Y1hsME9YSnZTbGxhZEdNMVoyWXdLMmhHVldNNVFYZzRZbWRPVmpoUmEzRnZPR1JtWlhwWEwwOTRjRVJTZURjcmNXeDVTalZFVTNkM2VXczNkVXBJTDB0MFpsUTRaWGRGZUhGR2VWRjVSRzUxWTAxd2JURmxUMlZLUkVzek56RnlhM0pETURaTmR6bGFVR3Q0YUM4emJqUm5NSGN6ZUcxQ2FVdDFaelF4VTNGTFVpOVZXbFpVVTJzNFQyOU5keXRYV1RsdldqbG1PVEJIT1hwRlkxQm1WMGg2T0hNNWNHVk5WMEZzU0d0VFpGSlZURnBCVVRFMFYxcHZSalo2U2xOMFlXa3pNbE51VkdwTk1VRkdMMWcwVEdsNFZVb3JOV1FyWW5CQkswRllVVkpQT0RaVVVGRkxSMmhPUjNBeVNrTTVjbkEwZG5WbFZraDRSVFpETm5Wd2VWbzBlRTF3VDBwNE5rdE5ibGhMVDI1ME5GQm9aRkZXUmxoaE9HNVhObGxIVW5WTVlWSktiQzlSYkM5WVJHaFdka1pPUlZwa2NHbDFTMU16YzNaRE5XRlBaRkV2ZEdFeWQyNHZTVlZCUjJsSU4zWnNhV3NyY0dSWWJpdHpUemRxWW5GcmFYQkpWak5qYWtKRFptUlpXV1kxTlZwbk9YaE1OR0ZtZFVaUFRXcHZTa05uWWtsTk1rNDBOVTVMVlhSSWQzSTBLMVJxYTBSMVVFcE9ibVpTYm1ZM1JGSTJUR3h6TkZkRFdWQk1lbmxDV21OT1owMVlWQ3R1VFdobE5uWlJVV1ZvV0VjM1Jrc3ZPWEZaVEN0SU1rVlpPWE53U1ZoaE5rVkxVRmxEYzAxUFRqaDNTRk5SWmpZek9VNTFaMXBYV1U1cU0wVlVkRXd6VFVkNGRXRjJSV3RaTTFVd09YWnBhRUpTWlZnd1R6QXlaazlNVjNSclJEZzRkSFZWWVM5Q01IY3hRbUZHZHpNNFEzTktaVk50T0N0emRITkpiMGhoV0VSdWJITjBWeXRHUmtJMlFUTnljMU5sV1RoQ2JFNDBLMDlvVG1SRk9FZDBkbTU2U0ZoWlVtMHdjMEo0TDFkdlEyWjNLMVpNVDJaaFYwWllNMUpzYWtaT1UyUklLM2RTVFRGUWJHSjFPRnBQVTJod1RrcFZORE50Tm5GSVpXUXZRaXQ0Y0c5V1pFcENRVmRpTW1VMVluY3lkVGRtWjFSUFQzcDJkbms1WmxVeWVsaENZVUZHVkZsbmNVdEpXbkJSTjBsbmNXRXhka3d3WmpnMlpteHBNelF5SzFCa1ozcEVOM0ZCU1c1YVN6bFdVRkJUVGxCQldFaFZNVEZPWlVwdVYyTnVOVTFvYmtsV2NUUTNXR1F5U1RsTU1rMXlRblJVU2tKeFl5c3JXWGxDZEd4VmRUZFBUM05tZFZseFVqYzVjR3hwTmxGRWRITkRabmxvUkhkV09YSnJNVkV5VjI5YUsyMUVaMkY1T1cxSmN6QlhSRnB0WjNCUlpqa3lMMU5hYmsxU1VGRXhVV012T1ZocU5YTk9iV04xY0VGWFVYaFJRbWRDYW01QlFtUlljVnBaTldzMVZWWkpjM016TURJeVkxWkdhRlV5ZEVaSk1uWnJVMFYxT1RsMFFsVmhMemxpYm5GaE9Xb3ZkbFpWVkhoQlNFcDFOa2xJUkVoblpVWndWMFZaY1VvMFRrbEVaR0ZIZEdocWVGcENhblJOUXpsVlZsUmFkM3A2U0VSSlluZFJVMkp2U214MFVWWTJabW9yUnpoeWIwTXdjbUpRVUZSQ1dUUlBhRUprTm0xa1MyVlBjM0ZJTkhWbldYWm9WSGxVZG5rdlVtSlJNRk5LUWt4MGJIWmlNVmt2YzFrMWQwSmFTWHA1Y1RoS2EyOTViSFpTUkd4RlYzQjFhSGRqWXpSNVJYQnpTVWwzTkdoWVUwZHlVSE5KZURWRlEzZDJTRFExUzNSQlMzRXpZMFIyU3pRd1RVNHZURGhuZDBJeE9UaDBabVEzYUdnclNtOU1ObEI0UVZkQlUwTnFRMFlyU2pOYVp6MDkucHRtcVh3V2lDbEtrZnV4S2J3c1hSanpFejF4QVM1NlhUa0ZUWG5ONnFZVTlzTlduTk1KejdwSlRwdFdmSlM5MGo1a3doR1lneXFaZEV3SF9TWHRvc3c%3D&_eventId=submit&module=pub-base&password=281fd69bfe1c8ca583b3de417a02bdc37a09da70e8fc03dcb13c6269998fe8148738163b2464847b6f4e5eea44f5944c0b1e4e8c7a379d87a319292d6ee9c14964b4b314d092b720cd441928bde396ed49a2fb07105ee55b27252e992140610be92337c80d6706e6250cddb3a07a95e7fb81c054f51a8e5cab91323e5b37098a
    #拼接请求密码数据
    data = "username=" + USER_NAME + "&pwd1=" + pwd + "&captcha=&rememberMe=false&lt=" + it + "&execution=" + execution + "&_eventId=submit&module=sy&password=" + pwd
    print("data = ",data)
    res = session.post(url=url, headers=headers, data=data, allow_redirects=False,verify=False)
    print("5-res.headers",res.headers)
    print("6-res.conntent", res.content)
    cookies = res.headers['Set-Cookie']
    #print("5-set cookies",cookies)
    #获取验证用TGC
    searchObj = re.search("TGC=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        TGC = searchObj.group(1)
        print("TGC found!!", TGC)

    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-ch-ua": "\"Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
        "sec-ch-ua-mobile": "\?0",
		"Content-type":"application/x-www-form-urlencoded",
        "sec-ch-ua-platform": "Windows"
    }

    b = {}
    #重新赋值cookie
    b['Cookie'] = "CASPRIVACY=;TENANTCODE=hd;tenantCode=hd;module=passports; prjidentify=hd; JSESSIONID="+first_cookie+";TGC="+TGC
    #print(b)
    headers['Cookie'] = b['Cookie']
    print("all_header",headers)
    #6-
    #获取cas认证location链接
    iturl = res.headers['Location']
    print("cas认证location链接",iturl)
    res = session.get(url=iturl, headers=headers, allow_redirects=False,verify=False)

    # url= 'https://tjsh.ushayden.com/portals/tjsh#'
    #
    # rs = requests.get(url=url, headers=headers)
    # data = rs.content.decode('utf-8')

    url= 'https://tjsh.ushayden.com/portals/tjsh#'
    cookies = {'JSESSIONID': first_cookie}

    rs = requests.get(url=url, headers=headers,verify=False)
    data = rs.content.decode('utf-8')
    #print("finall_data",data)
    searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        csrf = searchObj.group(1)
        print("csrf found!!", csrf)

    else:
        csrf = 'cbf8f02813894948b7184d95671b428d'
        print("Csrf Not found!!")
    return cookies,csrf
def selogin():
    import requests
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver import Firefox, FirefoxOptions
    import re
    print("开始登录")
    opt = FirefoxOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)     # 创建Chrome无界面对象

    for i in range(3):

        # selenium登录测试长庆
        time.sleep(i)
        driver.get("https://tjsh.ushayden.com/passports/login?service=https%3A%2F%2Ftjsh.ushayden.com%2Fportals%2Fcas&tenantCode=tjsh&trial=false#")
        driver.find_element(By.ID, "name").send_keys("zhai")
        driver.find_element(By.ID, "pwd1").send_keys("123456")
        driver.find_element(By.LINK_TEXT, "登录").click()
        j=i+10
        #time.sleep(j)
        # 获取JSESSIONID1
        c = driver.get_cookies()
        for a in c:
            if a['name'] == 'JSESSIONID':
                b = a
        cookies = {'JSESSIONID': b['value']}
        print("登录成功,cookies", cookies)
        time.sleep(j)
        url = 'https://tjsh.ushayden.com/portals/tjshadmin#'
        rs = requests.get(url= url ,cookies =cookies,verify = False)
        print(rs.status_code,i)
        data = rs.content.decode('utf-8')

        searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
        if searchObj:
            #print("searchObj.group() : ", searchObj.group())
            #print("searchObj.group(1) : ", searchObj.group(1))
            csrf = searchObj.group(1)
            print("csrf found!!",csrf)
            break

        else:
            time.sleep(1)
            if i == 19:
                print("Csrf Not found!!")
                csrf = i
            # driver.close()
            # driver.quit()
            # return cookies, 0
            driver.close()
            driver.quit()

    driver.close()
    driver.quit()
    print("quit browser")
    return cookies, csrf
if __name__=='__main__':

    selogin()