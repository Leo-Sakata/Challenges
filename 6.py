#1
c='カミュ'
for i in range(0, len(c)):
  print(c[i])

#2
obj=input('何を：')
dist=input('誰に：')
sentence='私は昨日{}を書いて、{}に送った!'.format(obj, dist)
print(sentence)

#6
print("aldous Huxley was born in 1894".capitalize())

#4
lst="どこで？　だれが？　いつ？".split("　")
print(lst)

#5
words=["the", "fox", "jumped", "over", "the", "fence", "."]
one=" ".join(words[0:6]) + words[6]
print(one)

#6
print("A screaming comes across the sky.".replace("s", "$")

#7

#8
print("Shohei \"Shotime\", all the time")
      
#9
print("three "+"three "+"three")
print("three"*3)

#10
s="四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(s[:s.index('、')])
