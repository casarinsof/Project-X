# EXPERIMETS(Ify):
# Project-X
Anomaly Detection in collaboration

Roi size = 96 for all experiments

$ = not launched yet


| Exp n.         | *Exp Name*       | GSM or GSF | Layer | GSM in bottleneck | GSM in dec | ```avg_val accuracy``` | loss | loss in che layers    | Acc per Folder |
|:---------------|:-----------------|:-----------|:------|:------------------|:-----------|:-----------------------|:-----|:----------------------|:---------------|
| 82313  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```  ```               | NO   |                       |                | 
| 82436  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```  ```               | SI   | 0 e 1, 0.5_0.2_0.1    |                |
| 83319  lr1e-4  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```   ```              | SI   | 0 e 1, 1.0, 0.4, 1.0  |                | 
| 82476  lr1e-4  | GSM_01           | GSM        | 0 1   | NO                | YES        | ```   ```              | YES  | 0 e 1, 1.0, 0.4, 1.0  |                |
| $82490  lr1e-4 | GSM_01           | GSM        | 0 1   | NO                | NO         | ```   ```              | NO   |                       |                |
| $82495 lr1e-3  | GSM_01           | GSM        | 0 1   | NO                | NO         | ```   ```              | NO   |                       |                |
| $82498 lr1e-3  | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```   ```              | NO   |                       |                | 
| $82499  lr1e-3 | GSF_012_Bot_Dec  | GSF        | 0 1 2 | YES               | YES        | ```   ```              | YES  | 0 e 1, 0.7, 0.05, 0.2 |                |
| $82544  lr1e-3 | GSM_01           | GSM        | 0 1   | NO                | NO         | ```   ```              | YES  | 0 e 1, 0.7, 0.3       |                |
