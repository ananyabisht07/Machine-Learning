from collections import Counter
import bs4
import requests
import matplotlib.pyplot as plt
web=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup=bs4.BeautifulSoup(web.content, 'html.parser')
textcontent=[]

for i in range(0,20):
	para=soup.find_all("p")[i].text
	textcontent.append(para)
with open("webdata.txt",'w') as f:
	for i in textcontent:
		f.write('%s' % i)
f=open("webdata.txt",'r')
data=f.read()
num_words=len(data.split())
print("Number of words:",num_words)


with open("webdata.txt",'r') as f:
	list1=[word for line in f for word in line.split()]
word_count=Counter(list1)
word1=[]
count1=[]
for word, count in word_count.most_common(20): 
	print('%s:%d' %(word,count))
	word1.append(word)
	count1.append(count)
plt.pie(count1,labels=word1,autopct='%1.1f%%') 
plt.show()
