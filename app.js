document.getElementById("questionForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = {};

  formData.forEach((value, key) => {
    data[key] = parseInt(value);  // sayısal veri olarak ilet
  });

  fetch("/tahmin", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((json) => {
      if (json.tahmin) {
        document.getElementById("resultText").innerText = json.tahmin;
        document.getElementById("responseContainer").classList.remove("hidden");
      } else if (json.error) {
        alert("Hata: " + json.error);
      }
    })
    .catch((err) => {
      alert("Sunucuya bağlanırken bir hata oluştu: " + err);
    });
});
