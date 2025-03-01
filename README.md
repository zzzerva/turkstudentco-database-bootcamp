# turkstudentco-database-bootcamp
Database Bootcamp 1. Ödev: SQL sorguları ve açıklamaları.

# Database Bootcamp – Ödev 1

Bu ödevde, verilen SQL sorularına uygun sorgular yazıldı ve her birinin açıklaması detaylandırıldı.

---

## **1. Soru: Çalışanların sadece FirstName, LastName ve Salary bilgilerini getiren bir SQL sorgusu yazınız.**

### **SQL Sorgusu:**
```sql
SELECT firstname, lastname, salary
FROM employees;
```
### **Açıklama:**
Bu sorguda, `employees` tablosundan **firstname**, **lastname** ve **salary** sütunlarını çektim.

**FROM** ifadesi, bu verilerin hangi tablodan çekileceğini belirtir. Ayrıca, ihtiyaca göre belirli sütunları ayrı ayrı sorgulayarak da veri çekebiliriz:
```sql
SELECT firstname FROM employees;
SELECT lastname FROM employees;
SELECT salary FROM employees;
```
Bu sorgularla yalnızca istenen sütunları da çekebiliriz.

---

## **2. Soru: Çalışanların çalıştıkları departmanları benzersiz olarak listeleyen bir SQL sorgusu yazınız.**

### **SQL Sorgusu:**
```sql
SELECT DISTINCT d.departmentname
FROM employees e
INNER JOIN departments d ON e.departmentid = d.departmentid;
```
### **Açıklama:**
Bu sorguda, `employees` ve `departments` tablolarını **INNER JOIN** ile `departmentid` sütunu üzerinden birleştirdim.

**INNER JOIN** tercih etmemin sebebi, yalnızca eşleşen satırları getirmek istemem ve bu işlemin **JOIN** işlemine kıyasla daha düşük maliyetli olmasıdır.

Daha sonra, çalışanların bağlı olduğu `departmentname` sütununu sorguya dahil ettim. **DISTINCT** ifadesi, tekrar eden departman isimlerini engelleyerek her departmanı yalnızca bir kez listelememi sağladı.

---

## **3. Soru: Sadece IT departmanında çalışanların bilgilerini getiren bir SQL sorgusu yazınız.**

### **SQL Sorgusu:**
```sql
SELECT * FROM employees e
INNER JOIN departments d ON e.departmentid = d.departmentid
WHERE d.departmentname = 'IT';
```
### **Açıklama:**
Bu sorguda, `employees` tablosundaki tüm sütunları seçtim ve **INNER JOIN** kullanarak `departments` tablosuyla `departmentid` sütunu üzerinden birleştirdim.

**WHERE** koşulunda yalnızca `departmentname` değeri **"IT"** olan satırların getirilmesini sağladım.

Ayrıca, tablo adlarını **`employees e`** ve **`departments d`** olarak kısaltarak kullandım. Bu sayede, `departments.departmentname` yerine `d.departmentname` gibi daha sade bir yazım kullanarak sorguyu daha okunaklı hale getirdim.

---

## **4. Soru: Çalışanları maaşlarına göre büyükten küçüğe sıralayan bir SQL sorgusu yazınız.**

### **SQL Sorgusu:**
```sql
SELECT e.firstname, e.lastname, e.salary
FROM employees e
ORDER BY e.salary DESC;
```
### **Açıklama:**
Bu sorguda, `employees` tablosundan **firstname**, **lastname** ve **salary** sütunlarını seçtim. **ORDER BY** ifadesi, sorgu sonucundaki verileri belirli bir sütuna göre sıralamak için kullanılır.

Bu örnekte, sıralamanın `salary` sütununa göre yapılması gerektiği için **ORDER BY salary** ifadesini kullandım. Maaşların büyükten küçüğe sıralanmasını sağlamak için **DESC** ifadesini ekledim.

---

## **5. Soru: Çalışanların FirstName ve LastName alanlarını birleştirerek, tam adlarını içeren yeni bir sütun oluşturan bir SQL sorgusu yazınız.**

### **SQL Sorgusu:**
```sql
SELECT CONCAT(e.firstname, ' ', e.lastname) AS full_name
FROM employees e;
```
### **Açıklama:**
Bu sorguda, çalışanların **firstname** ve **lastname** sütunlarını birleştirerek tam isimlerini içeren **full_name** adında yeni bir sütun oluşturdum. **CONCAT** fonksiyonu, MySQL gibi veritabanlarında metinleri birleştirmek için kullanılır.

**PostgreSQL** gibi sistemlerde `|| ' ' ||` operatörü kullanılsa da, **Tuncay hocamız**, MySQL’de **CONCAT** fonksiyonunun kullanılması gerektiğini belirtti.

Ayrıca, `' '` ifadesini ekleyerek ad ve soyad arasında bir boşluk olmasını sağladım. **AS full_name** ifadesiyle de oluşturduğum yeni sütuna anlamlı bir isim verdim.

---

Bu ödevde, farklı SQL sorgularını kullanarak belirlenen kriterlere uygun veri çekme işlemleri gerçekleştirildi. **SQL'in temel sorgulama yapıları** olan **SELECT, JOIN, WHERE, DISTINCT ve ORDER BY** gibi ifadeler pratik edildi. 
