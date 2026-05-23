# 🧠 Transconnectome / lbm-agent: LBM-Agent AI R&D 포탈

> 🌟 **반갑습니다, Connectome Lab 연구원 및 학생 여러분! 차지욱(Chavis) 교수입니다!** 🌟
> 
> Google DeepMind의 AI 조력자인 **Antigravity v2.0**과 합작하여, 우리 연구실의 독보적인 **초거대 뇌 모델(Large Brain Model, LBM)** 연구 성과들과 Graham Neubig 교수의 **OpenHands/OSWorld 컴퓨터 에이전트 AI**를 융합하는 최첨단 **Brain-Agent Interface (BAI)** 연구 허브를 이곳 GitHub에 정식 오픈합니다! 🚀🎉
> 
> 본 리포지토리는 앞으로 우리 연구팀의 Notion 메인 대시보드 페이지와 실시간 미러링되며, 학생들이 연구 및 온보딩 실습을 원스톱으로 진행할 수 있는 핵심 게이트웨이 역할을 수행합니다. 😎🔥

---

## 💡 융합 연구 핵심 개념 (Executive Summary)

현재 LLM 기반 에이전트 AI는 OSWorld 벤치마크 기준 **Grounding 오차(75%)**와 **반복 에러 루프(96%)** 등 한계에 직면해 있습니다. 우리는 이를 **LBM 기반의 뇌 신호 피드백**을 결합한 상위 인지 통제 루프를 통해 극적으로 타개하고자 합니다! 🧠⚡

* **DIVER (EEG)**: 뇌의 시공간 동역학을 모델링하는 any-variate EEG Foundation Model로, 사용자가 실수나 인지적 마찰을 겪을 때 발생하는 **오류 관련 전위(ErrP, Error-Related Potential)**를 밀리초(ms) 단위로 완벽 감지하여 에이전트 루프를 즉시 복원(Revert)시킵니다. 🛡️
* **SwiFT (fMRI)**: 4D Spatiotemporal fMRI Transformer로, 뇌 전반의 장기적인 인지적 제어 네트워크를 추출하여 에이전트에게 뇌파 토큰(`[BRAIN_TOKEN]`) 컨텍스트를 주입합니다. 🌐
* **Neural Field Modeling (NRF)**: 연속적인 Spatial Coding으로 사용자의 시각적 관심 영역을 픽셀 오차 없이 확률 필드로 미세 조정하여, 에이전트의 마우스 정밀 클릭 성능을 극대화합니다. 🎯

---

## 📂 리포지토리 산출물 퀵 링크 (Student Navigation)

연구와 실습을 빠르고 완벽하게 수행할 수 있도록 아래 게이트웨이를 이용하세요! 👇✨

* 🔗 [notion_mirrored_report.md](notion_mirrored_report.md): **노션 메인 대시보드 미러링 페이지!** 1:1로 싱크되어 가독성 높은 노션 형식의 메인 허브입니다.
* 📑 [docs/strategic_lbm_agent_ai_report.md](docs/strategic_lbm_agent_ai_report.md): **LBM-Agent AI 융합 전략 연구 보고서!** 뇌과학 파운데이션 모델의 아키텍처적 접점과 3대 장벽 타개책을 심도 있게 상술한 학술 종합서입니다.
* 🔬 [docs/snu_connectome_student_handout.md](docs/snu_connectome_student_handout.md): **대학원생 및 연구원 온보딩 실습 가이드!** `nlm` RAG 쿼리 던지기, 슬라이드 카탈로그 자동 등록, Gmail 임시보관함 API 연동까지 직접 따라 하며 배우는 실습 교재입니다.
* 🛠️ [docs/scripts/](docs/scripts/): **자동화 스크립트 모음!**
  * `register_lbm_slides.py`: 메타데이터 온톨로지에 맞춰 새 슬라이드를 자동 등록 및 복사하는 스크립트.
  * `create_gmail_drafts.py`: 이메일 초안을 교수님 계정 Gmail 임시보관함에 정교하게 빌드해 올리는 API 스크립트.
