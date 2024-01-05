let form = document.querySelector('.selection-box');
form.addEventListener('submit', runEvent);

function runEvent(e) {
  e.preventDefault();
  let numPlayers = parseInt(document.getElementById('num-players').value);
  let playerType = document.getElementById('player-type').value;
  // console.log(numPlayersVal);
  // console.log(playerTypeVal);
  fetchRandomPlayers(numPlayers, playerType);
}

function fetchRandomPlayers(numPlayers, playerType) {
  let xhr = new XMLHttpRequest();
  xhr.open(
    'GET',
    `http://127.0.0.1:8000/api/random/?numplayers=${numPlayers}&type=${playerType}`,
    true
  );

  xhr.onload = function () {
    if (this.status == 200) {
      let players = JSON.parse(this.responseText);
      let output = '';
      for (let i in players) {
        output += `<div class="player">${players[i].first_name} ${players[i].last_name}
        <img class="player-image" src="https://cdn.nba.com/headshots/nba/latest/260x190/${players[i].nba_id}.png" alt=""></div>`;
      }

      document.querySelector('.players').innerHTML = output;
    }
  };

  xhr.send();
}
