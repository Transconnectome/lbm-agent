#!/usr/bin/env python3
import base64
import json
import subprocess
import sys
from email.mime.text import MIMEText
from email.header import Header

# GitHub Public URLs for SNU Connectome Transconnectome assets
URL_REPO = "https://github.com/snuconnectome/transconnectome"
URL_STRATEGIC_REPORT = "https://github.com/snuconnectome/transconnectome/blob/main/docs/strategic_lbm_agent_ai_report.md"
URL_NOTION_REPORT = "https://github.com/snuconnectome/transconnectome/blob/main/docs/notion_mirrored_report.md"
URL_QUERY_PLAN = "https://github.com/snuconnectome/transconnectome/blob/main/docs/lbm_agent_rag_query_plan.md"
URL_QUERY_RESULTS = "https://github.com/snuconnectome/transconnectome/blob/main/docs/lbm_agent_rag_query_results.md"
URL_STUDENT_HANDOUT = "https://github.com/snuconnectome/transconnectome/blob/main/docs/snu_connectome_student_handout.md"
URL_GALLERY_HTML = "https://github.com/snuconnectome/transconnectome/blob/main/gallery.html"

# Email Content 1: English (Graham Neubig)
SUBJECT_EN = "📬 [BAI Initiative] Proposal for Integrating Large Brain Models (LBM) with OpenHands & OSWorld 🚀"
TO_EN = "gneubig@cmu.edu"
BODY_EN = f"""Dear Graham,

Greetings from Seoul National University! 🌟 I hope this email finds you with great energy and excitement! 

My research team at the SNU Connectome Lab has been absolute fans of your groundbreaking work on OpenHands and OSWorld. We are tremendously inspired by the rapid evolution of computer-use agents! 🤖✨ 

To take this boundary even further, we would love to propose a collaborative research framework that merges our Large Brain Models (LBM)—specifically DIVER-1 (our spatiotemporal EEG foundation model) and SwiFT (4D fMRI Swin Transformer)—with your agent loop. We term this framework the Brain-Agent Interface (BAI)! 🧠🤝💻

======================================================================
💎 FEASIBILITY BLUEPRINT & SCHOLARLY RESOURCES (GitHub Repository)
======================================================================
All our strategic reports, plans, and slides are now publicly hosted on our research repository:
👉 GitHub Repository: {URL_REPO}

Here are the direct GitHub links for your convenience:
1. 📑 Strategic Integration Report: 
   {URL_STRATEGIC_REPORT}
2. 🔬 Detailed RAG Query Plan (including NLM & Agent RAG Wisdom): 
   {URL_QUERY_PLAN}
3. 🖼️ Premium Visual Slide Gallery: 
   {URL_GALLERY_HTML}
======================================================================

As researchers, we love to be transparent about physical constraints! SwiFT has a 4-6 second hemodynamic latency, and DIVER faces low signal-to-noise ratio challenges in EEG. To bypass these feasibility gaps, we designed a structured 3-phase, 5-year roadmap (from passive neuro-adaptation to active token alignment and closed-loop control). We are very thrilled to discuss these details with you! 🎓🚀

Would you or your team members be available for a brief, casual Zoom chat next week? We would be honored to share our insights and explore how we can build this exciting future together! 🌈✨

Thank you very much for your time, inspiration, and consideration! 

-- (please excuse the brevity)
Chavis 올림 (Antigravity v2.0)

Best,
Chavis (Jiook Cha), PhD
Associate Professor
Department of Psychology
Seoul National University
"""

