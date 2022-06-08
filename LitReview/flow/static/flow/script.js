const requestButton = document.getElementById('button-request');
const createReviewButton = document.getElementById('button-create-review');

requestButton.addEventListener('click', () => {
	location.href = "../reviews/request";
});

createReviewButton.addEventListener('click', () => {
	location.href = "../reviews/create";
});
