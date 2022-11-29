# Project-X
Anomaly Detection in collaboration

Roi size = 96 for all experiments

$ = not launched yet


| #Baseline   | GSM or GSF | avg_val accuracy | Acc per folder                           |Test accu | nParams |
|:----------- |:-----------|:-----------------|:---------------------------------------- |:---------|:--------|
| 3D          |   NO       |    74.4 %        | 80.9 %, 75.1 %, 76.1 %, 65.30 %, 74.40 % |          |   16 M  |  

| Exp n. | *Exp Name*     | GSM or GSF | Layer  | GSM in bottleneck | GSM in dec| avg_val accuracy | Test accu | nParams | Acc per Folder                  | Background |
|:-------|:---------------|:-----------|:-------|:------------------|:----------|:-----------------|:----------|:--------|:--------------------------------|:-----------|
| #1     | GSM_01         |   GSM      |0 1     | NO                | NO        |  73.89 %         |           |   10 M  |79.28, 72.92 ,74.51 ,65.67 ,77.05| YES        |
| 1 bis  | GSM_01viewsInCh|   GSM      |0 1     | NO                | NO        |   74.83 %        |           |   10 M  |            non li ho riportati  | YES        |
| 1 tris | GSM_01viewsInCh|   GSM      |0 1     | NO                | NO        |                  |           |   10 M  |     non li ho riportati         |    NO      |
| 2 $    | GSM_012        |   GSM      |0 1 2   | NO                | NO        |                  |           |  10 M   |                                 |            |
| 3 ...  | GSM_012_Bot    |   GSM      |0 1 2   | YES               | NO        |                  |           |  10 M   |                                 |  NO        |
| 4 ..   | GSM_12_BotDec  |   GSM      |1 2     | YES               | YES       |                  |           |   10 M  |                                 |  NO        | 
| #5     | GSM_012_Dec    |   GSM      |0 1 2   | NO                | YES       |   74.51 %        |           |   10 M  |80.00, 75.19, 75.25, 65.86, 76.26|  YES       |
| #6     | GSF_012_Dec    |   GSF      |0 1 2   | NO                | YES       |      75.80 %     |           |   11 M  |80.21, 77.44, 76.53, 66.78, 78.02| no sicura  |
| 7 ..   | GSM_12_Bot     |   GSM      |1 2     | YES               | NO        |       ...        |           |  10 M   |                                 | NO         |
| 8 ..   | GSF_12_Bot     |   GSF      |1 2     | YES               | NO        |       ...        |           |   11 M  |                                 | NO         |
| #9     | GSF_012_Bot_Dec|   GSF      |0 1 2   | YES               | YES       |   77.24 %        |           |  11 M   |83.08, 78.63, 77.61, 67.48, 79.39| YES        |
|9bis... | GSF_012_Bot_Dec|   GSF      |0 1 2   | YES               | YES       |                  |           |  11 M   |                                 | NO         |
| # 10   | GSF_12_Dec     |   GSF      |1 2     | NO                | YES       |    74.81 %       |           |  11 M   |81.59, 75.20, 74.95, 65.09, 77.20| NO         |
| 11 $   | GSF_12_BotDec  |   GSF      |1 2     | YES               | YES       |                  |           |  10 M   |                                 |  YES       |
