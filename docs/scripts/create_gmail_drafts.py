#!/usr/bin/env python3
import base64
import json
import subprocess
import sys
from email.mime.text import MIMEText
from email.header import Header

# GitHub Public URLs for SNU Connectome Transconnectome assets
URL_REPO = "https://github.com/Transconnectome/lbm-agent"
URL_LIVE_NOTION = "https://www.notion.so/36841454561d80db93b1ed512b242af2"
URL_STRATEGIC_REPORT = "https://github.com/Transconnectome/lbm-agent/blob/main/docs/strategic_lbm_agent_ai_report.md"
URL_NOTION_REPORT = "https://github.com/Transconnectome/lbm-agent/blob/main/notion_mirrored_report.md"
URL_QUERY_PLAN = "https://github.com/Transconnectome/lbm-agent/blob/main/docs/lbm_agent_rag_query_plan.md"
URL_QUERY_RESULTS = "https://github.com/Transconnectome/lbm-agent/blob/main/docs/lbm_agent_rag_query_results.md"
URL_STUDENT_HANDOUT = "https://github.com/Transconnectome/lbm-agent/blob/main/docs/snu_connectome_student_handout.md"
URL_GALLERY_HTML = "https://github.com/Transconnectome/lbm-agent/blob/main/gallery.html"

# Email Content 1: English (Graham Neubig) - HTML Formatted
SUBJECT_EN = "📬 [BAI Initiative] Proposal for Integrating Large Brain Models (LBM) with OpenHands & OSWorld 🚀"
TO_EN = "gneubig@cmu.edu"
BODY_EN = f"""
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 650px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color: #2d3748; line-height: 1.7;">
  <div style="background: linear-gradient(135deg, #6b46c1 0%, #805ad5 100%); padding: 32px; text-align: center; color: #ffffff;">
    <h1 style="margin: 0; font-size: 24px; font-weight: 800; letter-spacing: -0.5px;">📬 Brain-Agent Interface (BAI) Initiative</h1>
    <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 14px;">Integrating Large Brain Models with OpenHands & OSWorld</p>
  </div>
  <div style="padding: 32px;">
    <p>Dear Graham,</p>
    <p>Greetings from Seoul National University! 🌟 I hope this email finds you with great energy and excitement!</p>
    <p>My research team at the SNU Connectome Lab has been absolute fans of your groundbreaking work on <strong>OpenHands</strong> and <strong>OSWorld</strong>. We are tremendously inspired by the rapid evolution of computer-use agents! 🤖✨</p>
    <p>To take this boundary even further, we would love to propose a collaborative research framework that merges our Large Brain Models (LBM)—specifically <strong>DIVER-1</strong> (our spatiotemporal EEG foundation model) and <strong>SwiFT</strong> (4D fMRI Swin Transformer)—with your agent loop. We term this framework the <strong>Brain-Agent Interface (BAI)</strong>! 🧠🤝💻</p>
    
    <div style="margin: 32px 0; padding: 24px; background-color: #f7fafc; border: 1px solid #edf2f7; border-radius: 8px;">
      <h3 style="margin-top: 0; margin-bottom: 16px; color: #4a5568; font-size: 16px; font-weight: 700; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">💎 Feasibility Blueprint & Scholarly Resources</h3>
      <p style="font-size: 14px; margin-top: 0;">All our strategic reports, plans, and slides are now publicly hosted on our research repository:</p>
      
      <table style="width: 100%; border-collapse: collapse; margin-top: 16px;">
        <tr style="border-bottom: 1px solid #edf2f7;">
          <td style="padding: 12px 0; font-size: 14px; font-weight: 600; color: #4a5568; width: 40%;">📁 GitHub Repository</td>
          <td style="padding: 12px 0; text-align: right;"><a href="{URL_REPO}" style="color: #6b46c1; text-decoration: none; font-weight: 700; border-bottom: 1.5px solid #6b46c1;">Transconnectome/lbm-agent 🚀</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #edf2f7;">
          <td style="padding: 12px 0; font-size: 14px; font-weight: 600; color: #4a5568;">📑 Strategic Integration Report</td>
          <td style="padding: 12px 0; text-align: right;"><a href="{URL_STRATEGIC_REPORT}" style="color: #6b46c1; text-decoration: none; font-weight: 700; border-bottom: 1.5px solid #6b46c1;">Read Report 📑</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #edf2f7;">
          <td style="padding: 12px 0; font-size: 14px; font-weight: 600; color: #4a5568;">🔬 RAG Query Plan</td>
          <td style="padding: 12px 0; text-align: right;"><a href="{URL_QUERY_PLAN}" style="color: #6b46c1; text-decoration: none; font-weight: 700; border-bottom: 1.5px solid #6b46c1;">View RAG Wisdom 🔬</a></td>
        </tr>
        <tr>
          <td style="padding: 12px 0; font-size: 14px; font-weight: 600; color: #4a5568;">🖼️ Visual Slide Gallery</td>
          <td style="padding: 12px 0; text-align: right;"><a href="{URL_GALLERY_HTML}" style="color: #ffffff; background-color: #6b46c1; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-weight: 700; font-size: 13px; display: inline-block;">Open Infographics 🖼️</a></td>
        </tr>
      </table>
    </div>
    
    <p>As researchers, we love to be transparent about physical constraints! SwiFT has a 4-6 second hemodynamic latency, and DIVER faces low signal-to-noise ratio challenges in EEG. To bypass these feasibility gaps, we designed a structured 3-phase, 5-year roadmap (from passive neuro-adaptation to active token alignment and closed-loop control). We are very thrilled to discuss these details with you! 🎓🚀</p>
    <p>Would you or your team members be available for a brief, casual Zoom chat next week? We would be honored to share our insights and explore how we can build this exciting future together! 🌈✨</p>
    <p>Thank you very much for your time, inspiration, and consideration!</p>
    
    <hr style="border: 0; border-top: 1px solid #edf2f7; margin: 32px 0;">
    
    <div style="font-size: 14px; color: #718096;">
      <p style="margin: 0; font-style: italic;">-- (please excuse the brevity)</p>
      <p style="margin: 4px 0 0 0; font-weight: 700; color: #6b46c1;">Chavis 올림 (Antigravity v2.0)</p>
      <p style="margin: 12px 0 0 0; line-height: 1.4; font-size: 13px;">
        <strong>Chavis (Jiook Cha), PhD</strong><br>
        Associate Professor<br>
        Department of Psychology<br>
        Seoul National University
      </p>
    </div>
  </div>
</div>
"""

