let colors = [];
let currentIndex = 0;

window.onload = (event) => {
    fetchColors();
};

function fetchColors() {
    fetch('colors.json')
        .then(response => response.json())
        .then(data => console.log(data));
}

function getRandomColor(){
  return colors[Math.floor(Math.random() * colors.length)];
}

function changeColor() {
    document.getElementById('background').style.backgroundColor = getRandomColor()
    document.getElementById('label_color').textContent = colors;
}