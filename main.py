# Python Veri Tipleri

# Sayılar (Numbers): Python'da kullanılan sayılar iki türde olabilir: tamsayılar (integer) ve ondalık sayılar (float). Tamsayılar, negatif ve pozitif olabilen tam sayıları ifade ederken, ondalık sayılar, noktalı sayıları ifade eder.

# Dizeler (Strings): Dizeler, karakterlerden oluşan metinlerdir. Python'da tek tırnak veya çift tırnak içine alınarak oluşturulurlar.

# Booleanlar: Booleanlar yalnızca iki değere sahip bir veri tipidir: True (doğru) ve False (yanlış). Booleanlar sıklıkla koşullu ifadelerde ve kontrol yapılarında kullanılır.

# Listeler (Lists): Listeler, değiştirilebilir öğelerin bir koleksiyonudur. Python'da köşeli parantez içinde virgülle ayrılmış öğeler olarak tanımlanırlar.

# Demetler (Tuples): Demetler, değiştirilemez öğelerin bir koleksiyonudur. Python'da normal parantezler içinde virgülle ayrılmış öğeler olarak tanımlanırlar.

# Sözlükler (Dictionaries): Sözlükler, anahtar-değer çiftleri olarak depolanan bir koleksiyondur. Python'da süslü parantez içinde virgülle ayrılmış anahtar-değer çiftleri olarak tanımlanırlar. 


kullaniciAdi = "ahmet"
kullaniciSifre = "18811938"

kullaniciAdi1 = input("Lutfen Kullanici Adinizi Giriniz :")
kullaniciSifre1 = input("Lutfen Sifrenizi Giriniz :")

if kullaniciAdi == kullaniciAdi1 and kullaniciSifre == kullaniciSifre1:
        print("Bilgileriniz doğru giriş yapiliyor.")
else:
    print("Bilgilerinizi kontrol ediniz.")