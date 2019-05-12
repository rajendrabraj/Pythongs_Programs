#Take the File name as input

#a=str(input("Enter the name of the file with .txt extension:"))

a = "D:\Rajendra_2019\Python_docs\Country_data.txt"

#my_header ="Date	   Open	    High	Low	  Close*	Adj. close**	 Volume"

print("Stock market data for DHFL : File name is : " ,a )

#Read the contents of the File
file2=open(a,'r')

line=file2.readline()

print("Reading the contents of the file")
while(line!=""):
    #print(my_header)
    print(line)
    line=file2.readline()
file2.close()
print("File completed read till the end ")
