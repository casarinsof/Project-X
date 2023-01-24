# EXPERIMETS sto scrivendo anche quelli che ho lanciato io qua (non cancellare pls):
# Project-X
Anomaly Detection in collaboration

Roi size = 96 for all experiments

$ = not launched yet


| Exp n.         | *Exp Name*       | GSM or GSF | Layer | GSM in bottleneck | GSM in dec | ```avg_val accuracy``` | loss | loss in che layers    | Acc per Folder |
|:---------------|:-----------------|:-----------|:------|:------------------|:-----------|:-----------------------|:-----|:----------------------|:---------------|
| 82313  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```81.16 %```          | NO   |                       |83.66, 84.10, 78.18, 76.78, 83.09 | 
| 82436  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```80.18 %```          | SI   | 0 e 1, 0.5_0.2_0.1    |83.38, 82.00,  77.81, 74.98, 82.73|
| 83319  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```80.77 %```          | SI   | 0 e 1, 1.0, 0.4, 1.0  |83.12, 83.25, 77.83, 76.58, 83.07 | 
| 82476  lr1e-4  | GSM_01           | GSM        | 0 1   | NO                | YES        | ```80.38 %```          | YES  | 0 e 1, 1.0, 0.4, 1.0  |84.01, 81.72, 78.12, 75.55, 82.50 |
| $82490  lr1e-4 | GSM_01           | GSM        | 0 1   | NO                | NO         | ```80.72 %```          | NO   |                       |84.04, 82.21, 77.15, 76.82, 83.38 |
| $82495 lr1e-3  | GSM_01           | GSM        | 0 1   | NO                | NO         | ```   ```              | NO   |                       |83.84, 83.21, 77.78, 77.27,       |
| $82498 lr1e-3  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```   ```              | NO   |                       |81.03, 82.05, 77.14, 75.29        | 
| $82499  lr1e-3 | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```   ```              | YES  | 0 e 1, 0.7, 0.05, 0.2 |                |
| $82544  lr1e-3 | GSM_01           | GSM        | 0 1   | NO                | NO         | ```   ```              | YES  | 0 e 1, 0.7, 0.3       |  errore              |
