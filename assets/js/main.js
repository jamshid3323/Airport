const backToTopButton = document.querySelector('#top');

window.addEventListener("scroll", scrollFunction);

function scrollFunction() {
    if (window.pageYOffset > 300) {
        if (!backToTopButton.classList.contains("btnEntrance")) {
            backToTopButton.classList.remove("btnExit")
            backToTopButton.classList.add("btnEntrance")
            backToTopButton.style.display = "block";
        }
    } else {
        if (!backToTopButton.classList.contains("btnExit")) {
            backToTopButton.classList.remove("btnEntrance")
            backToTopButton.classList.add("btnExit")
            backToTopButton.style.display = "none";
        }
    }
}

backToTopButton.addEventListener("click", backToTop);

function backToTop() {
    window.scrollTo(0, 0);
}

function checkOne() {
    var one = document.getElementById("oneway");
    var multi = document.getElementById("multi");
    var round = document.getElementById("round");
    var roundTrip = document.getElementById("roundTrip");
    var oneWay = document.getElementById("one");
    var input = document.getElementById('multiCity');
    if (one.checked == true) {
        round.checked = false;
        multi.checked = false;
        oneWay.style.display = "block";
        input.style.display = "none";
        roundTrip.style.display = "none";
    } else if (round.checked == false && one.checked == false && multi.checked == false) {
        oneWay.style.display = "block";
    } else {
        oneWay.style.display = "none";
    }
}

function checkRound() {
    var round = document.getElementById("round");
    var one = document.getElementById("oneway");
    var multi = document.getElementById("multi");
    var roundTrip = document.getElementById("roundTrip");
    var input = document.getElementById('multiCity');
    var oneWay = document.getElementById("one");
    if (round.checked == true) {
        one.checked = false;
        multi.checked = false;
        roundTrip.style.display = "block";
        input.style.display = "none";
        oneWay.style.display = "none";
    } else if (round.checked == false && one.checked == false && multi.checked == false) {
        oneWay.style.display = "block";
        roundTrip.style.display = "none";
    } else {
        roundTrip.style.display = "none";
    }
}

function checkMulti() {
    var multi = document.getElementById("multi");
    var one = document.getElementById("oneway");
    var round = document.getElementById("round");
    var input = document.getElementById('multiCity');
    var roundTrip = document.getElementById("roundTrip");
    var oneWay = document.getElementById("one");
    if (multi.checked == true) {
        one.checked = false;
        round.checked = false;
        input.style.display = "block";
        roundTrip.style.display = "none";
        oneWay.style.display = "none";
    } else if (round.checked == false && one.checked == false && multi.checked == false) {
        oneWay.style.display = "block";
        input.style.display = "none";
    } else {
        input.style.display = "none";
    }
}
