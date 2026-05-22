#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path
from datetime import datetime, timezone

# Add cha-talks infographics to path
sys.path.append("/home/juke/git/cha-talks/infographics")
from catalog import register_entry, Ontology

PROMPT_DIR = Path("/home/juke/.gemini/antigravity-cli/brain/8b0c7e07-72c1-418e-8aa9-392705a5d20b/prompts")
IMAGE_DIR = Path("/home/juke/.gemini/antigravity-cli/brain/8b0c7e07-72c1-418e-8aa9-392705a5d20b/images")

CHA_TALKS_DIR = Path("/home/juke/git/cha-talks/infographics")
CHA_OUTPUT_DIR = CHA_TALKS_DIR / "output"
CHA_PROMPTS_DIR = CHA_TALKS_DIR / "prompts"

SLIDES_DATA = [
    {
        "index": 1,
        "id": "lbm_agent_s1",
        "title_ko": "LBM 기반 차세대 Agent AI 연동 전략",
        "title_en": "Strategic Integration of LBM and Agent AI",
        "topic": "ai_ml/ai_for_science",
        "viz_type": "concept_map",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["lbm", "agent_ai", "neuroscience", "shared_autonomy"],
        "description": "차지욱 교수의 LBM(DIVER, SwiFT, NRF) 연구 성과와 Graham Neubig 교수의 OpenHands 및 OSWorld 에이전트 AI의 융합 전략 연구 표지 인포그래픽"
    },
    {
        "index": 2,
        "id": "lbm_agent_s2",
        "title_ko": "현재 Agent AI의 3대 핵심 병목과 한계",
        "title_en": "Three Key Bottlenecks of Current Agent AI",
        "topic": "ai_ml/ai_for_science",
        "viz_type": "concept_map",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["bottlenecks", "latency", "grounding", "robustness"],
        "description": "OSWorld 벤치마크 기반 컴퓨터 에이전트 루프가 겪는 시각-언어 오정렬(Grounding) 실패율(75%), 극심한 LLM 추론 지연(96%), 비정형 쿼리 취약성(50%) 분석"
    },
    {
        "index": 3,
        "id": "lbm_agent_s3",
        "title_ko": "DIVER: 채널 Permutation Equivariant Spatio-temporal 뇌파 모델",
        "title_en": "DIVER: Channel Equivariant Spatio-temporal EEG Foundation Model",
        "topic": "neuroscience/brain_imaging",
        "viz_type": "concept_map",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["diver", "eeg", "permutation_equivariance", "any_variate"],
        "description": "Spatio-temporal Attention, STCPE, any-variate attention으로 전극 위치가 달라져도 대칭성을 보장하여 제로샷 BCI 일반화를 실현하는 초거대 뇌파 모델 DIVER-1 아키텍처"
    },
    {
        "index": 4,
        "id": "lbm_agent_s4",
        "title_ko": "SwiFT & Neural Field Modeling: 고해상도 뇌 연결망 및 연속 공간 표상",
        "title_en": "SwiFT and Neural Field Modeling for Continuous Brain Representation",
        "topic": "neuroscience/brain_imaging",
        "viz_type": "comparison",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["swift", "nrf", "fmri", "implicit_neural_representation"],
        "description": "4D fMRI 볼륨을 선형적 복잡도로 다루는 SwiFT 아키텍처와, 복셀 그리드를 탈피해 3D MNI 공간 상의 연속적 좌표 기반의 암시적 공간 표상을 실현하는 NRF(Neural Field)의 비교 분석"
    },
    {
        "index": 5,
        "id": "lbm_agent_s5",
        "title_ko": "Brain-Agent Interface (BAI): 뇌 신호 기반 상위 인지 통제 루프",
        "title_en": "Brain-Agent Interface (BAI) Meta-Cognitive Control Loop",
        "topic": "neuroscience/computational_neuro",
        "viz_type": "concept_map",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["bai", "closed_loop", "errp", "cognitive_control"],
        "description": "뇌 토큰과 언어 공간의 정렬(NOBEL, fMRI-LM), 사용자 오류 관련 전위(ErrP) 피드백 기반 자동 Revert 루프, 인지 부하 맞춤 적응형 콘덴서(요약) 및 서브 에이전트 위임 아키텍처"
    },
    {
        "index": 6,
        "id": "lbm_agent_s6",
        "title_ko": "5-Year Roadmap: 뇌-에이전트 융합의 3단계 미래 전략",
        "title_en": "5-Year Strategic Roadmap for Brain-Agent Integration",
        "topic": "ai_ml/ai_for_science",
        "viz_type": "timeline",
        "purpose": "lecture",
        "audience": "expert",
        "tags": ["roadmap", "passive_adaptation", "shared_autonomy", "symbiosis"],
        "description": "1-2년차 수동적 뇌파 모니터링 적응(Passive), 3-4년차 뇌-언어 토큰 정렬 및 고차원 의도 디코딩(Active), 5년차 이후 실시간 클릭 보정 및 뇌파 피드백 강화학습(Symbiotic) 5개년 3단계 로드맵"
    }
]

def main():
    print("=== LBM & Agent AI Infographic Automation Pipeline ===")
    
    # 1. Directories Validation
    CHA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHA_PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 2. Check if all target images are generated
    missing_images = []
    for s in SLIDES_DATA:
        src_img = IMAGE_DIR / f"S{s['index']}_var1.png"
        if not src_img.exists():
            missing_images.append(src_img.name)
            
    if missing_images:
        print(f"❌ Error: Missing generated images: {missing_images}")
        print("Please wait for the background image generation task to complete.")
        return 1
        
    print("✅ All source images found! Starting copying and registration...")
    
    for s in SLIDES_DATA:
        idx = s["index"]
        entry_id = s["id"]
        
        # Paths
        src_img = IMAGE_DIR / f"S{idx}_var1.png"
        dest_img = CHA_OUTPUT_DIR / f"{entry_id}.png"
        
        src_prompt = PROMPT_DIR / f"S{idx}_prompt.md"
        dest_prompt = CHA_PROMPTS_DIR / f"{entry_id}.md"
        
        # 1) Copy Image
        shutil.copy2(src_img, dest_img)
        print(f"  Copied Image: {src_img.name} -> output/{entry_id}.png")
        
        # 2) Copy Prompt
        shutil.copy2(src_prompt, dest_prompt)
        print(f"  Copied Prompt: {src_prompt.name} -> prompts/{entry_id}.md")
        
        # 3) Register Entry to Catalog
        now_iso = datetime.now(timezone.utc).isoformat()
        try:
            entry = register_entry(
                entry_id=entry_id,
                created=now_iso,
                source="file",
                prompt_file=f"prompts/{entry_id}.md",
                outputs=[f"output/{entry_id}.png"],
                aspect_ratio="16:9",
                variants=1,
                tags=s["tags"],
                status="complete",
                cost_usd=0.4,
                topic=s["topic"],
                viz_type=s["viz_type"],
                purpose=s["purpose"],
                audience=s["audience"],
                title_ko=s["title_ko"],
                title_en=s["title_en"],
                description=s["description"]
            )
            print(f"  🎉 Catalog entry created: catalog/entries/{entry_id}.yaml")
        except Exception as e:
            print(f"  ❌ Failed to register catalog entry '{entry_id}': {e}")
            return 1
            
    print("✅ All entries registered successfully in catalog!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
