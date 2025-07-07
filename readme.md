# 🌱 GHG Emission Predictor

A machine learning-based Streamlit app that estimates **greenhouse gas (GHG) emissions** released in the supply chain for every ₹ or $ spent on a product.

## 💡 How It Works

You enter:
- The type of GHG (CO₂, CH₄, etc.)
- Source (commodity or industry)
- Base emission value
- Data quality scores (location, time, reliability, etc.)

The app:
- Preprocesses the input
- Scales the data
- Predicts GHG emissions using a trained ML model

## 🔧 Built With
- Streamlit
- Scikit-learn
- Pandas
- Joblib

## 📁 File Structure

    app.py
    requirements.txt
    README.md
    SupplyChainGHGData.xlsx
    model_training.ipynb
    models/
    ├── LR_model.pkl
    └── scaler.pkl
    utils/
    └── preprocessor.py

## How It Works

This app predicts **how much greenhouse gas (GHG) is emitted** for every dollar or rupee spent on a product or service in its supply chain.

### What you input:

- **Type of gas:** Like carbon dioxide, methane, or nitrous oxide — different gases have different impacts.
- **Measurement unit:** This tells the app how the emissions are measured, usually kilograms per dollar (or rupee) spent.
- **Source of data:** Whether the emission data is from a specific product (commodity) or an entire industry.
- **Base emission value:** The estimated emissions *without* adding any safety margins or adjustments.
- **Margins:** Additional factors added to the base emission to cover uncertainties.
- **Data Quality Ratings:** How reliable and relevant your data is, based on things like:
  - How recent the data is
  - How specific it is to your region
  - How well it matches your technology
  - And how complete the data is overall

### What happens next?

1. Your inputs get cleaned and converted into numbers the model can understand.
2. These processed inputs are then scaled using a pre-trained scaler (to make sure all numbers are in the right range).
3. The trained prediction model takes these inputs and predicts the **total GHG emissions per unit currency spent**.
4. The app shows you the predicted emission value so you can understand your product’s environmental impact.

---

### Why use this app?

Knowing your supply chain emissions helps businesses and individuals:

- Make smarter choices to reduce carbon footprints
- Understand where emissions come from in their products
- Track progress toward sustainability goals


## 🚀 Live Demo of the Project

Check out the working app here: [GHG Emissions Prediction](https://huggingface.co/spaces/AjinkyaLadkat/GHG_Emissions_Prediction)

## License

This project is licensed under the MIT License - see the [MIT License](LICENSE) file for details.
