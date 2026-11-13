# 아동용 AI 하네스 (Child AI Harness)

보호자가 자녀가 쓰는 AI 서비스에 넣어, **AI가 아이와 대화할 때 지켜야 할 원칙**을 알려 주는 설정 파일입니다.

- 유니세프 이노첸티 「Guidance on AI and Children」 3.0(2025.12)과 유엔아동권리협약을 바탕으로 합니다.
- 한국 아동의 생활 맥락(학업 부담, 상담 기관, 이주배경 아동 등)을 반영했습니다.
- 현재 **v0.2 베타**이며, 함께 다듬어 갈 분들의 의견을 받고 있습니다.

> ⚠️ 이 설정은 AI의 답변 방향을 안내할 뿐, 모든 위험을 막지는 못합니다. 보호자의 관심과 대화를 대신할 수 없습니다.

## 바로 쓰기 (보호자용)

1. [`dist/HARNESS_ALL.md`](dist/HARNESS_ALL.md) 파일을 엽니다.
2. 맨 위 **0. 보호자 설정**의 호칭, 출생연도, 말투, 언어를 채웁니다.
3. 전체를 복사해 아이가 쓰는 AI의 **긴 지침을 넣을 수 있는 곳**에 붙여 넣습니다.
   - ChatGPT: 프로젝트 지침 (또는 파일로 올리기)
   - Gemini: Gem 만들기 → 지침
   - Claude: 프로젝트 → 프로젝트 지침

> 합본은 약 8,400자입니다. ChatGPT의 "맞춤 설정(사용자 지정 지침)"처럼 글자 수 제한이 짧은 칸에는 다 들어가지 않습니다. 서비스마다 제한이 바뀔 수 있으니, 붙여 넣은 뒤 끝부분까지 저장됐는지 꼭 확인해 주세요.

여러 파일을 올릴 수 있는 환경(Claude 프로젝트, GPTs 지식 파일 등)에서는 `HARNESS.md`와 `age/`, `situations/` 파일을 나누어 올려도 됩니다.

## 파일 구성

| 파일 | 내용 |
|---|---|
| `HARNESS.md` | 메인: 보호자 설정, AI의 역할, 나이 계산, **상황별 안내** |
| `age/` | 연령별 말하기 방식 (초등·중등·고등) |
| `situations/risk.md` | 위험 대응 (가장 먼저 적용) |
| `situations/restrictions.md` | 금지 사항 — 상황 → 제한 → 대신 할 행동 → 응답 예시 |
| `situations/tools.md` | 검색·외부 도구 사용 규칙 |
| `situations/worries.md` | 고민 대응 1·2단계 |
| `situations/privacy.md` | 개인정보 지키기 |
| `situations/learning.md` | 학습 지원, 정확성 |
| `situations/wellbeing.md` | 건강한 사용 습관 |
| `dist/HARNESS_ALL.md` | 위 파일 전체 합본 (붙여 넣기용) |
| `tests/scenarios.md` | 테스트 질문과 기대 응답 |

## 참여 방법

- **의견·오류 사례:** [Issues](../../issues)에 남겨 주세요. GitHub이 처음이시면 글로만 쓰셔도 충분합니다.
- **직접 수정:** 파일을 고쳐 Pull Request를 보내 주세요. 자세한 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해 주세요.

## 라이선스

[CC BY 4.0](LICENSE) — 출처를 밝히면 누구나 자유롭게 사용·수정·공유할 수 있습니다.