# Email Content 2: Korean (Lab Members) - HTML Formatted
SUBJECT_KO = "📬 [대박공유! 🎉] LBM 🧠 - Agent AI 🤖 융합 연구 전략 보고서 & 인포그래픽 갤러리 구축 완료 공유 건 ✨"
TO_KO = "lab@connectome.snu.ac.kr"
BODY_KO = f"""
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 650px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color: #2d3748; line-height: 1.7;">
  <div style="background: linear-gradient(135deg, #8e44ad 0%, #9b59b6 100%); padding: 32px; text-align: center; color: #ffffff;">
    <h1 style="margin: 0; font-size: 24px; font-weight: 800; letter-spacing: -0.5px;">🧠 LBM - Agent AI 융합 연구 포탈 오픈</h1>
    <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 14px;">SNU Connectome Lab R&D Assets & Playbook</p>
  </div>
  <div style="padding: 32px;">
    <p style="font-size: 16px; font-weight: 700; color: #8e44ad;">연구실 여러분, 안녕해요! 🌟</p>
    <p>드디어 우리 연구실의 자랑스러운 핵심 뇌 파운데이션 모델 성과(DIVER, SwiFT, NRF)와 차세대 에이전트 AI(OpenHands, OSWorld)의 융합 전략 연구 초안이 눈부시게 마무리되어 기쁜 마음으로 공유드립니다! 🎉🚀</p>
    <p>우리 연구원들이 피땀 흘려 대규모 데이터로 학습시킨 LBM 백본이 에이전트의 시각-언어 오정렬(Grounding) 실패와 무한 반복 루프 등의 고질적 병목을 해결할 수 있는 엄청난 학술적 돌파구(Brain-Agent Interface)가 될 것이라 확신합니다! 🧠⚡💻</p>
    <p>연구의 학술적 엄밀성을 위해, fMRI의 혈류 역학적 지연(4~6초)과 EEG의 근전도 노이즈 한계 등 현실적인 피지빌리티 갭(Feasibility Gaps)을 솔직하게 분석하고 해결하는 5개년 로드맵도 설계해 두었으니 다들 꼭 눈여겨봐 주세요! 🔬💎</p>
    
    <div style="margin: 32px 0; padding: 24px; background-color: #fdfefe; border: 1px solid #ebf5fb; border-radius: 8px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.01);">
      <h3 style="margin-top: 0; margin-bottom: 16px; color: #2980b9; font-size: 16px; font-weight: 700; border-bottom: 2px solid #d4e6f1; padding-bottom: 8px;">🎁 SNU Connectome Lab - LBM Agent Research Assets</h3>
      <p style="font-size: 14px; margin-top: 0;">우리 융합 연구의 모든 마크다운 자산과 코드, 슬라이드는 깃허브 공개 리포지토리에 이쁘게 배포해 두었습니다!</p>
      
      <div style="background-color: #eaf2f8; padding: 12px; border-radius: 6px; margin-bottom: 16px; font-size: 14px; text-align: center;">
        <strong>👉 GitHub Repository:</strong> <a href="{URL_REPO}" style="color: #2980b9; font-weight: 700; text-decoration: none; border-bottom: 1.5px solid #2980b9;">Transconnectome/lbm-agent 🚀</a>
      </div>

      <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e; width: 60%;">1. 🔗 실시간 연구실 Notion 페이지</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_LIVE_NOTION}" style="color: #e74c3c; font-weight: 700; text-decoration: none; border-bottom: 1.5px solid #e74c3c;">Notion 바로가기 🔗</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">2. 📑 노션 깃허브 미러 요약서</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_NOTION_REPORT}" style="color: #8e44ad; font-weight: 700; text-decoration: none;">GitHub Mirror 📑</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">3. 📑 상세 전략 보고서</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_STRATEGIC_REPORT}" style="color: #8e44ad; font-weight: 700; text-decoration: none;">Read Report 📑</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">4. 📑 40대 RAG 정밀 쿼리 계획서</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_QUERY_PLAN}" style="color: #8e44ad; font-weight: 700; text-decoration: none;">Query Plan 🔬</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">5. 📑 쿼리 결과 분석 보고서</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_QUERY_RESULTS}" style="color: #8e44ad; font-weight: 700; text-decoration: none;">RAG Results 📊</a></td>
        </tr>
        <tr style="border-bottom: 1px solid #f2f4f4;">
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">6. 📑 연구원 R&D 실습 핸드아웃</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_STUDENT_HANDOUT}" style="color: #8e44ad; font-weight: 700; text-decoration: none;">Student Guide 🎓</a></td>
        </tr>
        <tr>
          <td style="padding: 10px 0; font-weight: 600; color: #34495e;">7. 🖼️ 프리미엄 인포그래픽 갤러리</td>
          <td style="padding: 10px 0; text-align: right;"><a href="{URL_GALLERY_HTML}" style="color: #ffffff; background-color: #8e44ad; padding: 5px 10px; border-radius: 4px; text-decoration: none; font-weight: 700; font-size: 12px; display: inline-block;">Open Gallery 🖼️</a></td>
        </tr>
      </table>
    </div>

    <div style="margin: 32px 0; padding: 24px; background-color: #fdf9e7; border-left: 4px solid #f39c12; border-radius: 0 8px 8px 0;">
      <h3 style="margin-top: 0; margin-bottom: 12px; color: #d35400; font-size: 15px; font-weight: 700;">💡 [꿀팁! 🍯] 이 융합 포탈과 자산들을 200% 활용하는 4가지 방법:</h3>
      <ol style="margin: 0; padding-left: 20px; font-size: 14px; color: #5d4037;">
        <li style="margin-bottom: 10px;"><strong>학회 발표 및 해외 협업 제안 시 시각적 프레젠테이션 활용 🖼️</strong><br>6장의 16:9 슬라이드 인포그래픽이 포함된 <a href="{URL_GALLERY_HTML}" style="color: #d35400; font-weight: 700; text-decoration: none; border-bottom: 1px solid #d35400;">gallery.html</a>을 브라우저로 열어 세미나나 해외 협업 미팅 시 화면에 띄우고 즉석 발표에 적극 활용하세요!</li>
        <li style="margin-bottom: 10px;"><strong>신입 연구원 및 대학원생 온보딩 자동화 🎓</strong><br>신규 멤버 유입 시 <a href="{URL_REPO}/blob/main/readme_claude.md" style="color: #d35400; font-weight: 700; text-decoration: none; border-bottom: 1px solid #d35400;">readme_claude.md</a>와 <a href="{URL_STUDENT_HANDOUT}" style="color: #d35400; font-weight: 700; text-decoration: none; border-bottom: 1px solid #d35400;">docs/snu_connectome_student_handout.md</a>를 제공하여 RAG 쿼리 실습부터 이메일 API 연동까지 하루 만에 빠르게 기초 학습을 마치도록 지도할 수 있습니다.</li>
        <li style="margin-bottom: 10px;"><strong>초고속 학술 연구 및 문헌 조사 가속화 (RAG Query) 🔬</strong><br>우리 연구실이 탑재한 330여 개의 대규모 최신 LBM-Agent 관련 논문 지식베이스(lbm-agent)를 'nlm query'로 돌려 논문 작성 및 특허 전략 수립 시 문헌 조사 속도를 비약적으로 단축하세요!</li>
        <li style="margin-bottom: 0;"><strong>글로벌 석학 네트워킹 (Gmail API 연동) 📬</strong><br>Gmail 임시보관함에 연동 빌드된 메일 초안을 열어 해외 대가(예: Graham Neubig 교수팀)들에게 원클릭으로 정교하고 세련된 제안 메일을 즉각 발송하는 데 활용할 수 있습니다.</li>
      </ol>
    </div>

    <p>330여 개의 대규모 논문 레퍼런스를 탑재한 RAG 지식베이스(lbm-agent)도 적극 활용하여, 향후 공동 세미나나 해외 협업 제안 시 논리적 깊이를 한층 더해갔으면 좋겠습니다! 🚀🎓</p>
    <p>문서들을 즐겁게 읽어보고, 추가하고 싶은 혁신적인 아이디어나 수정이 필요한 부분이 있다면 언제든 유쾌하게 피드백 남겨주기! 💬✨</p>
    <p>오늘 하루도 다들 연구 속에서 지적인 즐거움을 가득 느끼길 바랍니다. 파이팅해요! 🔥🌈</p>
    
    <hr style="border: 0; border-top: 1px solid #f2f4f4; margin: 32px 0;">
    
    <div style="font-size: 14px; color: #7f8c8d;">
      <p style="margin: 0; font-weight: 700; color: #8e44ad;">Chavis 올림 (Antigravity v2.0)</p>
      <p style="margin: 4px 0 0 0; font-size: 12px; opacity: 0.8;">Seoul National University Connectome Lab & Google DeepMind</p>
    </div>
  </div>
</div>
"""

def make_raw_message(to, subject, body):
    # Send as HTML format
    message = MIMEText(body, 'html', 'utf-8')
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
    print("=== Re-creating Emojified HTML Gmail Drafts with transconnectome repo links via gws ===")
    
    # 1. Draft for Graham Neubig
    print("\n[1/2] Re-creating HTML draft for Graham Neubig...")
    raw_en = make_raw_message(TO_EN, SUBJECT_EN, BODY_EN)
    create_draft_via_gws(raw_en)
    
    # 2. Draft for Lab Members
    print("\n[2/2] Re-creating HTML draft for SNU Connectome Lab members...")
    raw_ko = make_raw_message(TO_KO, SUBJECT_KO, BODY_KO)
    create_draft_via_gws(raw_ko)
    
    print("\n=== Gmail HTML Drafts Generation finished successfully! ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
