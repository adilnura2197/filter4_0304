#1
sozlar = ["python", "code", "java", "script", "html", "database"]

natija = list(filter(lambda el: len(el) > 4 and 'e' not in el, sozlar))
print(natija)


#2
roy = [5, 12, 7, 24, 9, 16, 3, 18, 11]

natija = list(filter(lambda x: x % 2 == 0 and x > 10, roy))
print(natija)


#3
saytlar = ["site.com", "test.org", "blog.uz", "info.org", "web.net"]

natija = list(filter(lambda el: el.endswith(".org"), saytlar))
print(natija)


#4
sonlar = [12, 8, 24, 15, 36, 9, 48, 20, 72]

natija = list(filter(lambda el: el % 4 == 0 and el % 6 == 0, sonlar))
print(natija)


#5
sonlar = [25, 13, 45, 102, 305, 77, 85, 100, 95]

natija = list(filter(lambda el: el % 10 == 5, sonlar))
print(natija)


#6
sozlar = ["salom", "dunyo", "kitob", "oquvchi", "uy", "maktab"]

natija = list(filter(lambda el: len(el) % 2 == 1, sozlar))
print(natija)
