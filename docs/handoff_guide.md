# 🔬 LBM-Agent R&D 포탈 프로젝트 인수인계 문서 (Project Handoff Guide)

본 문서는 서울대학교 Connectome Lab의 **Large Brain Model (LBM) - 에이전트 AI 융합 연구 (BAI Framework)** 포탈 구축 및 마이그레이션 프로젝트의 최종 인수인계 및 환경 설명서입니다. 

이 프로젝트는 연구원 및 외부 학생들이 R&D 및 실습 온보딩을 원스톱으로 진행하고, 대외적으로 연구 성과를 성공적으로 공유할 수 있도록 설계되었습니다.

---

## 📂 1. 프로젝트 기본 정보 (General Info)

* **로컬 작업 디렉토리 (Project Folder)**: `/home/juke/git/lbm-agent`
* **공식 GitHub 원격 저장소**: 🔗 [Transconnectome/lbm-agent](https://github.com/Transconnectome/lbm-agent)
* **기준 연구실 Notion 원본 페이지**: 🔗 [Notion Link (36841454561d80db93b1ed512b242af2)](https://www.notion.so/36841454561d80db93b1ed512b242af2)

---

## 🛠️ 2. 핵심 산출물 및 디렉토리 구조 (Key Assets)

리포지토리는 아래와 같은 표준화된 자산 구조로 정비되어 있습니다.

```
/home/juke/git/lbm-agent/
├── readme_claude.md           # [루트] 깃허브 대문 온보딩 게이트웨이 (Chavis 스타일 가이드)
├── notion_mirrored_report.md   # [루트] 노션 대시보드 1:1 미러링 문서 (200% 활용 시나리오 탑재)
├── gallery.html               # [루트] 16:9 슬라이드 인포그래픽 갤러리 뷰어 (HTML 단일 파일)
└── docs/                      # [docs 폴더] R&D 보고서 및 실습 리소스
    ├── handoff_guide.md       # 본 인수인계 문서
    ├── strategic_lbm_agent_ai_report.md  # 융합 전략 연구 종합서
    ├── snu_connectome_student_handout.md # 신입 연구원 실습 온보딩 핸드아웃
    ├── lbm_agent_rag_query_plan.md       # NLM RAG 쿼리 계획서
    ├── lbm_agent_rag_query_results.md    # NLM RAG 쿼리 결과 보고서
    ├── images/                # nanobanana2 API로 빌드된 4K 한글 슬라이드 이미지 리소스
    └── scripts/               # 자동화 및 연동 API 스크립트 폴더
        ├── register_lbm_slides.py  # 메타데이터 슬라이드 등록용 스크립트
        └── create_gmail_drafts.py  # Gmail 임시보관함 연동 빌더 (HTML 초안 생성)
```

---

## 🔬 3. R&D 지식베이스 및 API 인프라 구성

인수 인계자가 연구를 가속하기 위해 파악해야 할 핵심 인프라 설정입니다.

### ① `nlm` RAG 지식베이스
- **노트북 별칭(Alias)**: `lbm-agent`
- **구축 규모**: 330여 개의 대규모 AI/뇌과학 논문 PDF 데이터베이스 완비
- **사용법**: 터미널에서 `nlm query --notebook lbm-agent "질문내용"`을 통해 학술 레퍼런스 조사를 수초 만에 수행 가능

### ② 지메일 초안 빌더 API (`create_gmail_drafts.py`)
- **역할**: 구글 워크스페이스 CLI인 `/home/juke/.npm-global/bin/gws`를 연동하여, 초프리미엄 HTML 형식의 제안 메일 및 요약 메일 2종을 사용자 계정의 임시보관함(Drafts)에 자동 업로드합니다.
- **실행 방법**:
  ```bash
  python3 docs/scripts/create_gmail_drafts.py
  ```
- **생성되는 초안**:
  1. *Graham Neubig 교수 대상 영문 제안서* (오가니제이션 갤러리 및 보고서 링크 액티브 앵커 장착)
  2. *연구실 멤버 대상 국문 요약 메일* (포탈 활용법 4대 꿀팁 카드 및 노션 원본 페이지 링크 액티브 앵커 장착)

---

## 💾 4. 연구실 고유 운영 가이드라인 (Mandatory Rules)

후임 개발자 및 연구원은 연구실의 정체성 및 무결성을 유지하기 위해 다음 세 가지 규칙을 엄격하게 고수해야 합니다:

1. **용어 사용 금지 (Terminology Block)**:
   - 문서, 이메일, 주석 및 구두 커뮤니케이션 시 **"랩실"** 및 **"랩 멤버"**라는 단어를 절대 사용하지 마십시오.
   - 항상 정중하고 깊이 있는 **"연구실"** 또는 **"Connectome Lab"**, **"연구원"**으로 격상시켜 명명하십시오.
2. **링크 상대 경로 무결성 (Zero Absolute Paths)**:
   - 리포지토리 내의 마크다운 파일 간의 이동은 외부 방문자의 에러 방지를 위해 반드시 상대 경로(`docs/snu_connectome_student_handout.md` 등) 체계로 구성해야 하며, 로컬 절대 경로(`file:///home/juke/...`)의 유입을 철저히 차단하십시오.
3. **학술 공헌자 서명**:
   - 모든 대내외 커뮤니케이션 및 학술 가이드 문서의 최하단에는 **`Chavis 올림 (Antigravity v2.0)`**을 일관되게 주입하여 신뢰성을 확보하십시오.

---
* **작성일**: 2026년 5월 23일
* **작성 조력**: Antigravity (Advanced Agentic Coding Assistant, Google DeepMind)
* **인계인수 책임**: SNU Connectome Lab 차지욱 교수 연구팀
