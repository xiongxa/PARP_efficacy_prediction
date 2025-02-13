# -*- coding: utf-8 -*-
import pandas as pd
# from catboost import CatBoostClassifier
import tkinter as tk
from PIL import ImageGrab
import pickle

# import model
model = lgb.Booster(model_file='models/primary_prediction_model.txt')

# GUI 窗口
window = tk.Tk()
window.geometry('500x300')
window.title("Efficacy and prognosis prediction of PARP inhibitors")

# 特征输入框
feature_names = ['BRCA/HRD status', 'Tatal Bile Acids', 'Fibrinogen Concentration', 'Antibody-ABO', 'Thrombin Time', 'PARPi']
input_data = []
row = 0
for name in feature_names:
    tk.Label(window, text=name, anchor='center').grid(row=row, column=0, sticky='W', padx=15, pady=1)
    feature_input = tk.Entry(window)
    feature_input.grid(row=row,column=1, padx=15, pady=1)
    row=row+1
    input_data.append(feature_input)

# 预测按钮
def predict():
    features = [float(inp.get()) for inp in input_data]
    prob = model.predict([features])[0][1] * 100
    risk_level = 'Low' if prob < 0.5 else 'High'
    output_label.config(text=F"Patient's risk level: {risk_level}")
predict_button = tk.Button(window, text="Predict", command=predict)
predict_button.grid(column=0, columnspan=2, pady=20)

# 输出标签
output_label = tk.Label(window, text="")
output_label.grid(column=0, columnspan=2)

window.mainloop()