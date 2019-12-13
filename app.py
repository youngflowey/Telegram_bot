import requests, pprint, random, html
from flask import Flask, render_template, request
from decouple import config
app = Flask(__name__)

# 텔레그램 API
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

# 구글 API
google_url = 'https://translation.googleapis.com/language/translate/v2'
google_key =  config('GOOGLE_TOKEN')
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 텔레그램에게 전송
# 텔레그램이 알림을 보내주면, 응답하는 구조인데 응답의 내용이 없으므로 '', 응답 잘받았으면 200

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 텔레그램이 보내주는 데이터 구조확인
    pprint.pprint(request.get_json())
    
    # 2. 사용자 아이디, 메시지 추출
    chat_id = request.get_json().get('message').get('from').get('id')
    message = request.get_json().get('message').get('text')

    # 사용자가 로또라고 입력하면 로또 번호 6개 돌려주기
    if message == '로또':
        result = random.sample(range(1,46),6)

    # 사용자가 /번역 이라고 말하면 한-영 번역 제공
    elif message[:4] == '/번역 ' :   # 띄어쓰기로 구분
        data = {
            'q' : message[4:],
            'source' :'ko',
            'target' :'en'
        }
        # 1. 구글 API 번역 요청
        response = requests.post(f'{google_url}?key={google_key}',data).json()
        # 2. 번역 결과 추출 -> 답장 변수에 저장
        result = html.unescape(response['data']['translations'][0]['translatedText'])

    # 그 외의 경우엔 메아리
    else: 
        result = '로또 혹은 /번역 안녕하세요 라고 입력해보세요'


    # 3. 텔레그램 API에 요청해서 답장 보내쥐
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    return '', 200 # 상태코드( 200 : 잘 받았다 )
    # 텔레그램이 받는거라서 아무것도 없음

# 요청 : get 요청( url치고 엔터 , 어떠한 정보 내놓으세요) / post 요청

# 로컬주소를 사용하면 telegram이 접속할 수가 없다. 따라서 서버를 공개해야 한다. 단, 지금은 설치에 시간이 걸리므로, 우선 로컬주소를 공개해주는 프로그램인 ngrok 을 사용해 실습하도록한다

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # 1. 사용자가 입력한 데이터 받아오기
    # flask
    message = request.args.get('message')

    # 2. 텔레그램 API 메시지 전송 요청 보내기
    # python library
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')
    return '메시지 전송 완료!! :)'


# 반드시 파일 최하단에 위치시킬 것!
if __name__ == '__main__':
    app.run(debug=True)