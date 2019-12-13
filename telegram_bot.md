# 파이썬 챗봇 만들기

## 1. 개발환경 세팅

### 1.1 프로젝트 폴더 및 .gitignore생성

* 새로운 repository

![image-20191213091346143](images/image-20191213091346143.png)

![image-20191213091437307](images/image-20191213091437307.png)

![image-20191213091455466](images/image-20191213091455466.png)

![image-20191213091820677](images/image-20191213091820677.png)

붙여넣기

![image-20191213091759224](images/image-20191213091759224.png)

### 1.2 가상환경 생성 및 진입

* 가상환경 만들기

  ```bash
  바탕화면/telegram-bot
  $ python -m venv venv
  ```

![image-20191213092735519](images/image-20191213092735519.png)

* 가상환경 진입

  ```bash
  바탕화면/telegram-bot/
  $ source venv/Scripts/activate
  ```

![image-20191213092750022](images/image-20191213092750022.png)

* VSCode 자동 가상환경 진입 설정
  * 이 옵션을 설정하는 경우, 반드시 .vscode폴더가 있는 디렉토리에서 open with code 혹은 open folder로 진입을 해야 터미널을 새로 켤때 자동으로 가상환경 진입이 된다.
  * 자동으로 가상환경이 켜지지 않으면 당황하지 않고 source~activate 명령어를 직접 쳐서 가상환경에 진입하자.
  * **Ctrl + Shift + P -> Python : Select Interpreter -> 사용할 환경 선택**
  * 무조건 Telegram_bot 폴더에서 실행해야해

![image-20191213092837328](images/image-20191213092837328.png)

		* 설정이 완료되면 .vscode 폴더가 생긴다

![image-20191213092848520](images/image-20191213092848520.png)

```bash
telegram-bot/
	.vscode/
	venv/
	.gitignore
```



![image-20191213092935705](images/image-20191213092935705.png)

우리환경이 플라스크를 따라라

![image-20191213093026429](images/image-20191213093026429.png)

![image-20191213093051558](images/image-20191213093051558.png)

[flask quickstart](http://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)

![image-20191213093134518](images/image-20191213093134518.png)

![image-20191213093222669](images/image-20191213093222669.png)

![image-20191213093229769](images/image-20191213093229769.png)

제일 하단에 껐다 켰다 하지 않기 위해

![image-20191213093416014](images/image-20191213093416014.png)

### 1.3 Flask 개발용 서버 실행

#### 1.3.1 Flask 공식문서로 시작하기

반드시 가상환경 진입 여부를 확인하고 설치하자. 명령어 좌상단의 (venv)

```bash
(venv)
$ pip install Flask
```

```bash

```

#### 1.3.2 서버실행을 간편하게

공식문서에 있는대로 flask run 명령어를 수행하면 서버가 실행된다. 하지만 이 경우엔 app.py의 내용을 수정하면 서버를 재실행해야 반영된다. 따라서 코드를 추가해서 이를 방지해보자.











[telegram](http://www.telegram.pe.kr/)

다운로드

쭉쭉 넘어가

