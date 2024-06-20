document.addEventListener('DOMContentLoaded', function() {
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
        toggleFormsBtnEli.textContent = 'Mostrar Formularios para Eliminar';
    }
});

const toggleFormsBtnActu = document.getElementById('toggleFormsBtnActu');
const formActualizarEmpresa = document.getElementById('formActualizarEmpresa');
const formActualizarOferta = document.getElementById('formActualizarOferta');
let formsVisibleAc = false;

toggleFormsBtnActu.addEventListener('click', function() {
    formsVisibleAc = !formsVisibleAc;

    if (formsVisibleAc) {
        formActualizarEmpresa.style.display = 'block';
        formActualizarOferta.style.display = 'block';
        toggleFormsBtnEli.textContent = 'Ocultar Formularios para Agregar';
    } else {
        formActualizarEmpresa.style.display = 'none';
        formActualizarOferta.style.display = 'none';
        toggleFormsBtnEli.textContent = 'Mostrar Formularios para Eliminar';
    }
});

$('#empresasTable').DataTable({
    "paging": true,
    "searching": true,
    "pageLength": 5,
    "lengthMenu": [5, 10, 20],
    "language": {
        "lengthMenu": "Mostrar _MENU_ registros por página",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "search": "Buscar:",
    }
});



});