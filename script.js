let colors = [];
let currentIndex = 0;

window.onload = (event) => {
    fetchColors();
};

function fetchColors() {
    fetch('./colors.csv')
        .then(response => response.json())
        .then(data => console.log(data));
}

function changeColor() {
    document.getElementById('background').style.backgroundColor = 'red'
    document.getElementById('label_color').textContent = colors;
}