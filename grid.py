def main():
    print("Number of rows:")
    row = int(input())
    print("Number of Columns:")
    columns = int(input())
    print("Out:\n")

    for i in range(row): # iterate 
        print('|_______|'*columns) # print '|___|' columns times

if __name__ == '__main__':
    main()
