// Get the button element with the id "my-button"
var button = document.getElementById("submit_button").addEventListener("click", sub)

// Add a click event listener to the button
function sub() {
    var form = document.querySelector('form');

    // Get the form controls
    var controls = form.elements;

    var firstName = controls['first_name'].value;
    var middleName = controls['middle_name'].value;
    var lastName = controls['last_name'].value;
    var email = controls['email'].value;
    var password = controls['user_password'].value;
    var city = controls['city'].value;
    var state = controls['state'].value;
    var zip = controls['zip'].value;
    var phone = controls['phone'].value;

    // alert(phone);
    data = {
        Email_ID: email,
        Password: password,
        First_Name: firstName,
        Middle_Name: middleName,
        Last_Name: lastName,
        City: city,
        State: state,
        Zip: zip,
        Phone: phone,
    }


    var xhr = new XMLHttpRequest();

    xhr.open('POST', 'http://127.0.0.1:3000/signup_member');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
    if (xhr.status === 200) {
        // Handle the response data
        var data = JSON.parse(xhr.responseText);
        alert(data);
    }
    else if (xhr.readyState === 4 && xhr.status !== 200) {
        // Handle any errors
        alert('Error: ' + xhr.status);
    }
    };

    // Send the updated JSON data in the request body
    xhr.send(JSON.stringify(data));


}
