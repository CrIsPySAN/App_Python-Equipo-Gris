function showAlert(message, category) {
    const alertDiv = document.createElement("div")
    alertDiv.className = `alert alert-${category}`
    alertDiv.textContent = message

    document.body.appendChild(alertDiv)

    // Forzar un reflow para que la transición funcione
    alertDiv.offsetHeight

    // Mostrar la alerta
    alertDiv.classList.add("alert-show")

    setTimeout(() => {
        alertDiv.classList.remove("alert-show")
        setTimeout(() => {
            alertDiv.remove()
        }, 300) // Esperar a que termine la transición antes de remover el elemento
    }, 5000)
}

document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert")
    alerts.forEach((alert) => {
        const message = alert.textContent
        const category = alert.classList[1].split("-")[1]
        showAlert(message, category)
        alert.remove()
    })
})

