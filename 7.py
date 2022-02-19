#1
lis=['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for i in lis:
  print(i)

#2
for i in range(25, 51):
  print(i)

#3
for i in lis:
  print(i, lis.index(i))

#4
bar=[4, 7, 8, 9, 10, 11, 12, 14, 16, 18, 23, 28, 41, 47]
while True:
  i=input('Enter number or q')
  try:
    n=int(i)
    if n in bar:
      print('正解')
    else:
      print('不正解')
  except ValueError:
    if i=="q":
      break
    else:
      print('数字を入力するか、qで終了します')
  
  

#5
l1=[8, 19, 148, 4]
l2=[9, 1, 33, 83]
l_sum=[]
for s in l1:
  for t in l2:
    l_sum.append(s*t)

print(l_sum)
