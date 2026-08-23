# 바이브코딩의 한계를 부수자 — 클로드 코드 실전용 Skills

연세 프리미엄 인강 강의 자료입니다.
**이 저장소를 받아서 Claude Code로 열면, 그때부터는 명령을 직접 칠 일이 거의 없습니다.**

## 미리 있어야 하는 것

| | 확인 | 없으면 |
|---|---|---|
| git | `git --version` | https://git-scm.com/downloads |
| Node.js | `node -v` | https://nodejs.org/ |

**git이 없으면 아래 첫 줄부터 막힙니다.** 윈도우에는 기본으로 깔려 있지 않습니다.

## 시작하는 법 — 세 줄

```
git clone https://github.com/Sweet-Butters/yonsei-claude-code.git
cd yonsei-claude-code
claude
```

Claude Code가 열리면 이렇게 칩니다.

```
/run-course
```

끝입니다. **설치할 것도, 복사할 것도 없습니다.**
스킬이 이 저장소 안(`.claude/skills/`)에 들어 있어서 폴더를 여는 순간 잡힙니다.

`/run-course` 는 이렇게 움직입니다.

1. 지금 어디까지 왔는지 폴더를 보고 판단합니다
2. 해당 차시가 무엇을 하는 차시인지 `발표자료/차시_개요.md` 를 읽고 세 줄로 알려 줍니다
3. 그 차시를 그대로 재현합니다 — 가상환경, 설치, 실행, 결과 확인까지
4. 끝나면 무엇이 만들어졌는지 말하고 **다음 차시로 갈지 물어봅니다**

## 차시 구성

| 차시 | 제목 |
|---|---|
| OT | 오리엔테이션 |
| 1강 | 설치 & 실행 |
| 2강 | GitHub & 크롤링 |
| 3강 | Skill 갖고오기 & 만들기 |
| 4강 | Telegram 알림봇 만들기 |
| 5강 | Telegram 알림봇 배포 & 실행 |

한 차시는 6~8분짜리 2편으로 나뉩니다. **3강까지는 계정 없이 끝까지 따라갈 수 있습니다.**

## 들어 있는 것

```
발표자료/         차시별 PDF 6종 (사람용) + 차시_개요.md (/run-course 가 읽습니다)
1강_commands.md   설치·실행·로그인 명령 전문 (복사 가능)
2강_commands.md   clone · venv · pip · 크롤링 코드
3강_commands.md   남의 스킬 받기 · 내 스킬 만들기
4강_commands.md   clone · .env · Gmail 인증 · 실행 · 봇 명령
코드/             동작 확인된 크롤러 코드
부록/             본편에서 덜어낸 심화 내용
.claude/skills/   스킬 5종 (설치 불필요)
```

## 스킬 5종

| 스킬 | 언제 쓰나 |
|---|---|
| **`/run-course`** | **강의 전체를 처음부터 재현. 대부분 이것만 쓰면 됩니다** |
| `/run-crawler` | 2강 크롤러만 다시 돌리고 싶을 때 |
| `/check-my-bot` | 봇 폴더가 지금 돌 준비가 됐는지 점검 |
| `/run-mail-bot` | 알림봇을 내 컴퓨터에서 실행 |
| `/deploy-mail-bot` | 봇을 GitHub Actions로 24시간 돌리기 |

## 스킬이 대신 못 하는 것

| | 왜 |
|---|---|
| Claude Code 로그인 | 계정 인증 |
| API 키 발급 (Gmail · Gemini · Telegram) | 각 서비스 웹에서 본인이 |
| GitHub 저장소 만들기 · Secrets 등록 | 계정 권한 |

**한계가 아니라 정상입니다.** 스킬은 순서를 잡아 주고 빠뜨린 것을 잡아내는 것이지
계정 일을 대신하는 게 아닙니다.

## 다른 프로젝트에서도 쓰려면

이 저장소 밖에서도 스킬을 쓰고 싶으면
[claude-code-skills](https://github.com/Sweet-Butters/claude-code-skills) 를 받아 설치하세요.
내용은 같습니다.
