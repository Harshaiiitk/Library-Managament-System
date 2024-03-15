var button = document.getElementById("ser_but").addEventListener("click", fun)

function ref(dat){
    var table = document.getElementById("tab");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    cell1.innerHTML = dat[7];
    cell2.innerHTML = dat[0];
    cell3.innerHTML = dat[2];
    cell4.innerHTML = dat[3];
    cell5.innerHTML = dat[6];

}

function fun(event) {
    event.preventDefault();
    var search = document.getElementById('search');
    var data = {
        type : "all",
        input: search.value
    }
    var data2;
    // alert(data["input"]);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:3000/get_document');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        // Handle the response data
        data2 = JSON.parse(xhr.responseText);
        ref(data2);
        
    }
    else if (xhr.readyState === 4 && xhr.status !== 200) {
        // Handle any errors
        alert('cant find book' + xhr.status);
    }
    };

    // Send the updated JSON data in the request body
    xhr.send(JSON.stringify(data));
    console.log(data2);
}