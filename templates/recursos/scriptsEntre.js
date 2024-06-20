document.addEventListener('DOMContentLoaded', function() {

    const toggleFormsBtn = document.getElementById('toggleFormsBtn');
    const formAgregarEntrevistador = document.getElementById('formAgregarEntrevistador');
    const formAgregarEntrevista = document.getElementById('formAgregarEntrevista');
    let formsVisible = false;

    toggleFormsBtn.addEventListener('click', function() {
        formsVisible = !formsVisible;

        if (formsVisible) {
            formAgregarEntrevistador.style.display = 'block';
            formAgregarEntrevista.style.display = 'block';
            toggleFormsBtn.textContent = 'Ocultar Formularios de ingreso';
        } else {
            formAgregarEntrevistador.style.display = 'none';
            formAgregarEntrevista.style.display = 'none';
            toggleFormsBtn.textContent = 'Mostrar Formularios de ingreso';
        }
    });

    const toggleFormsBtnElimi = document.getElementById('toggleFormsBtnElimi');
    const formEliminarEntrevistador = document.getElementById('formEliminarEntrevistador');
    const formEliminarEntrevista = document.getElementById('formEliminarEntrevista');
    let formsVisibleEli = false;

    toggleFormsBtnElimi.addEventListener('click', function() {
        formsVisibleEli = !formsVisibleEli;

        if (formsVisibleEli) {
            formEliminarEntrevistador.style.display = 'block';
            formEliminarEntrevista.style.display = 'block';
            toggleFormsBtnElimi.textContent = 'Ocultar Formularios para eliminar';
        } else {
            formEliminarEntrevistador.style.display = 'none';
            formEliminarEntrevista.style.display = 'none';
            toggleFormsBtnElimi.textContent = 'Mostrar Formularios para eliminar';
        }
    });

    const toggleFormsBtnActua = document.getElementById('toggleFormsBtnActua');
    const formActualizarEntrevistador = document.getElementById('formActualizarEntrevistador');
    const formActualizarEntrevista = document.getElementById('formActualizarEntrevista');
    let formsVisibleActu = false;

    toggleFormsBtnActua.addEventListener('click', function() {
        formsVisibleActu = !formsVisibleActu;

        if (formsVisibleActu) {
            formActualizarEntrevistador.style.display = 'block';
            formActualizarEntrevista.style.display = 'block';
            toggleFormsBtnActua.textContent = 'Ocultar Formularios para eliminar';
        } else {
            formActualizarEntrevistador.style.display = 'none';
            formActualizarEntrevista.style.display = 'none';
            toggleFormsBtnActua.textContent = 'Mostrar Formularios para eliminar';
        }
    });

    $('#entrevistadoresTable').DataTable({
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