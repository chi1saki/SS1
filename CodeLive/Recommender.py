#main function
def main():
    print("Welcome to the CSC110 Book Recommender. Type the word in the left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages  : output the average ratings of all books in the system")
    print("quit      : exit the program")
    print("next task?")
    x = str(input())
    if (x =="recommend"):
        recommend()
    elif (x=="averages"):
        averages()
    elif (x=="quit"):
        quit()
main()
#read file
def readfile():
    ratings = open("ratings.txt")
    data = []
    user = []
    f=ratings.readlines()
    ratings.seek(0)
    for i, line in enumerate(ratings):
        if i%3 ==1:
            data.append((line.rstrip()))
        if i %3 ==0:
            user.append((line.strip()))
    data = list(list(dict.fromkeys(data)))
    user = list(list(dict.fromkeys(user)))
    ratings.seek(0)
    ratingsdata = {}
    averages = {}
    for a in data:
        averages[a] = [0,0]
    for b in user:
        ratingsdata[b]=[0 for i in range (len(data))]
    for i,line in enumerate(ratings):
        for d in range(len(data)):
            if(data[a]==line.strip()):
                ratingsdata[f[i-1].rstrip()][a] = int (f[i+1].rstrip())
                averages[data[a]][0] += int(f[i + 1].rstrip())
                averages[data[a]][1] += 1
    for k in averages:
        averages[k]= averages[k][0]/averages[k][1]
    return data, user, ratingsdata, list(averages.item())

#function averages
def averages():
    averages = readfile()[3]
    averages.sort(key = lambda x:x[1], reverse = True)
    print ("recommendation: ")
    for i in averages:
        print(i[0]+" "+ str(i[1]) )

averages()
#function recommend
def recommend():
    users = str(input("user?")).capitalize()
    user = readfile()[1]
    ratingsdata = readfile()[2]
    data = readfile()[0]
    similar=[]
recommend()
#function quit
def quit():
    print(" ")
quit()