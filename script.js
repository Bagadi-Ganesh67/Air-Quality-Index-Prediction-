document.getElementById("aqiForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let inputData = {
        "PM2.5": parseFloat(document.getElementById("pm25").value),
        "PM10": parseFloat(document.getElementById("pm10").value),
        "NO": parseFloat(document.getElementById("no").value),
        "NO2": parseFloat(document.getElementById("no2").value),
        "NOx": parseFloat(document.getElementById("nox").value),
        "NH3": parseFloat(document.getElementById("nh3").value),
        "CO": parseFloat(document.getElementById("co").value),
        "SO2": parseFloat(document.getElementById("so2").value),
        "O3": parseFloat(document.getElementById("o3").value),
        "Benzene": parseFloat(document.getElementById("benzene").value),
        "Toluene": parseFloat(document.getElementById("toluene").value),
        "Xylene": parseFloat(document.getElementById("xylene").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.aqi) {
            document.getElementById("result").innerText = "Predicted AQI: " + data.aqi;
        } else {
            document.getElementById("result").innerText = "Error: " + data.error;
        }
    })
    .catch(error => {
        document.getElementById("result").innerText = "Error: " + error.message;
    });
});
