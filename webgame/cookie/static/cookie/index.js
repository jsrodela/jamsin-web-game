const vid1Elm = document.getElementById("vid1");
Math.floor(Math.random() * 8);

const container = document.getElementById("Videocontainer");

// Add shake effect on click
container.addEventListener('click', function () {
    // Add shake class
    this.className = 'shake';
    // Remove shake class after 500 ms (0.5 s)
    setTimeout(function (element) { element.className = ''; }, 500, this);
});

// 문서 안 모든 이미지 가져오기
const imgs = document.querySelectorAll('img');

// 이미지에 event Listener 추가
imgs.forEach(element => {
    element.addEventListener("click", function () {
        // 일정 시간 후 함수 실행
        setTimeout(function (element) {
            aud1.play();
            
            // 현재 이미지 숨기기
            element.style.display = 'none';

            // 다음 이미지 보이기
            element.nextElementSibling.style.display = '';
        }, 1000, this); // TODO 1000 대신 적당한 화면 전환 시간 넣기
    });

});

vid1Elm.addEventListener("click", function () {
    this.play();
    setTimeout(() => { aud2.play(); }, 1350);
});
vid1Elm.addEventListener("ended", function () {
    aud3.play(); this.style.display = "none";
    const video = document.createElement("video");
    const sourceElm = document.createElement("source");
    video.id = "unsae";
    video.setAttribute("width", "70%");
    switch (Math.floor(Math.random() * 21)) {
        case 0:
            sourceElm.setAttribute("src", "문구 1.mp4");
            break;
        case 1:
            sourceElm.setAttribute("src", "문구 2.mp4");
            break;
        case 2:
            sourceElm.setAttribute("src", "문구 3.mp4");
            break;
        case 3:
            sourceElm.setAttribute("src", "문구 4.mp4");
            break;
        case 4:
            sourceElm.setAttribute("src", "문구 5.mp4");
            break;
        case 5:
            sourceElm.setAttribute("src", "문구 1.mp4");
            break;
        case 6:
            sourceElm.setAttribute("src", "문구 2.mp4");
            break;
        case 7:
            sourceElm.setAttribute("src", "문구 3.mp4");
            break;
        case 8:
            sourceElm.setAttribute("src", "문구 4.mp4");
            break;
        case 9:
            sourceElm.setAttribute("src", "문구 5.mp4");
            break;
        case 10:
            sourceElm.setAttribute("src", "문구 1.mp4");
            break;
        case 11:
            sourceElm.setAttribute("src", "문구 2.mp4");
            break;
        case 12:
            sourceElm.setAttribute("src", "문구 3.mp4");
            break;
        case 13:
            sourceElm.setAttribute("src", "문구 4.mp4");
            break;
        case 14:
            sourceElm.setAttribute("src", "문구 5.mp4");
            break;
        case 15:
            sourceElm.setAttribute("src", "당첨 글.mp4");
            break;
        case 16:
            sourceElm.setAttribute("src", "당첨 글.mp4");
            break;
        case 17:
            sourceElm.setAttribute("src", "문양.mp4");
            break;
        case 18:
            sourceElm.setAttribute("src", "꽝.mp4");
            break;
        case 19:
            sourceElm.setAttribute("src", "꽝.mp4");
            break;
        case 20:
            sourceElm.setAttribute("src", "꽝.mp4");
            break;
    }
    video.appendChild(sourceElm);
    container.appendChild(video);
    video.play();
});
