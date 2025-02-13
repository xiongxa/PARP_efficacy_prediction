

# Efficacy and Prognosis Prediction of PARP Inhibitors

This Python application provides a graphical user interface (GUI) to predict the efficacy and prognosis of PARP inhibitors in ovarian cancer patients. It includes two prediction models: one for primary outcomes and another for recurrent outcomes. Both models are based on **LightGBM** and provide a user-friendly way for clinicians to input patient data and receive risk predictions.

## Project Structure

```
- models/
  - primary_prediction_model.txt   # Pre-trained LightGBM model for primary prediction
  - recurrent_prediction_model.txt # Pre-trained LightGBM model for recurrent prediction
- PARP_efficacy_prediction_GUI_primary_patients.py        # GUI for primary prediction model
- PARP_efficacy_prediction_GUI_recurrent_patients.py      # GUI for recurrent prediction model
- README.md                       # Project documentation
```

## Requirements

Before running the application, ensure that the following Python libraries are installed:

- `pandas` – For handling data.
- `lightgbm` – For running the pre-trained LightGBM models.
- `tkinter` – For creating the GUI interface (usually pre-installed with Python).
- `Pillow` – For image-related functionalities (used in GUI).

You can install the required libraries using `pip`:

```bash
pip install pandas lightgbm pillow
```

If `tkinter` is not available on your system, please refer to your system’s installation instructions for `tkinter`.

## Usage

### 1. **Model Files**:

This project contains two pre-trained LightGBM models:

- **`primary_prediction_model.txt`**: LightGBM model for predicting primary outcomes (e.g., initial response to PARP inhibitors).
- **`recurrent_prediction_model.txt`**: LightGBM model for predicting recurrent outcomes (e.g., prognosis after recurrence).

These model files are stored in the `models/` directory. Ensure that these model files are available in the correct folder.

### 2. **Running the Application**:

The project includes two Python scripts for running the GUI, each tied to a different model:

#### Primary Prediction GUI

This script uses the **primary prediction model** and allows clinicians to input the following features:

- **BRCA/HRD status**
- **Total Bile Acids**
- **Fibrinogen Concentration**
- **Antibody-ABO**
- **Thrombin Time**
- **PARPi concentration**

To run this script, execute:

```bash
python prediction_gui_primary.py
```

#### Recurrent Prediction GUI

This script uses the **recurrent prediction model** and allows clinicians to input the following features:

- **FBG (Fibrinogen)**
- **CA-199 (Cancer Antigen 199)**
- **Ki67**
- **Glycated Hemoglobin**
- **IOAA (Insulin-like Growth Factor-1)**

To run this script, execute:

```bash
python prediction_gui_recurrent.py
```

Both scripts will open a GUI where users can input the relevant features, click **Predict**, and receive the risk level (Low or High) based on the model’s prediction.

### 3. **How the Prediction Works**:

- The clinician inputs the required features into the GUI.
- The model processes the input and predicts the probability of a **High** or **Low** risk level based on the given features.
- If the probability is greater than 50%, the result will be **High risk**; otherwise, it will be classified as **Low risk**.
- The result is displayed in the GUI, helping clinicians make informed decisions regarding patient care.

## Example Output

After entering the required features and clicking **Predict**, the GUI will display one of the following messages based on the model’s prediction:

- **Patient's risk level: Low**
- **Patient's risk level: High**

<img width="933" alt="image" src="https://github.com/user-attachments/assets/1801589b-0cd8-4571-9b75-7fd28147a6fd" />


## Model Loading

Both GUI scripts load the models as follows:

```python
model = lgb.Booster(model_file='models/primary_prediction_model.txt')  # For primary prediction
# or
model = lgb.Booster(model_file='models/recurrent_prediction_model.txt')  # For recurrent prediction
```

The models are loaded directly from the `models/` folder where they are stored.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
