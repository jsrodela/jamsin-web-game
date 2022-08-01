const socket = new WebSocket(
  "ws://" + window.location.host + "/ws/testgame/"
);

const gameMessageElm = document.getElementById("game-message");
const rematchBtn = document.getElementById("rematch");
const roomIdP = document.getElementById("room-id");

const winningMoves = [
  ["rock", "scissors"],
  ["scissors", "paper"],
  ["paper", "rock"],
];

let playerMove;
let opponentMove;
let waiting;

function reset() {
  playerMove = null;
  opponentMove = null;
  waiting = false;
  gameMessageElm.innerText = "";
  rematchBtn.style.display = "none";
}

reset();

function checkWin() {
  let message = "You lose";
  if (playerMove == opponentMove) {
    message = "Draw";
  }
  winningMoves.forEach((moves) => {
    if (playerMove == moves[0] && opponentMove == moves[1]) {
      message = "You win";
    }
  });
  gameMessageElm.innerText = message;
  rematchBtn.style.display = "";
}

socket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  if (data.room_id) {
    roomIdP.innerText = "Room id: " + data.room_id;
  }
  if (data.message) {
    document.querySelector("#chat-log").value += data.message + "\n";
  }
  if (data.move) {
    opponentMove = data.move;
    if (playerMove) {
      checkWin();
    }
  }
};

socket.onclose = function (e) {
  console.error("Chat socket closed unexpectedly");
};

document.querySelector("#chat-input").focus();
document.querySelector("#chat-input").onkeyup = function (e) {
  if (e.keyCode === 13) {
    // enter, return
    document.querySelector("#chat-send").click();
  }
};

document.querySelector("#chat-send").onclick = function (e) {
  const messageInputDom = document.querySelector("#chat-input");
  const message = messageInputDom.value;
  socket.send(
    JSON.stringify({
      message: message,
    })
  );
  messageInputDom.value = "";
};

document.querySelectorAll("#game-input > input").forEach((element) => {
  element.addEventListener("click", function (e) {
    if (!waiting) {
      playerMove = this.value;
      socket.send(
        JSON.stringify({
          play: this.value,
        })
      );
      if (opponentMove) {
        checkWin();
      } else {
        gameMessageElm.innerText = "Waiting for the opponent...";
        waiting = true;
      }
    }
  });
});

rematchBtn.addEventListener("click", function (e) {
  reset();
});
