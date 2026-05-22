# 🧠 LBM 기반 차세대 Agent AI 연동 전략 연구 보고서 (Notion Mirrored)

> 📌 **Notion Metadata**
> **작성자**: Antigravity (Google DeepMind)
> **최종 수정일**: 2026-05-22
> **상태**: 🟢 완료 (카탈로그 및 갤러리 등재 필)
> **카테고리**: `AI for Science` / `Neuroscience`
> **프로젝트**: `cha-talks infographics integration`

---

## 💡 Overview

> 💡 **주요 요약 (Executive Summary)**
> 본 문서는 서울대학교 차지욱 교수 연구팀의 **Large Brain Model(LBM) 연구 성과(DIVER, SwiFT, Neural Field Modeling)**와 Graham Neubig 교수의 **OpenHands 및 OSWorld 에이전트 AI**의 융합 전략 연구를 노션 뷰어 형태로 포맷팅한 미러링 문서입니다.
> 
> * **핵심 가치**: 기존 VLM 에이전트의 물리적 한계(Grounding 오차, 추론 지연 등)를 LBM의 Spatiotemporal 뇌 토큰 매핑 및 오류 관련 전위(ErrP) 피드백 루프를 통해 보완하는 **Brain-Agent Interface(BAI)** 프레임워크를 제안합니다.
> * **현실적 제약 반영**: fMRI의 물리적 BOLD 지연(4~6초) 및 EEG의 두개골 노이즈 감쇄 문제를 직시하여 실시간 인터랙션과 장기 맥락 분석을 구분한 **5개년 3단계 로드맵**을 포함합니다.

---

## 📂 핵심 산출물 바로가기 (Notion Bookmarks)

