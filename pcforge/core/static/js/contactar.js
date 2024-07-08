document.addEventListener("DOMContentLoaded", function () {
    const privacyButton = document.getElementById("privac");
    const privacyCheckbox = privacyButton.querySelector(".translate-x-0");

    privacyButton.addEventListener("click", function () {
        const isChecked = privacyButton.getAttribute("aria-checked") === "true";

        if (isChecked) {
            privacyButton.setAttribute("aria-checked", "false");
            privacyCheckbox.classList.remove("translate-x-3.5");
            privacyButton.classList.remove("bg-indigo-600");
            privacyButton.classList.add("bg-gray-200");
        } else {
            privacyButton.setAttribute("aria-checked", "true");
            privacyCheckbox.classList.add("translate-x-3.5");
            privacyButton.classList.remove("bg-gray-200");
            privacyButton.classList.add("bg-indigo-600");
        }
    });
});

