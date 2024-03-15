var button = document.getElementById("mem_log").addEventListener("click", lo1)

function lo1(event) {
    event.preventDefault();
    var email = document.getElementById('mem_email');
    var password = document.getElementById('mem_pass');
    data = {
        Email_ID: email.value,
        Password: password.value
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:3000/login_member');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the response data
        var data = JSON.parse(xhr.responseText);
        alert("login successful");
        window.location.replace("member_page.html");
    }
    else if (xhr.readyState === 4 && xhr.status !== 200) {
        // Handle any errors
        alert('Invalid Credentials: ' + xhr.status);
    }
    };

    // Send the updated JSON data in the request body
    xhr.send(JSON.stringify(data));

}

var button = document.getElementById("lib_log").addEventListener("click", lo2)

function lo2(event) {
    event.preventDefault();
    // console.log("hello")
    var email = document.getElementById('lib_email');
    var password = document.getElementById('lib_pass');
    data = {
        Email_ID: email.value,
        Password: password.value
    }
    
    // console.log(data);
    var xhr = new XMLHttpRequest();
    // alert(data)
    xhr.open('POST', 'http://127.0.0.1:3000/login_librarian');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the response data
        var data = JSON.parse(xhr.responseText);
        alert("Logged in as Librarian");
        window.location.replace("librarian_page.html");
    }
    else if (xhr.readyState === 4 && xhr.status !== 200) {
        // Handle any errors
        alert('Invalid Credentials: ' + xhr.status);
    }
    };
    xhr.send(JSON.stringify(data));

}
