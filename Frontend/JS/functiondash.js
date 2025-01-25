document.addEventListener('DOMContentLoaded', function() {
    // Función para crear tarjetas de ejemplo en las columnas vacías
    function createSampleCards() {
        const inProgress = document.getElementById('in-progress');
        const completed = document.getElementById('completed');

        // Crear tarjetas de ejemplo para "En curso"
        for (let i = 0; i < 2; i++) {
            const card = document.createElement('div');
            card.className = 'task-card';
            card.innerHTML = `
                <div class="task-tags">
                    <span class="tag priority-medium">Media</span>
                    <span class="tag status-pending">En curso</span>
                </div>
                <h3>Tarea en progreso ${i + 1}</h3>
                <div class="task-meta">
                    <div class="user">
                        <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'%3E%3Ccircle cx='12' cy='8' r='5'/%3E%3Cpath d='M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2'/%3E%3C/svg%3E" alt="Usuario">
                    </div>
                    <span class="date">18 - 22 ene</span>
                </div>
            `;
            inProgress.appendChild(card);
        }

        // Crear tarjetas de ejemplo para "Trabajo terminado"
        for (let i = 0; i < 2; i++) {
            const card = document.createElement('div');
            card.className = 'task-card';
            card.innerHTML = `
                <div class="task-tags">
                    <span class="tag priority-low">Baja</span>
                    <span class="tag status-pending">Completado</span>
                </div>
                <h3>Tarea completada ${i + 1}</h3>
                <div class="task-meta">
                    <div class="user">
                        <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'%3E%3Ccircle cx='12' cy='8' r='5'/%3E%3Cpath d='M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2'/%3E%3C/svg%3E" alt="Usuario">
                    </div>
                    <span class="date">15 - 17 ene</span>
                </div>
            `;
            completed.appendChild(card);
        }
    }

    // Implementar funcionalidad de búsqueda
    const searchInput = document.querySelector('.search-container input');
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.task-card');

        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
    createSampleCards();
});


