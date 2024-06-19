document.addEventListener('DOMContentLoaded', function() {
    const toggleFormsBtn = document.getElementById('toggleFormsBtn');
    const formAgregarCandidato = document.getElementById('formAgregarCandidato');
    const formAgregarHabilidad = document.getElementById('formAgregarHabilidad');
    let formsVisible = false;

    toggleFormsBtn.addEventListener('click', function() {
        formsVisible = !formsVisible;

        if (formsVisible) {
            formAgregarCandidato.style.display = 'block';
            formAgregarHabilidad.style.display = 'block';
            toggleFormsBtn.textContent = 'Ocultar Formularios de ingreso';
        } else {
            formAgregarCandidato.style.display = 'none';
            formAgregarHabilidad.style.display = 'none';
            toggleFormsBtn.textContent = 'Mostrar Formularios de ingreso';
        }
    });

    const toggleFormsBtnE = document.getElementById('toggleFormsBtnE');
    const formEliminarCandidato = document.getElementById('formEliminarCandidato');
    const formEliminarHabilidad = document.getElementById('formEliminarHabilidad');
    let formsVisibleE = false;

    toggleFormsBtnE.addEventListener('click', function() {
        formsVisibleE = !formsVisibleE;

        if (formsVisibleE) {
            formEliminarCandidato.style.display = 'block';
            formEliminarHabilidad.style.display = 'block';
            toggleFormsBtnE.textContent = 'Ocultar Formularios de eliminacion';
        } else {
            formEliminarCandidato.style.display = 'none';
            formEliminarHabilidad.style.display = 'none';
            toggleFormsBtnE.textContent = 'Mostrar Formularios de eliminacion';
        }
    });


    const addExperienceButton = document.getElementById('addExperience');
            const experienceContainer = document.getElementById('experienciaLaboralContainer');
            
            let experienceCount = 1; // Contador para asignar IDs únicos
            addExperienceButton.addEventListener('click', function() {
                const newExperience = document.createElement('div');
                newExperience.classList.add('experience-item');
                newExperience.innerHTML = `
                    <h3>Experiencia Laboral ${experienceCount}</h3>
                    <div class="mb-3">
                        <label for="puesto_${experienceCount}" class="form-label">Puesto</label>
                        <input type="text" class="form-control" name="puesto[]" required>
                    </div>
                    <div class="mb-3">
                        <label for="empresa_${experienceCount}" class="form-label">Empresa</label>
                        <input type="text" class="form-control" name="empresa[]" required>
                    </div>
                    <div class="mb-3">
                        <label for="anio_experiencia_${experienceCount}" class="form-label">Años de Experiencia</label>
                        <input type="number" class="form-control" name="anio_experiencia[]" required>
                    </div>
                    <button type="button" class="btn btn-danger" onclick="removeExperience(this)">Eliminar</button>
                `;
                experienceContainer.appendChild(newExperience);
                experienceCount++;
            });







            
            


});

