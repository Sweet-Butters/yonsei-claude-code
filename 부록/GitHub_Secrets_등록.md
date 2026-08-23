# 부록 — GitHub Secrets 등록

## 강의에서 하는 방법 : 웹 UI

1. 내 저장소 페이지에서 **Settings**
2. 왼쪽 메뉴 **Secrets and variables → Actions**
3. **New repository secret**
4. Name과 Secret을 넣고 **Add secret**
5. 아래 목록만큼 반복

등록할 이름은 **다섯 개**입니다. `.github/workflows/check-mail.yml`이 이 이름들을 그대로 읽습니다.
철자가 하나라도 다르면 Actions가 빈 값으로 돌다가 실패합니다.

```
GEMINI_API_KEY
TELEGRAM_TOKEN
TELEGRAM_CHAT_ID
GOOGLE_CREDENTIALS_JSON
GOOGLE_TOKEN_JSON
```

`GOOGLE_CREDENTIALS_JSON`과 `GOOGLE_TOKEN_JSON`은 로컬의 `credentials.json` · `token.json`
**파일 내용을 통째로** 붙여넣습니다. 워크플로가 이 값을 다시 파일로 만들어 씁니다.
등록한 값은 다시 볼 수 없고, 워크플로 로그에서도 `***`로 가려집니다.

## 참고 : 명령줄(CLI) 방식

터미널에 익숙해진 뒤에 쓰면 훨씬 빠릅니다. 강의에서는 다루지 않습니다.

```
gh secret set GEMINI_API_KEY --body "$YOUR_KEY"
```
```
gh secret set TELEGRAM_TOKEN --body "$YOUR_TOKEN"
```
```
gh secret set TELEGRAM_CHAT_ID --body "$YOUR_CHAT_ID"
```
```
gh secret set GOOGLE_CREDENTIALS_JSON < credentials.json
```
```
gh secret set GOOGLE_TOKEN_JSON < token.json
```

바로 한 번 돌려보기:

```
gh workflow run check-mail.yml
```


---

> 위 다섯 개 이름은 `Sweet-Butters/mail-notifier`의 `.github/workflows/check-mail.yml`과
> 대조해 확정했습니다 (2026-08-20 확인).
