# 5강 — 24시간 자동 실행 & 운영

모든 명령은 **`mail-notifier` 폴더 안에서** 합니다. 강의 저장소 루트에서 하면 엉뚱한 저장소를 push 하게 됩니다.

## 1. 올리기 전에 확인

```
git status
```

목록에 `.env` · `credentials.json` · `token.json` 이 보이면 **거기서 멈춥니다.**

## 2. 내 저장소에 올리기

GitHub 웹에서 **New repository** 로 저장소를 만든 뒤(처음에는 Private),

```
git add .
```
```
git commit -m "알림봇 첫 커밋"
```
```
git push -u origin main
```

## 3. Secrets 등록

[부록/GitHub_Secrets_등록.md](부록/GitHub_Secrets_등록.md) 대로 **다섯 개**를 웹에서 등록합니다.

## 4. 워크플로로 cronjob 만들기

완성본은 참고용으로 옮겨 둡니다. 둘 다 `.github/workflows/` 에 있으면 10분마다 두 번 돕니다.

```
git mv .github/workflows/check-mail.yml check-mail.reference.yml
```

Claude Code 에게 시킵니다.

```
10분마다 main.py를 돌리는 GitHub Actions 워크플로를 .github/workflows/ 에 만들어줘.
키는 Secrets에서 읽고, 수동 실행 버튼도 넣고, 상태 파일이 바뀌면 커밋하게 해줘.
```
```
방금 만든 파일을 한 줄씩 설명해줘. check-mail.reference.yml 과 다른 점도 알려줘.
```

cron 은 **분 · 시 · 일 · 월 · 요일** 다섯 칸입니다. GitHub 은 UTC 기준이라 한국 시각은 +9시간입니다.

```
*/10 * * * *      10분마다
0 0 * * *         매일 한국 시각 오전 9시
```

다 됐으면 올립니다. 참고용 파일은 지웁니다.

```
git rm check-mail.reference.yml
```
```
git add .github/workflows
```
```
git commit -m "cronjob 워크플로 추가"
```
```
git push
```

## 5. 돌아가는지 확인

저장소의 **Actions** 탭 → **Run workflow** 로 지금 한 번 돌립니다.
빨간불이면 실패한 단계의 로그를 열고, 막히면 Claude Code 에서 `/deploy-mail-bot` 을 부릅니다.

## 6. 봇 명령으로 운영 (텔레그램에서 입력)

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

설정 변경은 다음 cron 실행(최대 10분) 때 반영됩니다.
