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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.calculator {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    width: 320px;
    box-shadow: 0 0 20px #3b82f6;
}

input {
    width: 100%;
    padding: 15px;
    font-size: 22px;
    border-radius: 12px;
    border: none;
    margin-bottom: 15px;
    text-align: right;
}

#buttons {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
}

button {
    padding: 15px;
    font-size: 18px;
    border: none;
    border-radius: 12px;
    background: #3b82f6;
    color: white;
    cursor: pointer;
    transition: 0.2s;
}

button:hover {
    transform: scale(1.1);
    background: #2563eb;
}

.result {
    margin-top: 15px;
    font-size: 24px;
    text-align: right;
    color: #facc15;
}
</style>
</head>
<body>

<div class="calculator">
    <input id="display" readonly>
    <div id="buttons"></div>
    <button style="width:100%; margin-top:10px; background:#ef4444;" onclick="clearDisplay()">C</button>
    <div class="result" id="result"></div>
</div>

<script>
let display = document.getElementById("display");
let resultDisplay = document.getElementById("result");

function add(value) {
    display.value += value;
    shuffleButtons();
}

function clearDisplay() {
    display.value = "";
    resultDisplay.innerText = "";
    shuffleButtons();
}

function calculate() {
    try {
        let res = eval(display.value);
        resultDisplay.innerText = res;
    } catch {
        resultDisplay.innerText = "Error";
    }
    shuffleButtons();
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

function shuffleButtons() {
    let container = document.getElementById("buttons");
    let buttons = Array.from(container.children);
    let texts = buttons.map(b => b.innerText);
    texts = shuffle(texts);

    buttons.forEach((b, i) => {
        b.innerText = texts[i];
        b.onclick = texts[i] === "=" ? calculate : () => add(texts[i]);
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