#1
mus=["Mai Kuraki", "Smile.dk", "CASCADA"]

print(mus)

#2
loc=[(34.0, -118.5), (35.7, 140.0), (1.6, 110.4)]

print(loc)

#3
dic={"Name": "Leo",
     "Prefecture": "Chiba",
     "Sports": "Futsal"}

print(dic)

#4
key=input('キーを入力')
if key in dic:
  print(dic[key])
  
else:
  print('情報なし')

#5
songs={"Mai Kuraki":["always", "Reach for the sky"],
       "SMiLE.dk":"Dragonfly",
       "CASCADA":["A Neverendig Dream", "Everytime We Touch"]}

print(songs)