* 📑 **종합 전략 연구 보고서**: [strategic_lbm_agent_ai_report.md](file:///home/juke/.gemini/antigravity-cli/brain/8b0c7e07-72c1-418e-8aa9-392705a5d20b/strategic_lbm_agent_ai_report.md)
* 🖼️ **프리미엄 16:9 슬라이드 갤러리**: [gallery.html](file:///home/juke/git/cha-talks/infographics/gallery.html)
* 🛠️ **자동화 카탈로그 등록 스크립트**: [register_lbm_slides.py](file:///home/juke/.gemini/antigravity-cli/brain/8b0c7e07-72c1-418e-8aa9-392705a5d20b/scratch/register_lbm_slides.py)

---

## 🔽 핵심 기술 메커니즘 (Toggle Lists)

<details>
<summary><b>1️⃣ DIVER-1: Spatio-temporal Attention & any-variate EEG Model (클릭하여 열기)</b></summary>
<div style="padding-left: 20px; margin-top: 10px;">

* **개념**: 시간과 공간 정보를 병렬적으로 처리하지 않고 **Spatio-temporal Attention**과 **Rotary Position Embedding(RoPE)**를 결합하여 뇌의 시공간 동역학을 모델링합니다.
* **장점**: **Sliding Temporal Conditional Positional Encoding(STCPE)**와 **any-variate attention** 메커니즘을 적용하여, 채널의 개수나 전극 위치가 달라지더라도 Permutation & Translation Equivariance를 강건하게 유지합니다.
* **에이전트 기여**: 개발자가 마주하는 극심한 인지 과부하(Workload) 및 실수 시 발생하는 뇌파 상의 **오류 관련 전위(ErrP, Error-Related Potential)**를 SOTA 급 정확도로 검출하여 에이전트의 무한 반복 에러 루프를 초기에 강제 셧다운(Revert)시킬 수 있습니다.
</div>
</details>

<details>
<summary><b>2️⃣ SwiFT: Swin 4D fMRI Transformer (클릭하여 열기)</b></summary>
<div style="padding-left: 20px; margin-top: 10px;">

* **개념**: fMRI의 복잡한 4D spatiotemporal 볼륨을 4D Window Multi-head Self-Attention(4DW-MSA) 및 Shifted Window(4DSW-MSA)를 통해 **선형적 계산 복잡도**로 다룹니다.
* **에이전트 기여**: 뇌 전반의 장기적인 인지적 제어(Cognitive Control) 네트워크와 고차원 주의 집중(Attention Map)의 상태 변화를 포착하여 에이전트에게 뇌파 토큰 형태(`[BRAIN_TOKEN]`)로 컨텍스트를 주입합니다.
</div>
</details>

<details>
<summary><b>3️⃣ Neural Field Modeling (NRF): Implicit Spatial Coding (클릭하여 열기)</b></summary>
<div style="padding-left: 20px; margin-top: 10px;">

* **개념**: fMRI의 이산적 볼륨 그리드(Discrete voxel grid)에서 탈피해, 표준화된 3D MNI 공간 상의 좌표(x, y, z)와 Fourier Positional Encoding을 결합하여 해상도 독립적(resolution-agnostic)인 연속 함수로 신경 표현을 부호화합니다.
* **에이전트 기여**: 사용자의 시각적 타겟 관심도를 연속 필드로 추출하여, OSWorld 에이전트의 75% 실패 지점인 **마우스 클릭 픽셀 오차(Grounding Refinement)를 확률적으로 미세 조정**합니다.
</div>
</details>

---

## 📊 인포그래픽 카탈로그 데이터베이스 (Notion Database View)

| 슬라이드 번호 | 노션 카드 (ID) | 슬라이드 한글 제목 | 핵심 비주얼 장치 | 온톨로지 매핑 (Topic) |
| :--- | :--- | :--- | :--- | :--- |
| Slide 1 | `lbm_agent_s1` | LBM 기반 차세대 Agent AI 연동 전략 표지 | Concept Map | `ai_ml/ai_for_science` |
| Slide 2 | `lbm_agent_s2` | 현재 Agent AI의 3대 핵심 병목과 한계 | 3대 장벽 다이어그램 | `ai_ml/ai_for_science` |
| Slide 3 | `lbm_agent_s3` | DIVER: Spatio-temporal 뇌파 모델 아키텍처 | Permutation Block 구조도 | `neuroscience/brain_imaging` |
| Slide 4 | `lbm_agent_s4` | SwiFT & NRF 비교 분석 | Comparison Table | `neuroscience/brain_imaging` |
| Slide 5 | `lbm_agent_s5` | Brain-Agent Interface (BAI) 메타 인지 폐루프 | Closed-loop Flowchart | `neuroscience/computational_neuro` |
| Slide 6 | `lbm_agent_s6` | 뇌-에이전트 융합 5개년 3단계 전략적 로드맵 | Timeline / Phase | `ai_ml/ai_for_science` |

---

## 🚧 현실적 장벽 및 타개안 (Feasibility Checkbox)

- [x] **fMRI BOLD 지연 (4~6초)**
  - *타개안*: 실시간 제어(마우스 보정, 즉시 롤백)는 EEG(DIVER) 밀리초 수준의 해상도를 사용하고, fMRI(SwiFT/NRF)는 장기적인 작업 맥락 수립 및 인지 과부하 상태 프로파일링에 국한하여 이원화합니다.
- [x] **EEG 신호의 극심한 근전도/움직임 노이즈 (Artifacts)**
  - *타개안*: 타이핑 및 눈 깜빡임 노이즈를 방어하기 위해 pre-processing 경량 필터를 포함하고, BCI 신호를 직접 타자 도구로 쓰기보다 에이전트 루프의 중단/동의 여부 판단 등 '상위 메타 컨트롤러(Meta-Cognitive Controller)'로 작동시킵니다.
- [x] **에이전트의 추론 지연 (Prefill Latency)**
  - *타개안*: 뇌파에서 실시간으로 감지된 사용자 인지 상태에 따라 OpenHands의 컨텍스트 요약 수준(Condensing Intensity)을 동적으로 조율하고, 서브 에이전트에 자율 위임하는 비율을 조절하여 병목을 상쇄합니다.

---

## 📅 5개년 3단계 R&D 로드맵 (Notion Board)

> 📅 **Phase 1: 수동적 뇌파 피드백 적응 (1~2년차)**
> * EEG 기반 실시간 인지 부하 및 Frustration 모니터링 엔진 구축.
> * OpenHands Event Stream 연동을 통해 사용자 피로도 맞춤 자동 컨텍스트 요약 강도 조율.

> 📅 **Phase 2: 능동적 공유 자율성 구축 (3~4년차)**
> * NOBEL/fMRI-LM 기반의 Spatiotemporal 뇌-언어 토큰 얼라인먼트 개발.
> * 자연어 질의 없이 "이 부분을 개선해줘"와 같은 사용자 고차원 인지 흐름 디코딩.

> 📅 **Phase 3: 양방향 공진화 및 실시간 제어 (5년차 이후)**
> * fMRI NRF 연속 필드 기반 실시간 마우스 Grounding 클릭 정밀 보정(PPO 알고리즘 연동).
> * 사용자의 실시간 오류 관련 전위(ErrP) 반응을 패널티/리워드로 활용하는 **뇌 피드백 기반 강화학습(RLHBF)** 구축.
