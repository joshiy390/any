var username;

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0px";
}


function setvis(uname) {
    var create = document.getElementsByClassName("create");
    if(uname === "") {
        document.getElementById("username").style.visibility = "hidden";
        document.getElementById("profilepic").style.visibility = "hidden";
        document.getElementById("log").innerText = "Log In";
        document.getElementById("log").href = "/login";
        create.display = "none"
    } else {
        document.getElementById("username").style.visibility = "visible";
        document.getElementById("username").innerText = "Hello, " + uname;
        document.getElementById("profilepic").style.visibility = "visible";
        document.getElementById("log").innerText = "Log Out";
        document.getElementById("log").href = "/logout";
        create.display = "initial";
    }
}

function random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function getWidth() {
    var width = document.getElementById("username").clientWidth;
    var truewidth = 17 + width + 5;
    var fullwidth = truewidth + "px";
    document.getElementById("profilepic").style.right = fullwidth;
}

function getCookieInfo() {
    username = document.getElementById("username_").innerText;
    return username;
}

function setCookie(uname, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = "username=" + uname + ";" + expires;
}

function decodeCookies() {
    var cookies = document.cookie
                      .split(';')
                      .map(cookie => cookie.split('='))
                      .reduce((accumulator, [key, value]) =>
                             ({ ...accumulator, [key.trim()]: decodeURIComponent(value) }),
                             {});

    return cookies;
}

function splashText(uname) {
    var comma;
    var number = random(1, 7);

    if(uname === "") {
        comma = "";
    } else {
        if(number != 6) {
            comma = ", ";
        } else {
            comma = ".";
        }
    }

    if(number === 1) {
        console.log("Hello there" + comma + uname + "!");
    } else if(number === 2) {
        console.log("Stealing cookies out the jar" + comma + uname + "?");
    } else if(number === 3) {
        console.log("Hey there" + comma + uname + "! Logging some code?");
    } else if(number === 4) {
        console.log("Why are you here" + comma + uname + '? Trying to impress your friends with your "coding skills"?');
    } else if(number === 5) {
        console.log("Computer unstable: SYSTEM_FAN_BLADE_TIP.SPEED > 1.15572735 ATTOPARSECS_PER_MICROFORTNIGHT."
                    + " Consider initiating SELF_DESTRUCT.SEQUENCE.RAPID."
                    + " Failure may result in your storage device spontaneoustly teleporting.");
    } else {
        console.log("Hmm. " + uname + comma);
    }

}

function tried() {
    var button = document.getElementById("unbecome");
    var step;

    if (button.innerText === "Delete Account") {
        button.innerText = "Press this only if you're sure";
        step = 1;
    } else if (button.innerText === "Press this only if you're sure") {
        button.innerText = "OK, but are you sure?";
        step = 2
    } else {
        button.innerText = "Do it.";
    }
}

window.onload = function() {
    uname = getCookieInfo();
    setvis(uname);
    getWidth();
    setCookie(uname, 30);
    var cookies = decodeCookies();
    splashText(cookies.username);

    console.log("Support Any.io on www.patreon.com/Fantastik");
};