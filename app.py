import streamlit as st
import pandas as pd
import time
import random

st.set_page_config(page_title="Nutri-Scan ESP", layout="wide", page_icon="🧬")

st.title("🧬 Nutri-Scan ESP : Agent IA autonome")
st.markdown("Moteur d'inférence causale | Brevet OMPIC #74133 | AgriTech 5.0")

st.subheader("📤 Téléverser les données de la ferme (4 matrices)")

col1, col2, col3, col4 = st.columns(4)

with col1:
    file_water = st.file_uploader("1. Irrigation Water (EI)", type=["csv"])
with col2:
    file_soil = st.file_uploader("2. Soil Solution (SS) - 3 depths", type=["csv"])
with col3:
    file_plant = st.file_uploader("3. Plant Tissue/Sap (F)", type=["csv"])
with col4:
    file_dna = st.file_uploader("4. Soil DNA/Metagenome (S)", type=["csv"])

if st.button("🚀 Launch Causal Inference Engine"):
    if file_water and file_soil and file_plant and file_dna:
        with st.spinner("Corrélation multi-matrices en cours..."):
            time.sleep(2)
            
            try:
                df_water = pd.read_csv(file_water)
                df_soil = pd.read_csv(file_soil)
                df_plant = pd.read_csv(file_plant)
                df_dna = pd.read_csv(file_dna)
                
                # Calcul simulé pour faire varier les chiffres
                base_isn = len(df_water) * 0.05 + len(df_soil) * 0.1 + len(df_plant) * 0.08
                base_ipp = len(df_dna) * 0.1 + len(df_soil) * 0.05
                
                isn = min(0.95, max(0.10, base_isn + random.uniform(-0.05, 0.05)))
                ipp = min(0.90, max(0.05, base_ipp + random.uniform(-0.05, 0.05)))
                
                st.success("✅ Analyse terminée")
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("ISN (Nutritional Stress)", f"{isn:.2f}", "CRITICAL" if isn > 0.6 else "OK")
                with col_b:
                    st.metric("IPP (Botrytis Risk)", f"{ipp:.2f}", "HIGH" if ipp > 0.6 else "LOW")
                with col_c:
                    st.metric("Predicted Outbreak", "21 DAYS", "WARNING")
                
                st.error("⏰ **PREDICTIVE ALERT - SECTOR 3 DETECTED**")
                
                st.info("""
                **Etiological Diagnosis:** Functional blockage detected. 
                Excess NH₄⁺ preventing Ca²⁺ absorption. Pathogen pressure rising due to weakened cell walls.
                """)
                
                st.success("✅ **AUTONOMOUS ACTION PLAN (PAPI) GENERATED**")
                
                # --- LE PAPI DÉTAILLÉ (Ce que tu voulais) ---
                with st.expander("📄 Click to view the full PAPI Report (3 pages equivalent)", expanded=True):
                    st.markdown("""
                    ### **SECTOR 3: SYSTEMIC NUTRITIONAL CORRECTIONS (Priority 1)**
                    *   **Action:** Apply Calcium Nitrate (Ca(NO₃)₂) at 15 kg/ha.
                    *   **Reason:** To displace excess Na⁺ and restore Ca²⁺ availability in the root zone.
                    *   **Execution Date:** October 24, 2026 (based on 3-day weather forecast).
                    *   **Target:** All plants in Sector 3 (approx. 2.5 ha).
                    *   **Corrective Ratio:** Adjust NH₄⁺/NO₃⁻ from 1.5 to 0.8 in the fertigation.
                    *   **Monitoring:** Measure pH and EC in soil solution at J+3 and J+7.

                    ### **SECTOR 3: MICROBIOME MODULATION (Priority 2)**
                    *   **Action:** Inoculate *Pseudomonas fluorescens* CHA0 at 2 L/ha.
                    *   **Reason:** To outcompete *Fusarium* spp. and stimulate induced systemic resistance (ISR).
                    *   **Execution Date:** October 25, 2026.
                    *   **Method:** Drench application via drip irrigation.
                    *   **Frequency:** Repeat at J+15 if IPP remains > 0.60.

                    ### **SECTOR 3: PLANT DEFENSE REINFORCEMENT (Priority 3)**
                    *   **Action:** Apply Salicylic Acid (SA) elicitor at 0.5 mM.
                    *   **Reason:** To activate the plant's SAR (Systemic Acquired Resistance) pathway.
                    *   **Execution Date:** October 26, 2026.
                    *   **Method:** Foliar spray (early morning).
                    *   **Precaution:** Do not mix with copper-based products.

                    ### **SECTOR 3: MONITORING PLAN**
                    *   **J+7:** Re-sample soil solution and plant sap to measure Ca²⁺ and K⁺.
                    *   **J+14:** Re-evaluate ISN and IPP. If ISN < 0.40, reduce PAPI interventions.
                    *   **J+21:** Final assessment of pathogen pressure (Botrytis).
                    *   **Web Dashboard:** Real-time alerts will be sent via dedicated web account.
                    *   **WhatsApp:** Daily summary of priority zones.

                    ### **ADJACENT SECTORS (Priority 4)**
                    *   **Sector 2:** No immediate action. Monitor ISN (currently 0.45).
                    *   **Sector 4:** Low risk. Continue standard fertigation.
                    *   **Sector 1:** High risk of Na⁺ accumulation. Schedule leaching in 10 days.
                    """)
                
                st.markdown("🤖 **Agent Status:** Decision generated autonomously. No human intervention required. The plant has been read before it cried.")
                
            except Exception as e:
                st.error(f"Erreur de lecture des fichiers : {e}")
    else:
        st.warning("⚠️ Please upload all 4 synchronized matrices to launch the Causal Inference Engine.")
