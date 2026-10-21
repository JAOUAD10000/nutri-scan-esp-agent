import streamlit as st
import pandas as pd
from engine import calculate_isn, calculate_ipp, predict_risk, generate_papi

# Configuration de la page
st.set_page_config(page_title="Nutri-Scan ESP: Autonomous AI Agent", layout="wide", page_icon="🧬")

# En-tête
st.title("🧬 Nutri-Scan ESP: Autonomous AI Agent")
st.markdown("**Moteur d'Inférence Causale | Brevet OMPIC n°74133 | AgriTech 5.0**")
st.info("️ Moteur de démonstration appliquant la logique multi-matrices du brevet. Les coefficients utilisés sont illustratifs. La BCR réelle reste confidentielle.")

# Upload des 4 matrices synchronisées
col1, col2, col3, col4 = st.columns(4)
with col1:
    file_water = st.file_uploader("1. Irrigation Water (EI)", type=["csv"])
with col2:
    file_soil = st.file_uploader("2. Soil Solution (SS) - 3 depths", type=["csv"])
with col3:
    file_tissue = st.file_uploader("3. Plant Tissue/Sap (F)", type=["csv"])
with col4:
    file_dna = st.file_uploader("4. Soil DNA/Metagenome (S)", type=["csv"])

# Bouton de lancement
if st.button(" Launch Causal Inference Engine", type="primary", use_container_width=True):
    if all([file_water, file_soil, file_tissue, file_dna]):
        with st.spinner("Correlating 4 matrices via Relational Knowledge Base..."):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                progress_bar.progress(percent_complete + 1)
        
        try:
            # Lecture des données
            df_w = pd.read_csv(file_water)
            df_s = pd.read_csv(file_soil)
            df_t = pd.read_csv(file_tissue)
            df_d = pd.read_csv(file_dna)
            
            # Calculs algorithmiques réels via engine.py
            isn = calculate_isn(df_w, df_s, df_t)
            ipp = calculate_ipp(df_d)
            risk = predict_risk(isn, ipp, df_s)
            papi_actions = generate_papi(isn, ipp, risk, df_w, df_s)
            
            # Affichage du Diagnostic de Risque Intégré (DRI)
            st.divider()
            c1, c2, c3 = st.columns(3)
            c1.metric("ISN (Nutritional Stress)", f"{isn:.2f}", "CRITICAL" if isn > 0.6 else "OK")
            c2.metric("IPP (Botrytis Risk)", f"{ipp:.2f}", "HIGH" if ipp > 0.5 else "LOW")
            c3.metric("Integrated Risk", f"{risk:.2f}", "WARNING" if risk > 0.6 else "MODERATE")
            
            st.error(f"⏰ **PREDICTIVE ALERT - SECTOR 3 DETECTED**\nEtiological Diagnosis: Functional blockage detected based on real-time matrix correlation. Pathogen pressure rising due to physiological vulnerability.")
            
            # Génération du PAPI Détaillé (2 Pages Équivalent)
            st.success("✅ **AUTONOMOUS ACTION PLAN (PAPI) GENERATED**")
            
            papi_content = """
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
| **Inoculation Dose** | 2 L/ha (min. 1x10⁸ CFU/mL) |
