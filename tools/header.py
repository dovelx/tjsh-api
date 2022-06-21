from runners import pc_login

cookie = {'JSESSIONID': 'F7DB25EB2F3882EBD5F65D4EB1138337nEzl5A'}
csrf = 'e2369c62a599456a9976b1b40666310f'
list_a = []
list_a = pc_login.login()
cookie = list_a[0]
csrf = list_a[1]

#cookie = '667E60D72B457442D01D758D320D7F27mniGS9'


#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': csrf,
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain'
    }

gheaders = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

theaders = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'csrf': 'ce99098e0f9d4b459f7280d8d19ed693',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
  'Content-Type': 'text/plain',
  'Cookie': 'JSESSIONID=B0DB71A3E8DD570C2CA0EC1151603A28WQrnN5'
}
