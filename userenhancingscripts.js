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

