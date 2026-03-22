from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.calculator {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    width: 350px;
    box-shadow: 0 0 20px #3b82f6;
    transition: transform 0.2s;
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
    background: #111827;
    padding: 10px;
    border-radius: 12px;
    min-height: 40px;
}

.output-btn {
    width: 100%;
    margin-top: 10px;
    background: #10b981;
}

.clear-btn {
    width: 100%;
    margin-top: 10px;
    background: #ef4444;
}
</style>
</head>
<body>

<div class="calculator" id="calc">
    <input id="display" readonly>
    <div id="buttons"></div>
    <button class="output-btn" onclick="showAnswer()">Вывести ответ</button>
    <button class="clear-btn" onclick="clearDisplay()">C</button>
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
        // Злой эффект: случайное искажение
        if (Math.random() < 0.3 && !isNaN(res)) {
            let tweak = Math.floor(Math.random() * 3) + 1;
            res += Math.random() < 0.5 ? tweak : -tweak;
        }
        return res;
    } catch {
        return "Error";
    }
}

function showAnswer() {
    let res = calculate();
    resultDisplay.innerText = res;
    shuffleButtons();
}

// Хаос
function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}

function createButtons() {
    let container = document.getElementById("buttons");
    container.innerHTML = "";
    let buttons = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/",".","="];

    buttons.forEach(btn => {
        let b = document.createElement("button");
        b.innerText = btn;
        b.onclick = btn === "=" ? showAnswer : () => add(btn);
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
        b.onclick = texts[i] === "=" ? showAnswer : () => add(texts[i]);
    });
    let calc = document.getElementById("calc");
    calc.style.transform = `rotate(${Math.random()*6 - 3}deg)`;
}

createButtons();
</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML