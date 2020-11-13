import pandas as pd
import sys
import math
import numpy as np
import time

def topsis():
##########################               INPUT FORMAT CHECKING        ##############################################
    print("Validating Input...")
    n = len(sys.argv)
    if n != 5:
        print("Error: Provide correct input format <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        quit()
    if not sys.argv[1].lower().endswith('.csv') or not sys.argv[4].lower().endswith('.csv'):
        print("Error: input and output file format should be .csv")
        quit()
    if(len(sys.argv[2]) != len(sys.argv[3])):
        print("Error: Number of weights and number of impacts passed dont match")
        quit()
    i=0
    while i<len(sys.argv[3]):
        if sys.argv[3][i] not in ["+","-"]:
            print("Error: The impacts should be either '+'/'-'")
            quit()
        i+=2
    try:
        df = pd.read_csv(sys.argv[1])
    except:
        print("Error: Cannot find the file")
        quit()
    if(df.shape[1] <3):
        print("Error: Number of columns should be >= 3")
        quit()
    if(df.shape[1]-1 != len(sys.argv[2])//2+1 or df.shape[1]-1 != len(sys.argv[3])//2+1):
        print("Error: Number of columns of df and number of weights/impacts passed dont match")
        quit()

    df = pd.read_csv(sys.argv[1])
    l = np.array(df.values.tolist())
    l = l[:,1:]
    for row in l:
        for ele in row:
            try:
                float(ele)
                continue
            except:
                print("Error: Non Numeric Input!!!!")
                quit()

    rows, col = l.shape
##########################               DATA NORMALIZATION        ##############################################
    print("Evaluating data...")
    ssums = []
    for i in range(col):
        ssum=0
        for ele in l[:,i]:
            ssum+=math.pow(float(ele),2)
        ssums.append(ssum)
    for i in range(len(ssums)):
        ssums[i] = math.sqrt(ssums[i])
    for i in range(col):
        for j in range(rows):
            l[j][i]=(float(l[j][i])/ssums[i])*float(sys.argv[2][2*i])
    v_p = []
    v_n = []
    for i in range(col):
        if sys.argv[3][2*i] == "+":
            v_p.append(max(l[:,i]))
            v_n.append(min(l[:,i]))
        elif sys.argv[3][2*i] == "-":
            v_p.append(min(l[:,i]))
            v_n.append(max(l[:,i]))
##########################               SCORE GENERATION        ##############################################
    print("Calculating TOPSIS scores,ranks...")
    score_positive = []
    score_negeitive = []
    combined = []
    for i in range(rows):
        pscore = 0
        nscore = 0
        for j in range(col):
            pscore+=math.pow(float(l[i][j])-float(v_p[j]),2)
            nscore += math.pow(float(l[i][j]) - float(v_n[j]), 2)
        score_positive.append(pscore)
        score_negeitive.append(nscore)
    for i in range(len(score_negeitive)):
        score_negeitive[i] = math.sqrt(score_negeitive[i])
        score_positive[i] = math.sqrt(score_positive[i])
        combined.append(score_negeitive[i]+score_positive[i])

    score = []
    for i in range(len(score_negeitive)):
        score.append(score_negeitive[i]/combined[i])
##########################               RANK GENERATION         ##############################################
    g10 = lambda e: e[1][0]
    g1 = lambda e: e[1]
    ranks, _ = zip(*sorted(enumerate(sorted(enumerate(score), key=g1, reverse=True)), key=g10))
    ranks = list(ranks)
    for i in range(len(ranks)):
        ranks[i] = ranks[i]+1

##########################               RESULT FILE GENERATION         ##############################################
    print("Generating output...")
    res = df.copy(deep=True)
    res["Topsis Score"] = score
    res["Rank"] = ranks
    res.to_csv(sys.argv[4],index = False)
    print("Success!")


if __name__ == '__main__':
    topsis()
#python3 test2.py data.csv "1,1,1,1" "+,+,-,+" output.csv
