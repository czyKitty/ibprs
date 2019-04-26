import sys
import re

# Return num of breakpoints
def breakpoints(series):
    sum = 0
    for i in range(len(series) - 1):
        if series[i] != series[i+1] + 1 and series[i] != series[i+1] - 1:
            sum += 1
    return sum

# Reverse sequence
def reverse(series, start, end):
    n = end - start + 1
    for i in range(n//2):
        series[start+i], series[start+(n-i-1)] = series[start+(n-i-1)], series[start+i]
    return series

# Returns true if given array has a decreasing strip.
def decreasingStrips(series):
    for i in range(1, len(series)-1):
        if series[i-1] + 1 != series[i] and series[i] + 1 != series[i+1]:
            return True
    return False

# Returns reversal that minimizes the number of breakpoints.
def reversal(series):
    max = 0
    maxSeg = (0,0)
    numBreakPoints = breakpoints(series)
    for i in range(1, len(series)-2):
        for j in range(i+1, len(series)-1):
            if abs(series[i]-series[j+1]) == 1 or abs(series[i-1]-series[j]) == 1:
                temp = reverse(series[:], i, j)
                if numBreakPoints - breakpoints(temp) > max:
                    max = numBreakPoints - breakpoints(temp)
                    maxSeg = (i,j)
                    if max == 2:
                        return (i,j)
    return maxSeg

# Returns increasing strip.
def increasingStrip(series):
    i = 1
    while i < len(series)-1 and series[i] + 1 != series[i+1]:
        i += 1
    j = i + 1
    while j < len(series)-2 and series[j] + 1 == series[j+1]:
        j += 1
    return (i, j)

def improvedBreakpointReversalSort(series,outText):
    numBreakPoints = breakpoints(series)
    reversalDistance = 0
    while numBreakPoints > 0:
        if decreasingStrips(series):
            (start, end) = reversal(series)
            reverse(series, start, end)
            reversalDistance += 1
        else:
            (start, end) = increasingStrip(series)
            reverse(series, start, end)
            reversalDistance += 1
        outText.write(" ".join(str(x) for x in series)+"    Breakpoints:"+str(breakpoints(series))+"    Reversal Distance:"+str(reversalDistance)+"\n")
        numBreakPoints = breakpoints(series)
    return [series,reversalDistance]

def main():
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    fileText = open(inputFileName,'r')
    lines = fileText.readline().split()
    
    # Exit if there's only one element
    if len(lines) < 2:
        sys.exit()

    series = [int(i) for i in lines[0:]]

    # Add begin and end
    newSeries = [0] + series + [len(series) + 1]

    # Output
    outText = open(outputFileName,'w')
    outText.write(" ".join(str(x) for x in newSeries)+"    Breakpoints:"+str(breakpoints(newSeries))+"    Reversal Distance:0"+"\n")
    result = improvedBreakpointReversalSort(newSeries,outText)
    result[0] = result[0][1:-1]
    outText.write("Final Result: "+" ".join(str(x) for x in result[0])+"    Reversal Distance:"+str(result[1])+"\n")

main()