import csv

def readInData():
    with open('aaplStockPrice.csv','rb') as f:
        reader = csv.reader(f)
        adjClosePrice = [ float( line[6] ) for i,line in enumerate(reader) if i != 0 ]
    return adjClosePrice

def std( adjClosePrice ):
    n =  len(adjClosePrice) * 1.0
    mean = sum(adjClosePrice) / n
    std = ( sum( [ (price - mean)**2 for price in adjClosePrice ] ) / n ) **0.5
    return std

def main():
    '''
    testing function
    :return:
    '''
    adjClosePrice = readInData()
    print std(adjClosePrice)

if __name__ == '__main__':main()