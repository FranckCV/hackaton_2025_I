document.addEventListener("DOMContentLoaded", function () {
  const table = document.querySelector(".table_listado");
  const headers = table.querySelectorAll("thead th");
  let sortDirection = {}; // Para saber en qué orden está cada columna

  // Guardamos los textos originales de cada header
  const originalTexts = [];

  headers.forEach((header, index) => {
    if (!header.classList.contains("opciones_column")) {
      const content = header.querySelector('.th_content');
      const originalText = content.querySelector('p').textContent;
      originalTexts[index] = originalText;

      header.addEventListener("click", () => {
        const tbody = table.querySelector("tbody");
        const rows = Array.from(tbody.querySelectorAll("tr"));

        const currentDirection = sortDirection[index] || 'desc';
        const newDirection = currentDirection === 'asc' ? 'desc' : 'asc';
        sortDirection = {};
        sortDirection[index] = newDirection;

        rows.sort((rowA, rowB) => {
          const cellA = rowA.cells[index].innerText.trim();
          const cellB = rowB.cells[index].innerText.trim();
          const isNumeric = !isNaN(cellA) && !isNaN(cellB);

          if (isNumeric) {
            return newDirection === 'asc'
              ? parseFloat(cellA) - parseFloat(cellB)
              : parseFloat(cellB) - parseFloat(cellA);
          } else {
            return newDirection === 'asc'
              ? cellA.localeCompare(cellB)
              : cellB.localeCompare(cellA);
          }
        });

        tbody.innerHTML = '';
        rows.forEach(row => tbody.appendChild(row));

        // Limpiar íconos en todos los headers usando el texto original
        headers.forEach((h, i) => {
          if (!h.classList.contains("opciones_column")) {
            const cont = h.querySelector('.th_content');
            cont.innerHTML = `<p>${originalTexts[i]}</p>`;
          }
        });

        // Agregar ícono en el header actual
        const directionIcon = newDirection === 'asc' ? 'down' : 'up';
        content.innerHTML = `<p>${originalText}</p> <i class="fa-solid fa-caret-${directionIcon}"></i>`;
      });
    }
  });
});
