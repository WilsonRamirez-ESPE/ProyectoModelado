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


});