/*
 * For more information, refer to the "Javascript API" documentation:
 * https://doc.dataiku.com/dss/latest/api/js/index.html
 */

let fetchButton = document.getElementById('fetch-button');
let clearButton = document.getElementById('clear-button');
let historyButton = document.getElementById('history-button');
let leagueDropdown = document.getElementById('dropdownMenuButton');

fetchButton.addEventListener('click', function(event) {
    $.getJSON(getWebAppBackendUrl('/predictions'), function(data) {
        console.log('Received data from backend', data)
        /* modifying html to show the dataset as a table */
        $('#message').append(data['data'])
    });
    return false;
});

historyButton.addEventListener('click', function(event) {
    $.getJSON(getWebAppBackendUrl('/predictions'), function(data) {
        console.log('Received data from backend', data)
        /* modifying html to show the dataset as a table */
        $('#message').append(data['data'])
    });
    return false;
});

clearButton.addEventListener('click', function(event) {
    $('#message').empty();
    return false;
});