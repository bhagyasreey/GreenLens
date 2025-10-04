```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Green Lens - AI Sustainability Toolkit", layout="wide")

st.markdown("""
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: #2d3748;
    background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
}
h1, h2, h3, h4 {
    color: #1a5a3a;
}
.highlight {
    background: linear-gradient(120deg, #4caf50 0%, #81c784 100%);
    padding: 2px 8px;
    border-radius: 4px;
    color: white;
    font-weight: 600;
}
.comparison-card {
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.comparison-card.current {
    background: linear-gradient(135deg, #ffebee 0%, #fce4ec 100%);
    border: 2px solid #ef5350;
}
.comparison-card.greenlens {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    border: 2px solid #4caf50;
}
.impact-item {
    text-align: center;
    padding: 25px;
    background: linear-gradient(135deg, #e3f2fd 0%, #f3f7fd 100%);
    border-radius: 10px;
    margin-bottom: 20px;
}
.code-block {
    background: #1e1e1e;
    color: #d4d4d4;
    padding: 25px;
    border-radius: 8px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    overflow-x: auto;
    line-height: 1.5;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div style="text-align: center; margin-top: 40px;">🌱</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center;">Green Lens</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2rem; color:#5a6c7d;">Real-Time AI Sustainability Toolkit</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:1.2rem; color:#5a6c7d;">Transforming AI Development with Transparent Environmental Insights</p>', unsafe_allow_html=True)

st.markdown("""
### AI is accelerating global innovation—but comes with hidden environmental costs. 
Training and inference of AI models consume <span class="highlight">energy, water, and materials</span>, often without real-time visibility. **Green Lens** addresses this by measuring, analyzing, and reporting AI's environmental impact **per query, per task, and across lifecycle stages**.
""", unsafe_allow_html=True)

st.markdown("## Our Vision")
vision_points = [
    ("📊 Accurate Assessment", "Carbon, water, and material footprint measurement"),
    ("🔄 Comparability", "Across models, infrastructures, and geographies"),
    ("💡 Actionable Insights", "Reduce environmental impact with recommendations"),
    ("🚀 Wide Adoption", "For AI companies, developers, and regulators")
]

cols = st.columns(len(vision_points))
for i, (title, desc) in enumerate(vision_points):
    with cols[i]:
        st.markdown(f"**{title}**")
        st.write(desc)

st.markdown("## Key Innovation: AITP Protocol")
st.markdown("""
**AI Telemetry & Sustainability Protocol**

Green Lens introduces AITP, a new standard for real-time AI sustainability:

- Embedded telemetry in ML frameworks (PyTorch, TensorFlow, JAX)
- Tracks energy, carbon, and water footprints per query, per inference, and per training run
- Allocates environmental impact in shared/multi-tenant systems
- Standardizes functional units for comparability:
    - LLMs: per 1M tokens
    - Vision models: per 1,000 images
    - Recommendation systems: per user/day
- Provides user-facing "carbon & water labels" to raise awareness
""")

st.markdown("## Toolkit Overview")
toolkit_data = {
    "Focus Area": ["Carbon Footprint", "Water Footprint", "Real-Time Monitoring", "Optimization Insights", "Lifecycle Assessment", "Comparative Analysis"],
    "Method": [
        "Live GPU/CPU telemetry → CO₂eq conversion",
        "Energy × WUE × Geo-Aware Index",
        "JSON/CSV logs + live plots",
        "Rule-based recommendations",
        "Training + inference + data + hardware",
        "AI vs AI or AI vs non-AI"
    ],
    "Deliverable": [
        "Per-query emissions logging",
        "Per-query water consumption",
        "Live dashboard",
        "Energy/water reduction tips",
        "Sustainability Scorecard",
        "Side-by-side scorecards"
    ],
    "Novelty": [
        "Real-time, per-query metrics",
        "Reflects water scarcity context",
        "Instant environmental insights",
        "Actionable sustainability improvements",
        "Full lifecycle per-unit impact",
        "Informed trade-off evaluation"
    ]
}
df_toolkit = pd.DataFrame(toolkit_data)
st.dataframe(df_toolkit, use_container_width=True)

st.markdown("## Sample Output")
st.markdown("### Per-Query Footprint")
st.code("""Query: "Translate 1000 sentences from English → French"
Elapsed Time: 0.37 sec
Energy: 0.005 kWh
Carbon: 0.002 kg CO₂eq
Water: 0.009 L
Recommendation: Use distilled model to save ~0.001 kg CO₂eq per 1000 tokens""", language='text')

st.markdown("### Sustainability Scorecard")
scorecard_data = {
    "Phase": ["Training", "Inference", "Total"],
    "Energy (kWh)": [12.5, 3.1, 15.6],
    "Carbon (kg CO₂eq)": [5.2, 1.4, 6.6],
    "Water (L)": [22.5, 4.8, 27.3],
    "Per-Unit": ["0.10 / 1M tokens", "0.02 / 1M tokens", "—"]
}
df_scorecard = pd.DataFrame(scorecard_data)
st.dataframe(df_scorecard, use_container_width=True)

st.markdown("## Current Solutions vs Green Lens")
cols = st.columns(2)
with cols[0]:
    st.markdown('<div class="comparison-card current">', unsafe_allow_html=True)
    st.markdown("### ❌ Current Tools")
    metrics = [
        "Granularity: Aggregated metrics only",
        "Carbon: Estimates, no geo-adjustment",
        "Water: Rarely included",
        "Lifecycle: Partial coverage",
        "User Awareness: None",
        "Comparability: Inconsistent units",
        "Insights: Rare recommendations",
        "Benchmarking: Fragmented"
    ]
    for m in metrics:
        st.markdown(f"- {m}")
    st.markdown('</div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="comparison-card greenlens">', unsafe_allow_html=True)
    st.markdown("### ✅ Green Lens")
    metrics_gl = [
        "Granularity: Real-time, per-query",
        "Carbon: Accurate + location-aware",
        "Water: WUE + scarcity index",
        "Lifecycle: Full coverage",
        "User Awareness: Carbon & water labels",
        "Comparability: Standardized units",
        "Insights: Automated optimization",
        "Benchmarking: Universal suite"
    ]
    for m in metrics_gl:
        st.markdown(f"- {m}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("## Why Green Lens Matters")
impact_items = [
    ("💡", "Innovation", "First real-time per-query AI footprint toolkit"),
    ("🎯", "Accuracy", "Telemetry-driven, not proxy estimates"),
    ("⚡", "Feasibility", "Lightweight Python, cloud-agnostic"),
    ("🌍", "Impact", "Enables sustainable AI decisions"),
    ("📢", "Awareness", "Increases carbon & water literacy")
]
for icon, title, desc in impact_items:
    st.markdown(f'<div class="impact-item"><div style="font-size:2.5rem;">{icon}</div><h4>{title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 40px; border-radius:10px;">
<h2>Ready to Try Green Lens?</h2>
<p style="margin: 20px 0; font-size: 1.1rem;">Experience our prototype and see real-time AI sustainability in action</p>
<a href="#" style="display:inline-block; padding:15px 40px; background: linear-gradient(135deg, #4caf50 0%, #45a049 100%); color:white; text-decoration:none; border-radius:30px; margin:10px;">View Prototype</a>
<a href="#" style="display:inline-block; padding:15px 40px; background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%); color:white; text-decoration:none; border-radius:30px; margin:10px;">Read Documentation</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<footer style="text-align: center; padding: 40px 0; color:#5a6c7d;">
<p>🌱 Green Lens - Making AI Sustainable, One Query at a Time</p>
<p>Built for positive environmental impact</p>
</footer>
""", unsafe_allow_html=True)
```
