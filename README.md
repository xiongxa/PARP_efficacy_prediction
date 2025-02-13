
# Efficacy and Prognosis Prediction of PARP Inhibitors

This Python application provides a simple graphical user interface (GUI) for predicting the efficacy and prognosis of PARP inhibitors in ovarian cancer patients. The model takes input features from the clinician and outputs the patient's risk level (Low or High).

## Requirements

Before running the application, ensure that the following Python packages are installed:

- `pandas`
- `tkinter`
- `Pillow`
- `scikit-learn`

You can install them using `pip`:

```bash
pip install pandas pillow scikit-learn
```

`tkinter` is usually pre-installed with Python, but if you are on a system where it's not available, refer to your system’s instructions for installing `tkinter`.

## Usage

1. **Model File**: The application requires a trained model file `recurrent_prediction_model.pkl` to make predictions. This model should be a pre-trained classifier (e.g., logistic regression, random forest, etc.) that has been saved using `pickle`. The model should be saved in the `models/` directory within the same directory as this script.

2. **Running the Application**:
   - Place your trained model (`recurrent_prediction_model.pkl`) in the `models/` directory.
   - Run the Python script (`prediction_gui.py`) directly:
   
   ```bash
   python prediction_gui.py
   ```
   
3. **Input Features**: The GUI will prompt the user to enter six features for a patient:
   - **BRCA/HRD status**
   - **Total Bile Acids**
   - **Fibrinogen Concentration**
   - **Antibody-ABO**
   - **Thrombin Time**
   - **PARPi concentration**

4. **Predicting Risk Level**: After entering the features, click the **Predict** button. The application will display the patient's risk level (Low or High) based on the prediction made by the model.

## Code Breakdown

- **Model Loading**: The trained model is loaded using `pickle.load()`. The model is expected to have a `predict_proba` method that returns the probabilities for the two possible outcomes (Low or High risk).
  
- **GUI**: The GUI is built using `Tkinter`. It consists of:
  - Six input fields where the user enters the feature values.
  - A **Predict** button that triggers the prediction function.
  - A label to display the patient's predicted risk level.

- **Prediction Logic**: The features inputted by the user are passed to the model, which returns a probability score. If the probability is greater than 50%, the risk level is classified as `High`. Otherwise, it is classified as `Low`.

## Example Output

After entering the required features, the GUI will display one of the following messages:

- **Patient's risk level: Low**
- **Patient's risk level: High**

## Notes

- This tool is intended to assist clinicians in quickly evaluating the risk level of patients based on the provided features.
- The performance of the model depends on the quality of the trained model file (`recurrent_prediction_model.pkl`).
  
## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This `README` will guide users on how to set up and use the application, while also providing some context on the model’s functionality and requirements.
