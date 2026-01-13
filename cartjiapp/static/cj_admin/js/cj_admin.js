

document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("cjToggle");
    const sidebar = document.querySelector(".cj-sidebar");
    
    if (!toggleBtn || !sidebar) {
        console.error("CJ Admin toggle: elements not found");
        return;
    }

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("open");
    });
});


function addImageForm() {
    const formset = document.getElementById("image-formset");
    const totalFormsInput = document.getElementById("id_form-TOTAL_FORMS");

    let totalForms = parseInt(totalFormsInput.value);
    let newForm = formset.children[0].cloneNode(true);

    // Update input names & ids
    newForm.innerHTML = newForm.innerHTML.replaceAll(
    /form-(\d+)-/g,
    `form-${totalForms}-`
    );

    // Clear input values
    newForm.querySelectorAll("input, select").forEach(input => {
        input.value = "";
    });

    formset.appendChild(newForm);
    totalFormsInput.value = totalForms + 1;
}



let deleteUrl = null;

document.querySelectorAll(".delete-order").forEach(btn => {
    btn.addEventListener("click", function (e) {
        e.preventDefault();

        // 🚫 If user disabled delete confirmation
        if (localStorage.getItem("disableOrderDelete") === "true") {
            return; // do nothing
        }

        deleteUrl = this.dataset.url;
        document.getElementById("deleteModal").style.display = "flex";
    });
});

document.getElementById("confirmDelete").onclick = function () {
    const dontAsk = document.getElementById("dontAskAgain").checked;

    if (dontAsk) {
        localStorage.setItem("disableOrderDelete", "true");
        document.getElementById("deleteModal").style.display = "none";
        return; // ❌ DO NOT DELETE
    }

    window.location.href = deleteUrl; // ✅ DELETE
};

document.getElementById("cancelDelete").onclick = function () {
    document.getElementById("deleteModal").style.display = "none";
};
