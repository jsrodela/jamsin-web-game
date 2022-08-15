const socket = new WebSocket(
    "ws://" + window.location.host + "/ws/minesweeper/"
);

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

    send_command('set', { 'size': size, 'num': num });

    set_table(size);

    tdlist = document.getElementById("game_table").getElementsByTagName("td"); //테이블 td태그
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            tdlist[size * i + j].addEventListener("click", left_click(i, j));
            tdlist[size * i + j].addEventListener("contextmenu", right_click(i, j));
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

function left_click(x, y) {
    return function () {
        if (this.className == "covered" && this.innerHTML != "🚩") {
            send_command("uncover", { pos: [x, y] });
            this.className = "uncovered";
        }
    };
}

function right_click(x, y) {
    return function () {
        if (this.className == "covered") {
            if (this.innerHTML == "") {
                send_command("flag", { pos: [x, y] });
                this.innerHTML = "🚩";
            } else {
                send_command("unflag", { pos: [x, y] });
                this.innerHTML = "";
            }
        }
    };
}

function send_command(command, data) { // string, object (can be empty)
    data['command'] = command;
    socket.send(JSON.stringify(data));
}

function uncover(x, y, value) {
    const table = document.getElementById('game_table');
    const cell = table.rows[x].cells[y];
    cell.className = 'uncovered';
    if (value == -1) {
        cell.innerHTML = '💥';
    } else if (value == 0) {
        /* Leave blank */
    } else {
        cell.innerHTML = value;
    }
}

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    switch (data.command) {
        case 'uncover':
            const cells = data.cells;
            for (let i = 0; i < cells.length; i++) {
                const cell = cells[i];
                uncover(cell.x, cell.y, cell.value);
            }
            break;
        default:
            console.log(data);
            break;
    }
};
