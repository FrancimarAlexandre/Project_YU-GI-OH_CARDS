let player1Life = 8000;
let player2Life = 8000;

function decreaseLife(player) {
    if (player === 'player1') {
        player1Life = Math.max(player1Life - 1000, 0);
        document.getElementById('player1-life').textContent = player1Life;
    } else if (player === 'player2') {
        player2Life = Math.max(player2Life - 1000, 0);
        document.getElementById('player2-life').textContent = player2Life;
    }
}

function increaseLife(player) {
    if (player === 'player1') {
        player1Life += 1000;
        document.getElementById('player1-life').textContent = player1Life;
    } else if (player === 'player2') {
        player2Life += 1000;
        document.getElementById('player2-life').textContent = player2Life;
    }
}
