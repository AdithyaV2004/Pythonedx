# To convert to random format to standard ISO format

months=[              #List of months for convertion to index
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            d=input("Date: ").strip()      ##Strip any leading any trailing spaces in input
            predict(d)
            return
        except:
            None

def predict(date):                        #To convert to ISO 8601
    if date[1]=="/" or date[2]=="/":             #if date is in form mm/dd/yyyy
        li=date.split("/")
        if int(li[0])>12 or int(li[1])>31 or not(len(li[2])==4):      #irregular dates
            raise Exception
        print(f"{li[2]}-{int(li[0]):02}-{int(li[1]):02}")
    else:                                                   #date in form month day, year
        li=date.split(" ")
        m=month(li[0].title())             #Function to convert month word to month number
        d=day(li[1])                     #function to extract only day number
        if m>12 or int(d)>31 or not(len(li[2])==4):         #Irregular date
            raise Exception
        print(f"{li[2]}-{m:02}-{int(d):02}")

def month(s):
    return (months.index(s)+1)

def day(s):
    i=s.index(",")     #To find idex where day entry ends
    return s[0:i]

main()
