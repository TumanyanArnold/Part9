def all_variants(text): # text = abc
    for i in range(1, len(text) + 1): # длина подпоследовательности
        for j in range(len(text) - i + 1):
            yield text[j: j + i] # Возвращаем подстроку, начинающуюся на j и с длиной i


a = all_variants("abc")
for i in a:
    print(i)