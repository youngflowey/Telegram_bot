import requests
from decouple import config

# API 요청 기본사항
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')

# 가져온 웹 내용의 text를 뽑아야 한다. text로 뽑으면 텍스트구조이므로
# 대신 json구조로 뽑아야한다

# 봇과 대화하고 있는 사용자 CHAT ID 추출
chat_id = config('CHAT_ID')
# chat_id = requests.get(f'{url}/bot{token}/getUpdates').json()["result"][0]["message"]["from"]["id"]

# 보낼 메세지 입력받기
text = input('메세지를 입력하세요!')

# API 에 요청을 보내 메세지 보내기
send_message=requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

# 요청값 어떻게 나오는지
print(send_message.text)


