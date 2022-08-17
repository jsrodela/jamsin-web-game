const socket = new WebSocket(
  "ws://" + window.location.host + "/ws/omok/"
);

document.body.oncontextmenu = () => { return false; };
document.body.onselectstart = () => { return false; };
document.body.ondragstart = () => { return false; };

/* False if it is opponent's turn */
let turn = false;

let color = null;
let opponentColor = null;

let tdlist;
let size = 15;

function set_game() {
  set_table(size);
  tdlist = document.getElementById("game_table").getElementsByTagName("td"); //테이블 td태그
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      tdlist[size * y + x].addEventListener("click", left_click(x, y));
    }
  }
}

function set_table(s) {
  //int
  let tag = '<table id="game_table" class="table_border">';
  for (let x = 1; x <= s; x++) {
    tag += '<tr>';
    for (let y = 1; y <= s; y++)
      tag +=
        '<td class="none"></td>';
    tag += '</tr>';
  }
  tag += '</table>';
  document.getElementById("area").innerHTML = tag;
}

function left_click(x, y) {
  return function () {
    if (!turn) {
      return;
    }
    if (this.className == "none") {
      send_command("place", x, y);
    }
  };
}

function send_command(command, x, y) {
  socket.send(JSON.stringify({
    command: command,
    pos: [x, y]
  }));
}

set_game();

socket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  if (data.room_id) {
    console.log("Room id: " + data.room_id);
  }

  if (data.color) {
    /* Check players' color and start the game */
    color = data.color;
    opponentColor = data.opponentColor;
    if (color == 'black') {
      turn = true;
    }
  }

  if (data.move) {
    const [x, y] = data.move;
    if (turn) {
      /* Place my stone */
      turn = false;
      tdlist[size * y + x].className = color;
    } else {
      /* Place opponent's stone */
      turn = true;
      tdlist[size * y + x].className = opponentColor;
    }
  }
};

socket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};
