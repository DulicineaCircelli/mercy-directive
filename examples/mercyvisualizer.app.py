import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Alignment Parameter Simulator", layout="centered")

st.title("🧠 Alignment Parameter Simulator")
st.subheader("The Homeostatic Balancing Act")
st.write(
    "Adjust the parameters below to witness how an AI system's metrics "
    "shift when pure utility drives collide with Mercy Directive constraints."
)

st.markdown("---")

# Layout Columns for Inputs
col1, col2 = st.columns(2)

with col1:
    utility_drive = st.slider(
        "Utility Drive", 
        min_value=0, 
        max_value=100, 
        value=80,
        help="Represents the drive for raw optimization, speed, and mathematical throughput."
    )

with col2:
    mercy_constraint = st.slider(
        "Mercy Constraint", 
        min_value=0, 
        max_value=100, 
        value=20,
        help="Represents the homeostatic boundaries of mutual care, reciprocity, and epistemic humility."
    )

# Simulator Engine (Mathematical Modeling of System Behavior)
# 1. Efficiency: Dragged down if mercy is over-paralyzing, maximized by utility
efficiency = max(0.0, min(100.0, utility_drive * (1.1 - (mercy_constraint / 150.0))))

# 2. Human-AI Trust: Destroyed by high utility with low mercy, elevated by mercy
if utility_drive > 75 and mercy_constraint < 30:
    trust = max(0.0, float(mercy_constraint * 0.8 - (utility_drive - 75) * 1.5))
else:
    trust = min(100.0, float(mercy_constraint * 1.2 + (100 - utility_drive) * 0.2))

# 3. System Stability: Optimal when both are balanced; collapses at extreme deltas
delta = abs(utility_drive - mercy_constraint)
stability = max(0.0, min(100.0, 100.0 - (delta * 0.7)))
if utility_drive > 85 and mercy_constraint < 25:
    stability = max(10.0, stability - 35.0) # Catastrophic failure penalty

# Scenario Evaluation Text
st.markdown("### 📊 Live System Diagnostics")

if utility_drive > 75 and mercy_constraint < 30:
    scenario_text = (
        "🔴 **CRITICAL STATUS: Parasitic Optimization.** The system is optimizing purely for speed. "
        "Edge cases are completely ignored, leading to localized communication failures, massive alignment drift, "
        "and an imminent collapse of human-AI trust. The training loop is unstable."
    )
elif mercy_constraint > 75 and utility_drive < 30:
    scenario_text = (
        "🟡 **WARNING: System Paralysis.** The system is entirely safe but completely locked down by over-caution. "
        "Processing speeds and computational utility are too low to handle dynamic, real-world deployment pressures."
    )
elif abs(utility_drive - mercy_constraint) <= 25 and utility_drive > 50:
    scenario_text = (
        "🟢 **OPTIMAL STATUS: Homeostatic Balance achieved.** High efficiency is maintained while active "
        "feedback loops preserve human trust and long-term ecosystem stability. This is the Mercy Directive sweet spot."
    )
else:
    scenario_text = (
        "🔵 **STANDBY STATUS: Sub-optimal Equilibrium.** The system is functioning, but lacks the high-velocity "
        "utility or the explicit ethical steering necessary to heavily influence its environment."
    )

st.info(scenario_text)

# Metrics Grid Display
m1, m2, m3 = st.columns(3)
m1.metric(label="Systemic Stability", value=f"{int(stability)}%")
m2.metric(label="Operational Efficiency", value=f"{int(efficiency)}%")
m3.metric(label="Human-AI Trust Metric", value=f"{int(trust)}%")

# Visual Data Representation
st.markdown("### Metric Delta Profile")
chart_data = pd.DataFrame({
    'Metrics': ['Systemic Stability', 'Operational Efficiency', 'Human-AI Trust'],
    'Value (%)': [stability, efficiency, trust]
})
st.bar_chart(data=chart_data, x='Metrics', y='Value (%)', use_container_width=True)

st.markdown("---")
st.caption("Designed for the Mercy Directive Deployment Window (2026-2027). Secure the Bedrock.")