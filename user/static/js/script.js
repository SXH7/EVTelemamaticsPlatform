const modal = document.querySelector('#modal');
const openModel = document.querySelector('.open-modal');
const closeModal = document.querySelector('.close-modal');
const submit = document.querySelector('.submit')

openModel.addEventListener('click', () => {
    modal.showModal();
})

closeModal.addEventListener('click', () => {
    modal.close();
})

submit.addEventListener('click', () => {
    modal.close();
})