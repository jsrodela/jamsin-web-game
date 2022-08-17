const socket = new WebSocket(
    "ws://" + window.location.host + "/ws/minesweeper/"
);

document.body.oncontextmenu = () => { return false; };
document.body.onselectstart = () => { return false; };
document.body.ondragstart = () => { return false; };

let num;
let tableElm;

const startBtn = document.getElementById("startBtn");
startBtn.addEventListener("click", set_game);

const sizeWidthInput = document.getElementById("size-width");
const sizeHeightInput = document.getElementById("size-height");
const numInput = document.getElementById("num");

const inputList = [sizeWidthInput, sizeHeightInput, numInput];
inputList.forEach(inputElm => {
    inputElm.addEventListener("keypress", (event) => {
        if (event.key == "Enter") {
            if (inputList.every((element) => { return element.value; })) {
                set_game();
            }
        }
    });
});

function set_game() {
    width = parseInt(sizeWidthInput.value); // Board width (cells)
    height = parseInt(sizeHeightInput.value); // Board height (cells)
    num = parseInt(numInput.value); // Number of mines

    send_command('set', { 'width': width, 'height': height, 'num': num });

    set_table(width, height);

    tableElm = document.getElementById('game_table');
    for (let x = 0; x < width; x++) {
        for (let y = 0; y < height; y++) {
            tableElm.rows[y].cells[x].addEventListener("click", left_click(x, y));
            tableElm.rows[y].cells[x].addEventListener("contextmenu", right_click(x, y));
        }
    }
}

function set_table(width, height) {
    let tag = '<table id="game_table" class="table_border">';
    for (let y = 1; y <= height; y++) {
        tag += '<tr>';
        for (let x = 1; x <= width; x++)
            tag += '<td class="covered"></td>';
        tag += '</tr>';
    }
    tag += '</table>';
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
    const cell = tableElm.rows[y].cells[x];
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
