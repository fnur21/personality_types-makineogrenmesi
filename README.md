# Kişilik Tipi Tahmini (Introvert vs Extrovert) – Makine Öğrenmesi Projesi

Bu projede, bireylerin sosyal davranışlarını temel alarak kişilik tiplerini (içe dönük veya dışa dönük) tahmin edebilen bir makine öğrenmesi modeli geliştirildi. Ardından bu modeli kullanarak HTML, CSS ve JavaScript ile hazırlanan bir arayüz üzerinden Flask yardımıyla gerçek zamanlı tahmin yapılması sağlandı.

---

## 🎯 Proje Amacı

Sosyal medya alışkanlıkları, yalnızlık tercihi, sosyalleşme düzeyi gibi bireysel davranışlar kullanılarak, kişinin **Introvert (içe dönük)** ya da **Extrovert (dışa dönük)** kişilik yapısına sahip olup olmadığını tahmin etmek.

---

## 📊 Veri Kümesi

- **Toplam Satır Sayısı:** 2900
- **Bağımsız Değişken Sayısı:** 8
- **Hedef Değişken:** Kişilik tipi (Introvert = 0, Extrovert = 1)
- **Veri Tipi:** Evet/Hayır (Yes/No) türündeki kategorik veriler

### 🔧 Ön İşleme Adımları

- Yes/No türündeki veriler 1/0’a dönüştürüldü
- Eksik veriler `0` ile dolduruldu
- `LabelEncoder` ile hedef değişken dönüştürüldü
- `StandardScaler` ile veriler normalize edildi
- Eğitim/Test ayrımı: %80 - %20

---

## 🤖 Kullanılan Algoritmalar

1. **Logistic Regression**
2. **Random Forest**
3. **Support Vector Machine (SVM)** → ✅ **En başarılı model**

Tüm modeller `class_weight='balanced'` ile dengesiz veri durumuna göre optimize edildi.

---

## 📈 Değerlendirme Metrikleri

- Accuracy (Doğruluk)
- Precision
- Recall
- F1-score
- ROC Eğrisi

📌 **En yüksek doğruluk SVM modeliyle elde edildi (%90+ başarı).**


## 💻 Arayüz Tasarımı

Projeye ait bir test arayüzü geliştirildi. Bu arayüzde kullanıcıya 7 soru soruluyor ve verilen cevaplara göre Flask destekli model, kişilik tipi tahmini yapıyor.

### Kullanılan Teknolojiler:

- **Backend:** Python + Flask
- **Frontend:** HTML, CSS, JavaScript
- **Model:** Eğitilmiş SVM modeli `.pkl` olarak yüklendi ve Flask üzerinden kullanıldı

---

