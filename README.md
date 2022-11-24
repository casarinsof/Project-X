# Project-X
Anomaly Detection in collaboration

Roi size = 96 for all experiments

$ = not launched yet


| #Baseline   | GSM or GSF | avg_val accuracy | Acc per folder                           |Test accu | nParams |
|:----------- |:-----------|:-----------------|:---------------------------------------- |:---------|:--------|
| 3D          |   NO       |    74.4 %        | 80.9 %, 75.1 %, 76.1 %, 65.30 %, 74.40 % |          |   10 M  |  

| Exp n. | *Exp Name*     | GSM or GSF | Layer  | GSM in bottleneck | GSM in dec| avg_val accuracy | Test accu | nParams | Acc per Folder                  | Background |
|:-------|:---------------|:-----------|:-------|:------------------|:----------|:-----------------|:----------|:--------|:--------------------------------|:-----------|
| 1      | GSM_01         |   GSM      |0 1     | NO                | NO        |                  |           |         |                                 | YES        |
| 2 $    | GSM_012        |   GSM      |0 1 2   | NO                | NO        |                  |           |         |                                 |            |
| 3 $    | GSM_012_Bot    |   GSM      |0 1 2   | YES               | NO        |                  |           |         |                                 |            |
| 4 $    | GSM_12_BotDec  |   GSM      |1 2     | YES               | YES       |                  |           |         |                                 |            | 
| 5      | GSM_012_Dec    |   GSM      |0 1 2   | NO                | YES       |                  |           |         |                                 |  YES       |
| 6      | GSF_012_Dec    |   GSF      |0 1 2   | NO                | YES       |      75.80 %     |           |         |80.21, 77.44, 76.53, 66.78, 78.02| No L yes A |
| 7      | GSM_12_Bot     |   GSM      |1 2     | YES               | NO        |                  |           |         |                                 | No L yes A |
| 8      | GSF_12_Bot     |   GSF      |1 2     | YES               | NO        |                  |           |         |                                 | No L yes A |
| 9      | GSF_012_Bot_Dec|   GSF      |0 1 2   | YES               | YES       |                  |           |         |                                 | YES        |
| 10     | GSF_12_Dec     |   GSF      |1 2     | NO                | YES       |                  |           |         |                                 | NO         |
