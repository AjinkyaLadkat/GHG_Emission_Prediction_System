import streamlit as st
import joblib
import numpy as np
import pandas as pd
from utils.preprocessor import preprocess_input

# Load model and scaler
model = joblib.load('models/LR_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# App title and intro
st.title("🌱 Supply Chain Emissions Predictor")

st.markdown("""
This app estimates how much **greenhouse gas (GHG)** is released for every **₹ or $** spent on a product, based on:
- Type of gas
- Source of emission
- Data quality (location accuracy, time relevance, etc.)

It's designed to help **businesses and individuals** understand their carbon footprint better.
""")

# Input form
with st.form("prediction_form"):

    st.subheader("📥 Enter Product/Emission Details")

    # Substance type
    st.markdown("**1. What kind of greenhouse gas is this data about?**")
    substance = st.selectbox("Choose substance type:",
        ['Select an option', 'Carbon Dioxide (CO₂)', 'Methane (CH₄)', 'Nitrous Oxide (N₂O)', 'Other GHGs'],
        index=0,
        key="substance_key"
    )

    # Unit type
    st.markdown("**2. What unit is used for the emission measurement?**")
    st.caption("This shows how emissions relate to money spent, like kg of gas per dollar or rupee.")
    unit = st.selectbox("Choose unit format:",
        ['Select an option', 'kg/2018 USD, purchaser price', 'kg CO₂e/2018 USD, purchaser price'],
        index=0,
        key="unit_key"
    )

    # Source type
    st.markdown("**3. Where is this emission data coming from?**")
    st.caption("Is the data based on the industry as a whole or a specific product?")
    source = st.selectbox("Choose source type:",
        ['Select an option', 'Commodity', 'Industry'],
        index=0,
        key="source_key"
    )

    # Base emission value
    st.markdown("**4. Base Emission Value (without margin)**")
    st.caption("The estimated GHG emitted per dollar or rupee spent, excluding overheads.")
    supply_wo_margin = st.number_input("Base GHG Emission (kg/unit currency)", min_value=0.0, key="supply_key")

    # MARGIN input 
    st.markdown("**5. Margins of Supply Chain Emission Factors**")
    st.caption("Additional margin factor added to base emissions.")
    margin = st.number_input("Margins of Supply Chain Emission Factors", min_value=0.0, key="margin_key")

    st.subheader("📊 Data Quality (DQ) Ratings")
    st.caption("Rate the quality of your data on a scale from 0 (very poor) to 1 (very high).")

    dq_reliability = st.slider("🔍 How reliable is the data source?", 0.0, 1.0, key="dq_reliability_key")
    dq_temporal = st.slider("⏳ How recent is the data?", 0.0, 1.0, key="dq_temporal_key")
    dq_geo = st.slider("🗺️ How specific is the data to your region?", 0.0, 1.0, key="dq_geo_key")
    dq_tech = st.slider("⚙️ Does the data match your technology?", 0.0, 1.0, key="dq_tech_key")
    dq_data = st.slider("📈 How complete is the data?", 0.0, 1.0, key="dq_data_key")

    submit = st.form_submit_button("📤 Predict Emissions")

# Handle submission
if submit:
    if 'Select an option' in [substance, unit, source]:
        st.warning("Please select valid options for Substance, Unit, and Source.")
    else:
        input_data = {
            'Substance': substance.lower().replace(" (", "_").replace(")", "").replace(" ", "_"),
            'Unit': unit,
            'Supply Chain Emission Factors without Margins': supply_wo_margin,
            'Margins of Supply Chain Emission Factors': margin,  # <-- added back here
            'DQ ReliabilityScore of Factors without Margins': dq_reliability,
            'DQ TemporalCorrelation of Factors without Margins': dq_temporal,
            'DQ GeographicalCorrelation of Factors without Margins': dq_geo,
            'DQ TechnologicalCorrelation of Factors without Margins': dq_tech,
            'DQ DataCollection of Factors without Margins': dq_data,
            'Source': source,
        }

        input_df = preprocess_input(pd.DataFrame([input_data]))

        # Debug prints (uncomment if needed)
        # st.write("Input columns to scaler:", input_df.columns.tolist())
        # st.write("Scaler expects:", scaler.feature_names_in_)

        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)

        st.success(
            f"🌍 Your product releases **{prediction[0]:.4f} kg of CO₂ equivalent** for every **$1 spent** in the supply chain."
        )
