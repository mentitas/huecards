let alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"];

window.onload = (event) => {
    changeColor()
};

function changeColor() {

    letter = alphabet[Math.floor(Math.random() * 16)];
    number = 1 + Math.floor(Math.random() * 30);

    formatted_number = ("0" + number).slice(-2);

    document.getElementById('background').style.backgroundColor = colors[letter][number]
    document.getElementById('label_color').textContent = letter + formatted_number;
}