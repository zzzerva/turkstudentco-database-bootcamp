# turkstudentco-database-bootcamp

Bu repo, Database Bootcamp kapsamında gerçekleştirilen SQL ödevlerini içermektedir. Her ödev, verilen sorulara uygun olarak yazılmış SQL sorgularını ve açıklamalarını içermektedir.

## İçindekiler
- [Ödev 1](#ödev-1)
- [Ödev 2](#ödev-2)

---

## Ödev 1
**Açıklama:**
Bu ödevde, verilen SQL sorularına uygun sorgular yazılmış ve her birinin detaylı açıklaması yapılmıştır.

**Sorular:**
1. **Çalışanların sadece FirstName, LastName ve Salary bilgilerini getirme**
   - `employees` tablosundan bu sütunları getiren bir sorgu yazın.

2. **Çalışanların çalıştıkları departmanları benzersiz olarak listeleme**
   - `employees` ve `departments` tablolarını JOIN ile birleştirin.
   - `DISTINCT` kullanarak tekrar eden departman isimlerini engelleyin.

3. **Sadece IT departmanında çalışanların bilgilerini getirme**
   - `INNER JOIN` kullanarak `departments` tablosunu bağlayın.
   - `WHERE` koşulu ile sadece IT departmanını filtreleyin.

4. **Çalışanları maaşlarına göre büyükten küçüğe sıralama**
   - `ORDER BY salary DESC` kullanarak sıralama yapın.

5. **Çalışanların FirstName ve LastName alanlarını birleştirerek tam adlarını içeren yeni bir sütun oluşturma**
   - `||` veya `CONCAT` fonksiyonunu kullanarak `full_name` sütununu oluşturun.
---

## Ödev 2
**Açıklama:**
Bu ödevde, verilen SQL sorularına uygun olarak sorgular yazılmış ve her birinin detaylı açıklaması yapılmıştır.

**Sorular:**
1. **Invoice tablosunda, tüm değerleri NULL olan kayıtların sayısını bulma**
   - Tek bir SQL sorgusu ile bu kayıtların sayısını bulun.
   - PostgreSQL’de satır sayısını yorum satırı olarak ekleyin.

2. **Total değerlerini iki katına çıkartarak eski ve yeni değerleri karşılaştırma**
   - Mevcut `total` sütununu ikiyle çarpıp `new_total` olarak adlandırın.
   - Sonuçları büyükten küçüğe sıralayın.

3. **Adres verisini belirli karakterlerle filtreleme ve 2013 Ağustos ayına göre listeleme**
   - `billing_address` sütununun ilk 3 ve son 4 karakterini alarak birleştirin.
   - 2013 yılının Ağustos ayında kesilen faturalar için filtreleme yapın.
---

## Kullanım
1. PostgreSQL veya uygun bir veritabanı yönetim sistemi kullanarak SQL dosyalarını çalıştırın.
2. Her ödev için verilen açıklamalar doğrultusunda sorguları test edin ve çıktıları inceleyin.

**Lisans:** Bu repo eğitim amaçlı hazırlanmıştır.


