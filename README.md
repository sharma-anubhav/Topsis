# TOPSIS-Anubhav-101803051

## What is TOPSIS
Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method.<br> TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.

## Installation
```pip install TOPSIS-Anubhav-101803051```

## Input csv format
Input file contain three or more columns<br>
First column is the object/variable name <br>
From 2nd to last columns contain numeric values only

## How to use it
Command Prompt<br>
```topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>```<br>
Example:<br>
```topsis inputfile.csv “1,1,1,2” “+,+,-,+” result.csv```<br><br>
<i>Note: The weights and impacts should be ',' seperated, input file should be in pwd.</i> 

## Sample input data
|Model|Corr|Rseq|RMSE|Accuracy|
|-----|----|----|----|--------|
|M1   |0.79|0.62|1.25|60.89   |
|M2   |0.66|0.44|2.89|63.07   |
|M3   |0.56|0.31|1.57|62.87   |
|M4   |0.82|0.67|2.68|70.19   |
|M5   |0.75|0.56|1.3 |80.39   |
## Sample output data
|Model|Corr|Rseq|RMSE |Accuracy|Topsis Score       |Rank|
|-----|----|----|-----|--------|-------------------|----|
|M1   |0.79|0.62|1.25 |60.89   |0.7731301458119156 |2   |
|M2   |0.66|0.44|2.89 |63.07   |0.22667595732024362|5   |
|M3   |0.56|0.31|1.57 |62.87   |0.4389494866695491 |4   |
|M4   |0.82|0.67|2.68 |70.19   |0.5237626971836845 |3   |
|M5   |0.75|0.56|1.3  |80.39   |0.8128626132980138 |1   |

## License
© 2020 Anubhav Sharma

This repository is licensed under the MIT license. See LICENSE for details.