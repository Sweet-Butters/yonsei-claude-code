# 3강 — 자동 알림 서비스 만들기

## URL

```
https://github.com/Sweet-Butters/mail-notifier
```
```
https://console.cloud.google.com/
```
```
https://aistudio.google.com/apikey
```
```
https://t.me/BotFather
```

## 저장소 가져오기

```
git clone https://github.com/Sweet-Butters/mail-notifier.git
```
```
cd mail-notifier
```

## 의존 패키지 설치

```
python -m venv .venv
```
```
.venv\Scripts\activate
```
```
pip install -r requirements.txt
```

## .env 만들기

저장소에 이미 `.env.example`이 있습니다. 복사해서 `.env`로 이름을 바꾸고 값을 채웁니다.

```
copy .env.example .env
```

채울 항목은 **세 개**입니다.

```
TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=
GEMINI_API_KEY=
```

> `.env`는 **절대 GitHub에 올리지 않습니다.** 이 저장소의 `.gitignore`에는
> `.env` · `credentials.json` · `token.json`이 이미 들어 있습니다. 확인만 하세요.

```
type .gitignore
```

## Gmail 인증 (한 번만)

```
python auth_gmail.py
```

요청하는 권한은 **`gmail.readonly` 하나뿐**입니다 — 메일을 읽기만 하고 쓰지 못합니다.
브라우저가 열리면 계정을 선택하고 권한을 승인합니다. 끝나면 `token.json`이 생깁니다.
"이 앱은 Google에서 확인하지 않았습니다" 화면이 나오면
**고급 → (앱 이름)(안전하지 않음)으로 이동**을 눌러 진행합니다.

## 실행

```
python main.py
```

## 봇 명령 (텔레그램에서 입력)

```
/watch 요리일정안내
```
```
/list
```
```
/block
```
```
/quota
```
```
/lang en
```

> GitHub Secrets 등록은 [부록/GitHub_Secrets_등록.md](부록/GitHub_Secrets_등록.md)를 보세요.
> 강의에서는 **웹 UI 방식**으로 진행합니다.

---

> 이 문서의 파일 이름·환경변수·Secrets 이름은 **저장소 실물로 대조해 확정**했습니다.
> (`Sweet-Butters/mail-notifier`, 2026-08-20 확인)
