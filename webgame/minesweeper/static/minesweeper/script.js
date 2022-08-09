document.body.oncontextmenu = () => { return false; };
document.body.onselectstart = () => { return false; };
document.body.ondragstart = () => { return false; };

let size;
let num;
let tdlist;

const startBtn = document.getElementById("startBtn");
startBtn.addEventListener("click", set_game);

function set_game() {
    size = parseInt(document.getElementById("size").value); //판 사이즈
    num = parseInt(document.getElementById("num").value); //지뢰 개수
    set_table(size);

    tdlist = document.getElementById("game_table").getElementsByTagName('td'); //테이블 td태그
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            tdlist[size * i + j].addEventListener("click", left_click);
            tdlist[size * i + j].addEventListener("contextmenu", right_click);
        }
    }
}

function set_table(s) //int
{
    let tag = "<table id=\"game_table\" class=\"table_border\">";
    for (let i = 1; i <= s; i++) {
        tag += "<tr>";
        for (let j = 1; j <= s; j++)
            tag += "<td id=" + ((i - 1) * s + j - 1) + " class=\"covered\"></td>";
        tag += "</tr>";
    }
    tag += "</table>";
    document.getElementById("area").innerHTML = tag;
}

function left_click() {
    if (this.innerHTML != "🚩") {
        this.className = "uncovered";
    }
}

function right_click() {
    if (this.className == "covered") {
        this.innerHTML = "🚩";
    }
}
