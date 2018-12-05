const listFriendsApi = 'http://127.0.0.1:8000/api/list/';

function getJson(apiUrl) {
    let HttpReq = new XMLHttpRequest(); // a new request
    HttpReq.open("GET", apiUrl, false);
    HttpReq.send(null);
    return JSON.parse(HttpReq.responseText);
};

const Friend = (friend) =>
    (
        `<div>
            <a class="list-group-item list-group-item-action" href="https://vk.com/id${friend.id}" target="_blank">
                <img class="rounded-circle" src="${friend.photo_50}" alt="${friend.first_name} ${friend.last_name}">
                ${friend.first_name} ${friend.last_name}
            </a>
        </div>`
    )

const getFriendsList = res => {
    let friends = res.data.results.map(Friend).join('');
    let friendsHtml = document.getElementById('friends');
    friendsHtml.innerHTML = '';
    friendsHtml.innerHTML += friends;
};

function updateFriends() {
    let jsonData = getJson(listFriendsApi);
    let friends = jsonData.results.map(Friend).join('');

    let friendsHtml = document.getElementById('friends');
    friendsHtml.innerHTML = '';
    friendsHtml.innerHTML += friends;

};

window.onload = function () {
    let buttonFriends = document.getElementById('friendsButton');
    buttonFriends.addEventListener('click', updateFriends);
};
