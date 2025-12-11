# 1. Kvadratlar ro‘yхati
kvadratlar = [x**2 for x in range(1, 11)]

# 2. Juft sonlar
juftlar = [x for x in range(1, 21) if x % 2 == 0]

# 3. Toq sonlar
toq_sonlar = [x for x in range(10, 31) if x % 2 != 0]

# 4. So‘z uzunliklari
sozlar1 = ["apple", "banana", "pear"]
uzunliklar = [len(s) for s in sozlar1]

# 5. Harflar ro‘yхati
harflar = [h for h in "So'z"]

# 6. Sonlar kubi
kublar = [x**3 for x in range(1, 6)]

# 7. Matritsani tekislash
matritsa = [[1, 2], [3, 4], [5, 6]]
tekis = [y for x in matritsa for y in x]

# 8. Bosh harflar
sozlar2 = ["dog", "cat", "mouse"]
bosh_harflar = [s[0] for s in sozlar2]

# 9. Musbat sonlar
sonlar = [-5, 3, -1, 0, 7, -2]
musbatlar = [x for x in sonlar if x > 0]

# 10. Juft/Toq belgisi
juft_toq = ["juft" if x % 2 == 0 else "toq" for x in range(1, 11)]

# 11. Kvadrat ildizlar
import math
ildizlar = [math.sqrt(x) for x in [4, 9, 16, 25]]

# 12. 5 ga bo‘linadiganlar
bolinadigan_5 = [x for x in range(0, 51) if x % 5 == 0]

# 13. Katta harflar
katta = [s.upper() for s in ["hello", "world", "python"]]

# 14. So‘zlarni teskariga o‘girish
teskari = [s[::-1] for s in ["car", "bike", "bus"]]

# 15. Ikki barobar
ikki_barobar = [x * 2 for x in [1, 2, 3, 4]]

# 16. 70 dan yuqori ballar
yuqori = [b for b in [65, 85, 45, 95, 70] if b > 70]

# 17. Faqat harflardan iborat so‘zlar
faqat_harf = [s for s in ["hello", "123", "world", "456"] if s.isalpha()]

# 18. 3 ga bo‘lganda qoldiq 1 bo‘ladiganlar
qoldiq_1 = [x for x in range(1, 21) if x % 3 == 1]

# 19. Oddiy (prime) sonlar
prime = [x for x in range(2, 51)
         if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]

# 20. Juft bo‘lsa "even", toq bo‘lsa "odd"
even_odd = ["even" if x % 2 == 0 else "odd" for x in [1, 2, 3, 4, 5]]

