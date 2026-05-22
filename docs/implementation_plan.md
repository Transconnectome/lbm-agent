# Implementation Plan - LBM & Agent AI Deep Research and Knowledgebase

이 계획은 차지욱 교수의 **Large Brain Model (LBM - DIVER, SwiFT, Neural Field Modeling)** 연구를 정교하게 파악하고, 이를 **Agent AI**의 시대적 조류 및 **Graham Neubig 교수의 OpenHands(구 OpenDevin)** 등 컴퓨터 에이전트 도구와 결합하기 위한 미래 전략 보고서를 작성하고, 이를 시각화한 프리미엄 한국어 인포그래픽 슬라이드를 제작하는 혁신적인 연구 워크플로우를 담고 있습니다.

이를 위해 **Google NotebookLM CLI (`nlm`)**의 강력한 Deep Research 및 노트북 소스 통합 기능과 **`infographics` 스킬(nanobanana2 이미지 생성 API)**을 총동원하여 150개 이상의 논문이 집약된 지식베이스를 구축하고 최고 수준의 분석 리포트를 도출합니다.

---

## Proposed Changes

### 1. Research & Knowledgebase 구축 (NotebookLM `nlm`)
- **[NEW] 노트북 생성**: `nlm notebook create "LBM-Agent-AI-Research"`를 통해 통합 노트북을 생성합니다.
- **별칭(Alias) 등록**: 관리의 편리성을 위해 `lbm-agent` 별칭을 지정합니다.
- **로컬 논문 소스 추가**: `/home/juke/jiook_cha_papers_download/out_*/papers/*.pdf` 등 기존 Connectome Lab 논문들을 노트북 소스로 추가합니다 (`nlm source add`).
- **Deep Research를 통한 소스 대량 확장**:
  - 아래 6가지 핵심 연구 주제에 대해 `nlm research start --mode deep --auto-import`를 실행하여 각 쿼리당 30~40개의 최신 웹 소스 및 논문을 발굴하고 노트북에 자동으로 밀어넣습니다.
    1. *DIVER fully channel equivariant EEG foundation model neural dynamics*
    2. *SwiFT Swin 4D fMRI Transformer brain network representation*
    3. *Neural field modeling functional neuroimaging implicit representation*
    4. *Agent AI LLM computer agents SWE-agent tool use OSWorld*
    5. *Graham Neubig OpenHands software engineering agent benchmark*
    6. *Brain-computer interface Large Brain Model for cognitive control and agent guidance*
  - 이를 통해 총 **150개 이상의 최신 논문 및 학술 소스**로 가득 찬 강력한 Knowledgebase를 구축합니다.

### 2. 다차원 쿼리 및 분석 (Cross-Query with Deep Research)
- 구축된 노트북에 `nlm query`를 사용하여 질문을 던지는 동시에, 최신 웹 정보를 얻기 위해 `nlm research start --mode deep` 또는 외부 Deep Research를 병렬 구동하여 지식의 깊이를 극대화합니다.
- **핵심 질문 영역**:
  - DIVER(EEG), SwiFT(fMRI), Neural Field Modeling 각각의 혁신성 및 LBM(Large Brain Model)으로서의 통합 시너지.
  - Agent AI 단계(기존 LLM 기반 에이전트에서 생체/인지 신호 기반 에이전트로의 진화)로 나아가기 위한 중대한 Research Questions 및 Challenges.
  - Graham Neubig 교수의 OpenHands 및 SWE-agent와 같은 실질적 도구에 LBM이 기여할 수 있는 아키텍처적 접점 (예: 인간의 실시간 인지 통제 신호(fMRI/EEG)를 결합한 에이전트 정렬, BCI-Agent 하이브리드 제어 루프).
  - LBM 기반 에이전트 생태계를 개척하기 위한 장기적 연구 로드맵 및 구체적 준비 전략.

### 3. 전략 연구 보고서 작성 (Strategic Research Report)
- **[NEW] 보고서 파일**: `/home/juke/.gemini/antigravity-cli/brain/8b0c7e07-72c1-418e-8aa9-392705a5d20b/strategic_lbm_agent_ai_report.md`
- 노트북 쿼리 결과 및 최신 딥 리서치 내용을 집대성하여, 학술적 깊이와 비즈니스적 통찰을 모두 갖춘 종합 보고서를 작성합니다.

### 4. 프리미엄 한국어 인포그래픽 슬라이드 제작 (`infographics` 스킬)
- **콘텐츠 분석 및 프롬프트 생성**: 전략 보고서의 핵심 메시지, 킬러 메트릭, 논리 흐름을 추출하여 슬라이드별(약 5-7장) nanobanana2 전용 프롬프트 마크다운 파일을 생성합니다.
- **이미지 생성 및 렌더링**: 테마 규칙에 따라 디자인 품질을 자가 검증한 후, `generate_image.py`를 호출하여 4K 해상도의 미려하고 현대적인 16:9 한글 인포그래픽 이미지들을 생성합니다.
- **갤러리 구축**: 최종 생성된 이미지들을 카탈로그에 등록하고 HTML 갤러리를 빌드하여 시각적으로 쉽게 이해할 수 있는 리포트 슬라이드셋을 제공합니다.

---

## Verification Plan

### Automated Tests & CLI Verification
1. **노트북 및 소스 유효성 확인**:
   - `nlm notebook list` 및 `nlm source list lbm-agent`를 실행하여 150개 이상의 소스가 정상 수집 및 업로드되었는지 확인합니다.
2. **지식 쿼리 동작성 확인**:
   - `nlm query lbm-agent --quiet "DIVER vs SwiFT"` 등을 실행하여 RAG 검색 엔진이 정상 동작하는지 검증합니다.
3. **인포그래픽 이미지 생성 검증**:
   - 이미지 생성 로그 및 결과 디렉토리 내 `.png` 이미지 생성 여부를 확인합니다.
   - `catalog.py verify`를 통해 카탈로그 무결성을 검사합니다.

### Manual Verification
- 생성된 종합 보고서(`strategic_lbm_agent_ai_report.md`)와 HTML 슬라이드 갤러리의 레이아웃 완성도 및 뇌과학-AI 융합 통찰의 정교함을 최종 리뷰합니다.
