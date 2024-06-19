//FUNCIONES PARA EMPRESA Y OFERTA DE TRABAJO
const toggleFormsBtnEMPRE = document.getElementById('toggleFormsBtnEMPRE');
const formAgregarEmpresa = document.getElementById('formAgregarEmpresa');
const formAgregarOferta = document.getElementById('formAgregarOferta');
let formsVisibleEMPRE = false;

toggleFormsBtnEMPRE.addEventListener('click', function() {
    formsVisibleEMPRE = !formsVisibleEMPRE;

    if (formsVisibleEMPRE) {
        formAgregarEmpresa.style.display = 'block';
        formAgregarOferta.style.display = 'block';
        toggleFormsBtnEMPRE.textContent = 'Ocultar Formularios para Agregar';
    } else {
        formAgregarEmpresa.style.display = 'none';
        formAgregarOferta.style.display = 'none';
        toggleFormsBtnEMPRE.textContent = 'Mostrar Formularios para Agregar';
    }
});

const toggleFormsBtnEli = document.getElementById('toggleFormsBtnEli');
const formEliminarEmpresa = document.getElementById('formEliminarEmpresa');
const formEliminarOferta = document.getElementById('formEliminarOferta');
let formsVisible = false;

toggleFormsBtnEli.addEventListener('click', function() {
    formsVisible = !formsVisible;

    if (formsVisible) {
        formEliminarEmpresa.style.display = 'block';
        formEliminarOferta.style.display = 'block';
        toggleFormsBtnEli.textContent = 'Ocultar Formularios para Agregar';
    } else {
        formEliminarEmpresa.style.display = 'none';
        formEliminarOferta.style.display = 'none';
        toggleFormsBtnEli.textContent = 'Mostrar Formularios para Agregar';
    }
});
