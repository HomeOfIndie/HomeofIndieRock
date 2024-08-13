// taking user back to top of page

const toTop = () => window.scrollTo({top:0, behavior: 'smooth'});


// Go back to previous page

const PreviousPage = () => history.go(-1);

// go to home page

const HomePage = () => window.location.href = 'index.html'

// on form submittion = submitted

function showalert () {

alert('Survey Complete!')
}

function onclickcomplete () {

document.body.innerHTML = 'Form Submitted!'
}

//Create your own Playlist//

function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    if (taskInput.value.trim() !== '') {
        const li = document.createElement('li');
        li.textContent = taskInput.value;
        taskList.appendChild(li);
        taskInput.value = '';
    }
}

function removeTask() {

    taskList.innerHTML = '';
}

function saveList() {
    const list = document.getElementById('taskList').innerHTML;
    let lists = JSON.parse(localStorage.getItem('lists')) || [];
    lists.push(list);
    localStorage.setItem('lists', JSON.stringify(lists));
    redirectToPlaylists();
}

function redirectToPlaylists() {
    window.location.href = 'AllPlaylists.html';
}

document.addEventListener('DOMContentLoaded', (event) => {
    const savedLists = JSON.parse(localStorage.getItem('lists')) || [];
    const savedTaskListContainer = document.getElementById('savedTaskList');
    savedLists.forEach((list, index) => {
        const listElement = document.createElement('div');
        listElement.classList.add('savedTaskList'); // Add a class for styling
        listElement.innerHTML = `<h2>Playlist ${index + 1}</h2><ul>${list}</ul>`;
        savedTaskListContainer.appendChild(listElement);
    });
});

