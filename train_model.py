import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Veriyi yükle
df = pd.read_csv("kişilik.csv")

# Giriş ve hedef değişkenleri ayır
X = df.drop("Personality", axis=1)
y = df["Personality"]

# Yes içe dönüklüğü gösteriyorsa, Yes'e 0, No'ya 1 ver
X = X.applymap(lambda x: 0 if x == "Yes" else 1)


# Kategori hedefini encode et
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Ölçekleme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Eğitim / test böl
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Modeli eğit
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# Kaydet
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")
joblib.dump(scaler, "scaler.pkl")

# Doğruluk çıktısı
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print("Doğruluk:", accuracy_score(y_test, y_pred))

print(X.columns)

