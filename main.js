let form = document.querySelector('form');
form.addEventListener('submit', runEvent);

function runEvent(e) {
  e.preventDefault();
  let numPlayersVal = document.getElementById('num-players').value;
  let playerTypeVal = document.getElementById('player-type').value;
  console.log(numPlayersVal);
  console.log(playerTypeVal);
}