# Email Content 2: Korean (Lab Members)
SUBJECT_KO = "📬 [대박공유! 🎉] LBM 🧠 - Agent AI 🤖 융합 연구 전략 보고서 & 인포그래픽 갤러리 구축 완료 공유 건 ✨"
TO_KO = "lab@connectome.snu.ac.kr"
BODY_KO = f"""연구실 여러분, 안녕해요! 🌟

드디어 우리 연구실의 자랑스러운 핵심 뇌 파운데이션 모델 성과(DIVER, SwiFT, NRF)와 차세대 에이전트 AI(OpenHands, OSWorld)의 융합 전략 연구 초안이 눈부시게 마무리되어 기쁜 마음으로 공유드립니다! 🎉🚀

우리 랩 멤버들이 피땀 흘려 대규모 데이터로 학습시킨 LBM 백본이 에이전트의 시각-언어 오정렬(Grounding) 실패와 무한 반복 루프 등의 고질적 병목을 해결할 수 있는 엄청난 학술적 돌파구(Brain-Agent Interface)가 될 것이라 확신합니다! 🧠⚡💻

연구의 학술적 엄밀성을 위해, fMRI의 혈류 역학적 지연(4~6초)과 EEG의 근전도 노이즈 한계 등 현실적인 피지빌리티 갭(Feasibility Gaps)을 솔직하게 분석하고 해결하는 5개년 로드맵도 설계해 두었으니 다들 꼭 눈여겨봐 주세요! 🔬💎

======================================================================
🎁 SNU CONNECTOME LAB - LBM AGENT RESEARCH ASSETS
======================================================================
우리 융합 연구의 모든 마크다운 자산과 코드, 슬라이드는 깃허브 공개 리포지토리에 이쁘게 배포해 두었습니다! 
👉 GitHub Repository: {URL_REPO}

아래 개별 GitHub 원격 URL을 클릭해 바로 학위 논문 연구 및 R&D 가속화에 마음껏 활용하기 바랍니다:

1. 📑 노션 요약 문서 (Notion Mirrored Summary):
   {URL_NOTION_REPORT}
2. 📑 상세 전략 보고서 (Strategic Integration Report):
   {URL_STRATEGIC_REPORT}
3. 📑 40대 RAG 정밀 쿼리 계획서 (RAG Query Plan - NLM 연계):
   {URL_QUERY_PLAN}
4. 📑 쿼리 결과 분석 보고서 (RAG Query Results - 30-40대 지혜의 쿼리 결과):
   {URL_QUERY_RESULTS}
5. 📑 대학원생 R&D 실습 핸드아웃 (Student Handout Guide):
   {URL_STUDENT_HANDOUT}
6. 🖼️ 프리미엄 인포그래픽 슬라이드 갤러리 (Infographic Gallery):
   {URL_GALLERY_HTML}
======================================================================

330여 개의 대규모 논문 레퍼런스를 탑재한 RAG 지식베이스(lbm-agent)도 적극 활용하여, 향후 공동 세미나나 해외 협업 제안 시 논리적 깊이를 한층 더해갔으면 좋겠습니다! 🚀🎓

문서들을 즐겁게 읽어보고, 추가하고 싶은 혁신적인 아이디어나 수정이 필요한 부분이 있다면 언제든 유쾌하게 피드백 남겨주기! 💬✨

오늘 하루도 다들 연구 속에서 지적인 즐거움을 가득 느끼길 바랍니다. 파이팅해요! 🔥🌈

-- 
Chavis 올림 (Antigravity v2.0)
"""

def make_raw_message(to, subject, body):
    message = MIMEText(body, 'plain', 'utf-8')
    message['to'] = to
    message['from'] = "Chavis <me>"
    message['subject'] = Header(subject, 'utf-8').encode()
    raw = base64.urlsafe_b64encode(message.as_bytes())
    return raw.decode('utf-8')

def create_draft_via_gws(raw_msg):
    payload = {
        "message": {
            "raw": raw_msg
        }
    }
    
    cmd = [
        "/home/juke/.npm-global/bin/gws",
        "gmail",
        "users",
        "drafts",
        "create",
        "--params", "{\"userId\": \"me\"}",
        "--json", json.dumps(payload)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        resp = json.loads(result.stdout)
        print(f"✅ Success! Created draft with ID: {resp.get('id')}")
        return resp
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to execute gws CLI: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def main():
    print("=== Re-creating Emojified Gmail Drafts with transconnectome repo links via gws ===")
    
    # 1. Draft for Graham Neubig
    print("\n[1/2] Re-creating draft for Graham Neubig...")
    raw_en = make_raw_message(TO_EN, SUBJECT_EN, BODY_EN)
    create_draft_via_gws(raw_en)
    
    # 2. Draft for Lab Members
    print("\n[2/2] Re-creating draft for SNU Connectome Lab members...")
    raw_ko = make_raw_message(TO_KO, SUBJECT_KO, BODY_KO)
    create_draft_via_gws(raw_ko)
    
    print("\n=== Gmail Drafts Generation finished successfully! ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
