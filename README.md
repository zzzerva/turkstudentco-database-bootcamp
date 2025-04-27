# TurkStudentCo-Database-Bootcamp

Bu repo, **Database Bootcamp** kapsamında gerçekleştirilen SQL ödevlerini içermektedir.  
Her ödev, verilen sorulara uygun olarak yazılmış **SQL sorgularını** ve **açıklamalarını** içermektedir.

## İçindekiler
- [Ödev 1](#ödev-1)
- [Ödev 2](#ödev-2)
- [Ödev 3](#ödev-3)
- [Ödev 4](#ödev-4)

---

## Ödev 1

### Açıklama
Bu ödevde, verilen **SQL sorularına** uygun sorgular yazılmış ve her birinin **detaylı açıklaması** yapılmıştır.

### Sorular
- Çalışanların sadece **FirstName**, **LastName** ve **Salary** bilgilerini getirme
- Çalışanların çalıştıkları **departmanları benzersiz** olarak listeleme
- Sadece **IT departmanında** çalışanların bilgilerini getirme
- Çalışanları **maaşlarına göre büyükten küçüğe** sıralama
- Çalışanların **FirstName** ve **LastName** alanlarını birleştirerek **full_name** oluşturma

---

## Ödev 2

### Açıklama
Bu ödevde, verilen **SQL sorularına** uygun olarak sorgular yazılmış ve her birinin **detaylı açıklaması** yapılmıştır.

### Sorular
- **Invoice** tablosunda, **tüm değerleri NULL** olan kayıtların sayısını bulma
- **Total** değerlerini **iki katına çıkartarak** eski ve yeni değerleri karşılaştırma
- **Adres verisini belirli karakterlerle filtreleme** ve **2013 Ağustos** ayına göre listeleme

---

## Ödev 3

### Açıklama
Bu ödevde, verilen **SQL sorularına** uygun olarak sorgular yazılmış ve her birinin **detaylı açıklaması** yapılmıştır.

### Sorular
- **2009 yılında, "USA" ülkesine ait tüm faturaların toplamını listeleyen sorgu**
- **Parça (track) bilgilerini playlisttrack ve playlist tablolarıyla birleştirerek listeleme**
- **"Let There Be Rock" albümündeki tüm parçaları sanatçı bilgisiyle birlikte getirme**

---

## Ödev 4

### Açıklama
Bu ödevde, bir **çevrimiçi eğitim platformu** için kapsamlı bir **veritabanı şeması** tasarlanmış ve gerekli **SQL kodları** yazılmıştır.  
Çalışmada tabloların doğru şekilde tanımlanması, birincil anahtar (PK), yabancı anahtar (FK) ve tekil anahtar (UK) kısıtlamalarının etkin kullanımı hedeflenmiştir.

### Yapılanlar
- **members**, **categories**, **courses**, **enrollments**, **certificates**, **certificate_assignments** ve **blog_posts** tabloları oluşturuldu.
- **Foreign Key (FK)** kullanılarak tablolar arası ilişkiler kuruldu.
- **Primary Key (PK)** ve **Unique Key (UK)** kısıtlamaları tanımlandı.
- **Varsayılan değerler (DEFAULT)** atandı.
- Performansı artırmak için **INDEX** tanımlamaları yapıldı.
- `categories` tablosuna örnek veri eklenmiştir.

### Kullanılan Tablolar
- members
- categories
- courses
- enrollments
- certificates
- certificate_assignments
- blog_posts

### Uygulanan Kısıtlamalar
- Primary Key (PK)
- Foreign Key (FK)
- Unique Key (UK)
- Default değerler
- Index kullanımı

### Dosya İçeriği
- SQL Kodları: `education_platform_schema.sql`
- (Opsiyonel) Şema Görseli: `erd_diagram.png`

---

## Kullanım
**PostgreSQL** veya uygun bir **veritabanı yönetim sistemi** kullanarak SQL dosyalarını çalıştırın.  
Her ödev için verilen açıklamalar doğrultusunda **sorguları test edin** ve çıktıları inceleyin.

---

## Lisans
Bu repo **eğitim amaçlı** hazırlanmıştır.

---