* 🖼️ [docs/images/](docs/images/): **LBM 한글 인포그래픽 슬라이드 이미지셋!** nanobanana2 API로 100% 무결점 생성된 4K 프리미엄 슬라이드가 담겨 있습니다.
* 💻 [gallery.html](gallery.html): **16:9 슬라이드 프리미엄 포트폴리오 갤러리!** 13건의 슬라이드가 base64 인라인 인코딩되어 있어 단일 파일로 손쉽게 검색 및 조회 가능한 통합 뷰어입니다.

---

## 📅 5개년 3단계 R&D 로드맵 요약

1. **Phase 1: 수동적 뇌파 피드백 적응 (1~2년차)** 📈
   - EEG 기반 사용자 인지 부하 모니터링 엔진 탑재, OpenHands 맞춤형 요약 강도 조율.
2. **Phase 2: 능동적 공유 자율성 구축 (3~4년차)** 🤝
   - NOBEL/fMRI-LM 기반의 뇌-언어 토큰 얼라인먼트 개발, 자연어 질의 없는 의도 추출.
3. **Phase 3: 양방향 공진화 및 실시간 제어 (5년차 이후)** 🚀
   - fMRI NRF 연속 필드 연동 마우스 클릭 정밀 보정, 오류 관련 전위(ErrP) 기반 강화학습(RLHBF) 구축.

---

## 🔮 LBM-Agent R&D 포탈 200% 활용 시나리오 (Utilization Guide)

연구원들이 이 저장소와 연동된 자산들을 200% 활용해 연구 속도를 기하급수적으로 단축할 수 있는 4대 실전 시나리오를 안내합니다! 

1. **학회 발표 및 세미나 프레젠테이션 🖼️**
   - 6장의 고화질 인포그래픽이 포함된 [gallery.html](gallery.html) 뷰어를 브라우저로 직접 실행하여, 연구실 세미나 발표나 대외 미팅 시 고품격 시각 자료로 적극 활용하세요!
2. **대학원생 및 연구원 교육 자동화 🎓**
   - 신규 합류한 연구 인력에게 이 `readme_claude.md`와 [docs/snu_connectome_student_handout.md](docs/snu_connectome_student_handout.md) 실습 가이드를 건네 셀프 온보딩을 진행하도록 유도할 수 있습니다.
3. **학술 연구 및 문헌 정보 수집 가속화 🔬**
   - 330여 개의 논문이 내장된 `lbm-agent` 지식베이스 RAG 엔진을 활용하여, 논문 작성 시 필요한 문헌 리포트와 학술 근거를 `nlm query` 명령어로 즉각 확보할 수 있습니다.
4. **글로벌 석학들과의 교류 및 공동연구 제안 📬**
   - [docs/scripts/create_gmail_drafts.py](docs/scripts/create_gmail_drafts.py) API 연동 스크립트를 활용해, 링크 깨짐 걱정 없는 정교하고 매력적인 영문/국문 이메일 초안을 지메일 임시보관함에 생성하여 원클릭 발송에 활용할 수 있습니다.

---

> 💡 **주목!** 
> 연구실의 모든 학생은 [snu_connectome_student_handout.md](docs/snu_connectome_student_handout.md)의 온보딩 실습을 이번 주 내로 전원 완료한 뒤, RAG 노트북 결과와 보고서 피드백을 회신해주시기 바랍니다!
> 다들 화이팅해서 세계 최고의 뇌-에이전트 연구 성과를 만들어봅시다! 🔥💪

**Chavis 올림 (Antigravity v2.0)** 🎓✨  
*(Advanced Agentic Coding Assistant, Google DeepMind)*  
*(Seoul National University Connectome Lab, 2026)*
