#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def initialise(a,b):
    scoring,backtrack = [],[]
    for x in range(a+1):
        scoring.append([-2*x])
        backtrack.append(['L'])
        for y in range(b):
            scoring[-1].append(None)
            backtrack[-1].append(None)
    for y in range(1,b+1):
        scoring[0][y] = -2 * y
        backtrack[0][y] = 'U'
    scoring[0][0],backtrack[0][0] = 0,'END'
    return scoring,backtrack

def c(i,j):
    scores = {'A':4,'C':3,'G':2,'T':1}
    if i == j:
        return scores[i]
    return -3

def s(a,b):
    scoring,backtrack = initialise(len(a),len(b))
    for i in range(1,len(scoring)):
        for j in range(1,len(scoring[i])):
            D = c(a[i-1],b[j-1]) + scoring[i-1][j-1]
            U = scoring[i][j-1] -2
            L = scoring[i-1][j] -2
            maxi = max(D,U,L)
            if D == maxi:
                backtrack[i][j] = 'D'
            elif U == maxi:
                backtrack[i][j] = 'U'
            else:
                backtrack[i][j] = 'L'
            scoring[i][j] = maxi
    outA,outB,i,j = '','',-1,-1
    while backtrack[i][j] != 'END':
        if backtrack[i][j] == 'D':
            outA = a[i] + outA
            outB = b[j] + outB
            i -= 1
            j -= 1
        elif backtrack[i][j] == 'U':
            outA = '-' + outA
            outB = b[j] + outB
            j -= 1
        else:
            outA = a[i] + outA
            outB = '-' + outB
            i -= 1
    return scoring[-1][-1],[outA,outB]

# ------------------------------------------------------------

# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

best_score,best_alignment = s(seq1,seq2)

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

