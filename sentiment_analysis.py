import textblob as tb
import csv
delimiters=["[","'","]","(",")"]
pos=0
neg=0
neu=0
with open('feedback.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        data=row
        string_data=str(data)
        for i in delimiters:
            string_data=string_data.replace(i,'')
        input_to_textblob = tb.TextBlob(string_data)
        sentence_polarity = input_to_textblob.sentiment.polarity
        if (sentence_polarity > 0):
            print("Positive Sentence")
            pos+=1
        elif (sentence_polarity == 0):
            print("Neutral Statement")
            neu += 1
        elif (sentence_polarity < 0):
            print("Negative Sentence")
            neg += 1

print("Total Positive",pos)
print("Total Negative",neg)
print("Total Neutral",neu)