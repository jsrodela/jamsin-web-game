document.body.oncontextmenu = () => {
  return false;
};
document.body.onselectstart = () => {
  return false;
};
document.body.ondragstart = () => {
  return false;
};

let size;
let num;
let tdlist;

function set_game() {
  size = parseInt(document.getElementById("size").value);
  num = parseInt(document.getElementById("num").value);

  set_table(size);

  tdlist = document.getElementById("game_table").getElementsByTagName("td"); //테이블 td태그
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      tdlist[size * i + j].addEventListener("click", left_click(i, j));
    }
  }
}

function set_table(s) {
  //int
  let tag = '<table id="game_table" class="table_border">';
  for (let i = 1; i <= 15; i++) {
    tag += "<tr>";
    for (let j = 1; j <= 15; j++)
      tag +=
        "<td id=" +
        ((i - 1) * 15 + j - 1) +
        ' class="covered"><img src="../static/omok/omok.PNG" width= 50 height= 50> </td>';
    tag += "</tr>";
  }
  tag += "</table>";
  document.getElementById("area").innerHTML = tag;
}

function left_click(x, y) {
  return function () {
    if (this.className == "covered" && this.innerHTML != "🚩") {
      send_command("uncover", x, y);
      this.className = "uncovered";
    }
  };
}

function send_command(command, x, y) {}

set_table(20);
