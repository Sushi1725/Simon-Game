# lines = open('high_scores.txt', 'r').readlines()
# output = open("fasd.txt", 'w')


# # for line in sorted(lines, key=lambda line: line.split()[0], reverse=True):
# #     print(lines)
# #     placeholder = line.split()[0]
# #     print(placeholder)
# #     print(int(placeholder[0]))
# #     print(line.split())
# #     print(line)
# #     for sortScore in sorted(placeholder, key=lambda sortScore: int(sortScore[0]), reverse=True):
# #         # output.write(sortScore)
# #         print(sortScore)
# # e = []
# # for line in lines:
# #     linn = line.split(',')
# #     print(linn)
# #     lin = int(linn[0])
# #     print(lin)
# #     e.append(lin)
# #     print(e)
    
# # for l in sorted(e, reverse=True):
# #     print(l)

# # a = int(input())
# # if (a % 2) != 0:
# #     print('odd')
# # e = []
# # for line in lines:
# #     e.append(int(line.split(',')[0]) + line.split(',')[1])
# #     print(e)
    
# # for l in sorted(e, reverse=True):
# #     print(l)



# # num = []
# # e = []
# # for line in lines:
# #     e.append(line.split(',')[0])
# #     e.append(line.split(',')[1])
# #     print(e)
    
# # for index, l in enumerate(e):
# #     try:
# #         if(int(index) % 2) == 0:
# #             # print('the index is odd (which is a number)')
# #             num.append(int(l))
# #             print(num)
# #     except ValueError:
# #         pass
# # for new in sorted(num, reverse=True):
# #     print(new)



# num = []
# e = []
# ori = []
# currentIndex = 0
# for line in lines:
#     # print(line)
#     e.append(line.split(',')[0])
#     e.append(line.split(',')[1])
# # print(e)
    
# for index, l, in enumerate(e):
#     # print(index, l)
#     try:
#         if(int(index) % 2) == 0:
#             num.append(int(l))
#             # num.append(index)
#             # print(num)
#             try:
#                 test = e[index+1]
#                 # print(test)
#                 ori.append(l)
#                 ori.append(test)
#                 # print(ori)
#             except IndexError:
#                 pass
#     except ValueError:
#         pass
#     new = sorted(num, reverse=True)
#     print(new)
#     currentIndex = index
    

# output.close()
# # lines.close()


# # importing pandas package
# import pandas

# # assign dataset
# csvData = pandas.read_csv("fasd.csv")

# # displaying unsorted data frame
# print("\nBefore sorting:")
# print(csvData)

# # sort data frame
# csvData.sort_values(csvData.columns[0], axis=0, ascending=[False], inplace=True)

# # displaying sorted data frame
# print("\nAfter sorting:")
# print(csvData)


# import sys
# import csv

# reader = csv.reader(open("fasd.csv"), delimiter=",")

# for Score, Name in reader:
#     sortedList = sorted(reader, key=lambda row: int(row[0]), reverse=True)
#     print(sortedList)
    
    
import sys
import csv

scoreFile = open("fasd.csv")
fileReader = csv.reader(scoreFile, delimiter=",")
score = 9
initial = ['A', 'B', 'C']

try:
    # for Score, Name in fileReader:
    #     sortedFile = sorted(fileReader, key=lambda row: int(row[0]), reverse=True)
    #     print(sortedFile)
    # scoreFile.close()

    scoreFile2 = open("fasd.csv", "w", newline='')
    fileWriter = csv.writer(scoreFile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(['Score', 'Name'])
    fileWriter.writerow([score, initial[0] + initial[1] + initial[2]])

    # for i, j in enumerate(sortedFile):
    #     fileWriter.writerow(sortedFile[i])
except IndexError:
    pass