# Tabular regressor task

***This folder contains regressor model, training and prediction pipeline.***

We used AutoGluon as it is easy to setup and it achieves good performance due to Ensembling of different models.

In order to use our solutions follow guide provided below.

## Guide:

General folder structure is as follows:
- AutoGluonModels/ 
- data/
   - prediction_results/
- notebooks/
- logger.py
- train.py
- predict.py
- README.md 

Before you move on to next stages make sure to setup venv and install current requirements.txt.

###  How to train model?

Use Kaggle training notebook
(we strongly encourage you to do so in case of target being result replication)
or run `train.py` using CLI call:

In our case we call: 

```
python train.py 
--train_data data/train.csv 
--time_limit 360
```

General parameters of above call:

```
!python train.py 
--train_data path/to/train_data.csv 
--time_limit maximum_time_of_training_in_seconds_or_None
--target_column name_of_your_target_column
```

###  How to run `predict.py`?

Generalized CLI call looks like this:

```
python predict.py 
--test_data /path/to/test_data.csv 
--model_path /path/to/autogluon_model_folder 
--output_path /path/to/save_predictions.csv
```

In our case we call: 

```
python predict.py 
--model_path AutogluonModels/kaggle_model_timelimitnone 
--test_data data/hidden_test.csv 
--output_path data/prediction_results/hidden_test.csv
```
