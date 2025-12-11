# 1. Kvadratlar ro'yxati: 1 dan 10 gacha sonlarning kvadratlari
kvadratlar = [x**2 for x in range(1, 11)]

# 2. Juft sonlarni tanlash: 1 dan 20 gacha sonlardan faqat juftlari
juftlar = [x for x in range(1, 21) if x % 2 == 0]

# 3. Toq sonlar ro'yxati: 10 dan 30 gacha bo'lgan toq sonlar
toq_sonlar = [x for x in range(10, 31) if x % 2 != 0]

# 4. So'z uzunliklari: ["apple", "banana", "pear"] so'zlarining uzunliklari
sozlar = ["apple", "banana", "pear"]
uzunliklar = [len(s) for s in sozlar]

# 5. Harflar ro'yxati: "So'z" so'zidagi har bir harfni olib ro'yxat qilish
harflar = [h for h in "So'z"]

# 6. Sonlar kubi: 1 dan 5 gacha bo'lgan sonlarning kublari
kublar = [x**3 for x in range(1, 6)]

# 7. Matritsani tekislash: [[1, 2], [3, 4], [5, 6]] ni tekis ro'yxatga aylantirish
matritsa = [[1, 2], [3, 4], [5, 6]]
tekis = [y for x in matritsa for y in x]

# 8. So'z bosh harflari: ["dog", "cat", "mouse"] so'zlarining bosh harflari
sozlar2 = ["dog", "cat", "mouse"]
bosh_harflar = [s[0] for s in sozlar2]

# 9. Musbat sonlarni tanlash: [-5, 3, -1, 0, 7, -2] ro'yxatidan musbatlari
sonlar = [-5, 3, -1, 0, 7, -2]
musbatlar = [x for x in sonlar if x > 0]

# 10. Juft/Toq belgisi: 1 dan 10 gacha sonlar uchun "juft"/"toq" belgisi
juft_toq = ["juft" if x % 2 == 0 else "toq" for x in range(1, 11)]
