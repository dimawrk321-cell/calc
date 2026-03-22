from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Chaos Calculator</title>

<style>
body {
    background: #0f172a;
    color: white;
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.calculator {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    width: 300px;
}

input {
    width: 100%;
    padding: 15px;
    font-size: 20px;
    border-radius: 10px;
    border: none;
    margin-bottom: 10px;
}

#buttons {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
}

button {
    padding: 15px;
    font-size: 18px;
    border: none;
    border-radius: 10px;
    background: #3b82f6;
    color: white;
    cursor: pointer;
}

.result {
    margin-top: 10px;
    font-size: 22px;
    text-align: right;
}
</style>
</head>

<body>

<div class="calculator">
    <input id="display" readonly>
    <div id="buttons"></div>
    <button style="width:100%; margin-top:10px;" onclick="clearDisplay()">C</button>
    <div class="result" id="result"></div>
</div>

<script>
let display = document.getElementById("display");

function add(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = "";
    document.getElementById("result").innerText = "";
}

function calculate() {
    try {
        let result = eval(display.value);
        document.getElementById("result").innerText = result;
    } catch {
        document.getElementById("result").innerText = "Error";
    }
}

// 🔥 хаос
function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}

function createButtons() {
    let container = document.getElementById("buttons");

    let buttons = [
        "0","1","2","3","4","5","6","7","8","9",
        "+","-","*","/",".","="
    ];

    buttons = shuffle(buttons);

    buttons.forEach(btn => {
        let b = document.createElement("button");
        b.innerText = btn;

        if (btn === "=") {
            b.onclick = calculate;
        } else {
            b.onclick = () => add(btn);
        }

        container.appendChild(b);
    });
}

createButtons();
</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML