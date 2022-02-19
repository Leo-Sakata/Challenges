#1
st = open("yf.txt", 'r', encoding='utf-8')
print(st.read())

#2
ans=input('来年のFリーグ王者は？')

with open('answer.txt', 'w') as f:
  f.write(ans)
  f.close()

#3
import csv

l=[
  ['Top Gun', 'Risky Business', 'Minority Report'],
  ['Titanic', 'The Revenant', 'Inception'],
  ['Training Day', 'Man on Fire', 'Flight']
  ]

with open('9-3.csv', 'w', newline="") as f:
  w = csv.writer(f, delimiter=',')
  w.writerow(l[0])
  w.writerow(l[1])
  w.writerow(l[2])
