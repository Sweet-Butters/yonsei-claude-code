# 1강 — 설치 & 실행

## URL (각각 따로 복사)

```
https://code.visualstudio.com/
```
```
https://nodejs.org/
```
```
https://github.com/signup
```
```
https://git-scm.com/downloads
```

## git

`GitHub`은 웹사이트, `git`은 내 컴퓨터에 까는 프로그램입니다. **둘은 다릅니다.**
2강부터 남의 코드를 `git clone`으로 받아 오므로 git이 없으면 거기서 막힙니다.

설치 여부 확인.

```
git --version
```

버전이 안 나오면 위 `git-scm.com/downloads`에서 받아 설치합니다.
윈도우는 내려받은 설치 파일을 **기본값 그대로** 넘기면 됩니다.

> 설치 후 **터미널을 새로 열어야** 반영됩니다.

## Claude Code

설치 여부 확인 — Node.js가 먼저 있어야 합니다.

```
node -v
```

설치.

```
npm install -g @anthropic-ai/claude-code
```

> 설치 후 **터미널을 새로 열어야** 반영됩니다.

작업할 폴더에서 실행. 이 폴더 위치가 곧 작업 범위가 됩니다.

```
claude
```

## Claude Code 안에서 쓰는 슬래시 커맨드

```
/login
```
```
/status
```
```
/context
```
```
/model
```
```
/effort
```
```
/exit
```

## Antigravity (Windows)

명령 프롬프트(CMD)에서 **아래 한 줄 전체**를 복사해 붙여넣습니다.

```
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

URL만 따로:

```
https://antigravity.google/cli/install.cmd
```

실행.

```
agy
```

명령 목록 확인 / 파일로 저장.

```
agy --help
```
```
agy --help > help.txt
```

> macOS · Linux · WSL 설치와 설치 옵션 플래그는 [부록/설치옵션과_다른환경.md](부록/설치옵션과_다른환경.md)에 있습니다.
