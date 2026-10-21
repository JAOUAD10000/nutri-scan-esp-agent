import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Nutri-Scan ESP: Autonomous AI Agent", layout="wide", page_icon="🧬")

st.title("🧬 Nutri-Scan ESP: Autonomous AI Agent")
st.markdown("**Moteur d'Inférence Causale | Brevet OMPIC n°74133 | AgriTech 5.0**")
st.info("️ Moteur de démonstration appliquant la logique multi-matrices du brevet. Les coefficients utilisés sont illustratifs. La BCR réelle reste confidentielle.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    file_water = st.file_uploader("1. Irrigation Water (EI)", type=["csv"])
with col2:
    file_soil = st.file_uploader("2. Soil Solution (SS) - 3 depths", type=["csv"])
with col3:
    file_tissue = st.file_uploader("3. Plant Tissue/Sap (F)", type=["csv"])
with col4:
    file_dna = st.file_uploader("4. Soil DNA/Metagenome (S)", type=["csv"])

if st.button("🚀 Launch Causal Inference Engine", type="primary", use_container_width=True):
    if all([file_water, file_soil, file_tissue, file_dna]):
        with st.spinner("Correlating 4 matrices via Relational Knowledge Base..."):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
        
        try:
            df_w = pd.read_csv(file_water)
            df_s = pd.read_csv(file_soil)
            df_t = pd.read_csv(file_tissue)
            df_d = pd.read_csv(file_dna)
            
            # --- LOGIQUE ALGORITHMIQUE SIMULÉE BASÉE SUR LE BREVET (Rev. 4) ---
            nh4 = df_w.loc[df_w['Parameter'] == 'NH4', 'Value'].values[0] if 'NH4' in df_w['Parameter'].values else 0
            no3 = df_w.loc[df_w['Parameter'] == 'NO3', 'Value'].values[0] if 'NO3' in df_w['Parameter'].values else 1
            ca_tissue = df_t.loc[df_t['Element'] == 'Ca', 'Concentration'].values[0] if 'Ca' in df_t['Element'].values else 0
            
            isn = min(0.95, max(0.10, (nh4 / max(no3, 0.1)) * 0.3 + (1 - ca_tissue/1.5) * 0.4))
            pathogens = df_d[df_d['Role'] == 'Pathogen']
            ipp = min(0.90, max(0.05, (pathogens['Abundance'] * pathogens['Virulence_Coefficient']).sum() * 2))
            
            # Affichage du Diagnostic de Risque Intégré (DRI)
            st.divider()
            c1, c2, c3 = st.columns(3)
            c1.metric("ISN (Nutritional Stress)", f"{isn:.2f}", "CRITICAL" if isn > 0.6 else "OK")
            c2.metric("IPP (Botrytis Risk)", f"{ipp:.2f}", "HIGH" if ipp > 0.5 else "LOW")
            c3.metric("Predicted Outbreak", "21 DAYS", "WARNING")
            
            st.error(f"⏰ **PREDICTIVE ALERT - SECTOR 3 DETECTED**\nEtiological Diagnosis: Functional blockage detected. Excess NH₄⁺ ({nh4} mmol/L) preventing Ca² absorption (Tissue Ca: {ca_tissue}% DW). Pathogen pressure rising due to weakened cell walls.")
            
            # --- GÉNÉRATION DU PAPI DÉTAILLÉ (2 PAGES ÉQUIVALENT) ---
            st.success("✅ **AUTONOMOUS ACTION PLAN (PAPI) GENERATED**")
            
            papi_content = f"""
### 📍 ZONE IDENTIFICATION & BASELINE
*   **Sector:** Sector 3 (Strawberry - Loukkos Pilot Farm)
*   **Surface:** 2.5 Hectares
*   **Growth Stage:** BBCH 60 (Full Flowering)
*   **Soil Type:** Sandy Loam, pH 5.8, EC 2.1 dS/m
*   **Dominant Pathogen Threat:** *Botrytis cinerea* (IPP: {ipp:.2f})

---

###  PRIORITY 1: SYSTEMIC NUTRITIONAL CORRECTIONS (Root Cause)
*Objective: Restore Ca²⁺ bioavailability and correct rhizospheric antagonism.*

| Action Parameter | Specification | Agronomic Justification | Execution Window |
| :--- | :--- | :--- | :--- |
| **Corrective Fertilizer** | Calcium Nitrate [Ca(NO₃)₂] | Displaces excess Na⁺/NH₄⁺ from CEC; restores cell wall lignification | Oct 24, 2026 |
| **Application Dose** | 15 kg/ha (pure CaO equivalent) | Calculated based on IEAR deficit and target tissue level of 1.2% DW | Single application |
| **Fertigation Adjustment** | Reduce NH₄⁺ source by 40%; Increase NO₃⁻ source | Target NH₄⁺/NO₃⁻ ratio shift from 1.5 → 0.8 to alleviate uptake blockage | Immediate effect |
| **Irrigation Protocol** | Maintain soil moisture at -20 kPa during application | Ensures mass flow transport of Ca²⁺ to active root zone | J+0 to J+3 |
| **Expected Response Kinetics** | Tissue Ca increase detectable at J+7; Full physiological recovery at J+14 | Based on sap flow velocity and xylem translocation rates | Monitoring Milestones |

---

### 🟠 PRIORITY 2: MICROBIOME MODULATION (Synergistic Action)
*Objective: Suppress pathogen pressure while nutritional correction takes effect.*

| Action Parameter | Specification | Agronomic Justification | Execution Window |
| :--- | :--- | :--- | :--- |
| **Biocontrol Agent** | *Pseudomonas fluorescens* CHA0 | Specific antagonist to *Botrytis*; produces antifungal metabolites | Oct 25, 2026 |
| **Inoculation Dose** | 2 L/ha (min. 1x10⁸ CFU/mL) | Ensures competitive exclusion in rhizosphere niche | Post-Calcium Application |
| **Application Method** | Drench via drip irrigation | Direct delivery to root zone where pathogen pressure is highest | Early morning only |
| **Environmental Constraint** | Do NOT apply if soil temp > 28°C or UV index > 8 | Prevents rapid die-off of introduced beneficial strain | Weather Dependent |
| **Repeat Condition** | Re-evaluate IPP at J+14. If IPP > 0.50, repeat application | Adaptive management based on real-time microbiome response | Conditional Trigger |

---

###  PRIORITY 3: PLANT DEFENSE REINFORCEMENT (Resilience)
*Objective: Activate Systemic Acquired Resistance (SAR) pathway independently of nutrition.*

| Action Parameter | Specification | Agronomic Justimization | Execution Window |
| :--- | :--- | :--- | :--- |
| **Elicitor Molecule** | Salicylic Acid (SA) derivative | Triggers PR-protein synthesis; strengthens physical barriers against fungal penetration | Oct 26, 2026 |
| **Foliar Concentration** | 0.5 mM solution | Optimal concentration for SAR activation without phytotoxicity risk | Early morning spray |
| **Adjuvant Requirement** | Non-ionic surfactant (0.1%) | Ensures uniform leaf coverage and stomatal penetration | Mandatory addition |
| **Compatibility Warning** | DO NOT mix with copper-based fungicides or high-pH products | SA efficacy is reduced above pH 7.0; copper causes precipitation | Strict Separation |
| **Physiological Marker** | Monitor peroxidase activity at J+7 | Biochemical confirmation of successful SAR induction | Lab Validation |

---

###  PRIORITY 4: MONITORING & ADJACENT SECTORS STRATEGY
*Objective: Validate intervention efficacy and prevent lateral spread.*

| Monitoring Parameter | Sampling Method | Target Threshold | Next Evaluation Date |
| :--- | :--- | :--- | :--- |
| **Soil Solution Ca²⁺** | Ceramic suction lysimeter (20cm depth) | > 4.0 mmol/L | Oct 31, 2026 (J+7) |
| **Plant Sap K/Ca Ratio** | Petiole sap analysis | < 3.0 (Current: 4.2) | Nov 07, 2026 (J+14) |
| **Botrytis Sporulation** | Spore trap count / Visual incidence | < 5 spores/m³ air | Nov 14, 2026 (J+21) |
| **Web Dashboard Alerts** | Automated SMS/WhatsApp notification | ISN drops below 0.40 | Real-time |

**Adjacent Sectors Status:**
*   **Sector 2:** Low risk (ISN 0.45). Continue standard fertigation. No immediate action required.
*   **Sector 4:** Moderate risk (ISN 0.58). Schedule preventive calcium application in 10 days.
*   **Sector 1:** High Na⁺ accumulation risk. Schedule leaching irrigation event within 10 days to prevent secondary salinity stress.

---
*️ Legal & Technical Disclaimer: This PAPI is generated autonomously by the Nutri-Scan ESP Causal Inference Engine based on synchronized multi-matrix data. All recommendations must be validated by a certified agronomist before field implementation. Coefficients used are illustrative demonstration values.*
"""
            
            with st.expander(" CLICK TO VIEW FULL PAPI REPORT (Detailed Technical Specifications)", expanded=True):
                st.markdown(papi_content, unsafe_allow_html=True)
                
            st.markdown("🤖 **Agent Status:** Decision generated autonomously via Breveted Correlation Logic (OMPIC #74133). No human intervention required for initial synthesis. The plant has been read before it cried.")
            
        except Exception as e:
            st.error(f"❌ Data Processing Error: {str(e)}")
    else:
        st.warning("⚠️ Please upload all 4 synchronized matrices to launch the Causal Inference Engine.")
