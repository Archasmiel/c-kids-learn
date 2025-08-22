document.addEventListener("DOMContentLoaded", function() {

    /* -------------------------------
       Translations
    -------------------------------- */
    const translations = {
        passwordError: "{{ _('Password must contain only') }} {{ _('Latin letters (a-z, A-Z), digits (0-9), and special characters') }} (!@#$%^&*).",
        passwordLengthError: "{{ _('Password must be at least') }} 8 {{ _('characters long.') }}",
        passwordUppercaseError: "{{ _('Password must contain at least one uppercase Latin letter.') }}",
        passwordNumberError: "{{ _('Password must contain at least one number.') }}",
        passwordSpecialError: "{{ _('Password must contain at least one special character.') }} (!@#$%^&*)",
        confirmPasswordError: "{{ _('Passwords do not match.') }}",
        emailError: "{{ _('Invalid email address.') }} {{ _('Please use only Latin letters, digits, and valid special characters.') }}"
    };

    /* -------------------------------
       Doctor Specialty Handling
    -------------------------------- */
    const specialtyGroup = document.getElementById("specialty_group");
    const otherSpecialtyGroup = document.getElementById("other_specialty_group");
    const specialtySelect = document.getElementById("specialty_select");

    // Fix initial state on page load (browser back button compatibility)
    const isDoctorChecked = document.querySelector('input[name="is_doctor"]:checked');
    if (specialtyGroup) {
        specialtyGroup.style.display = (isDoctorChecked && isDoctorChecked.value === "yes") ? "block" : "none";
    }
    if (otherSpecialtyGroup && specialtySelect) {
        otherSpecialtyGroup.style.display = (specialtySelect.value === "Other") ? "block" : "none";
    }

    // Listen to doctor yes/no radio buttons
    document.querySelectorAll('input[name="is_doctor"]').forEach(function(radio) {
        radio.addEventListener("change", function() {
            if (!specialtyGroup || !otherSpecialtyGroup) return;
            if (this.value === "yes" && this.checked) {
                specialtyGroup.style.display = "block";
            } else {
                specialtyGroup.style.display = "none";
                otherSpecialtyGroup.style.display = "none";
            }
        });
    });

    // Listen to specialty dropdown for "Other"
    if (specialtySelect) {
        specialtySelect.addEventListener("change", function() {
            if (!otherSpecialtyGroup) return;
            otherSpecialtyGroup.style.display = (this.value === "Other") ? "block" : "none";
        });
    }

    /* -------------------------------
       Toggle Password Field Visibility
    -------------------------------- */
    const togglePassword = document.getElementById("togglePassword");
    const passwordField = document.getElementById("passwordField");

    if (togglePassword && passwordField) {
        const passwordIcon = togglePassword.querySelector("i");
        togglePassword.addEventListener("click", function() {
            const isPassword = passwordField.getAttribute("type") === "password";
            passwordField.setAttribute("type", isPassword ? "text" : "password");
            if (passwordIcon) {
                passwordIcon.classList.toggle("bi-eye");
                passwordIcon.classList.toggle("bi-eye-slash");
            }
        });
    }

    /* -------------------------------
       Toggle Confirm Password Field
    -------------------------------- */
    const toggleConfirm = document.getElementById("toggleConfirmPassword");
    const confirmField = document.getElementById("confirmPasswordField");

    if (toggleConfirm && confirmField) {
        const confirmIcon = toggleConfirm.querySelector("i");
        toggleConfirm.addEventListener("click", function() {
            const isPassword = confirmField.getAttribute("type") === "password";
            confirmField.setAttribute("type", isPassword ? "text" : "password");
            if (confirmIcon) {
                confirmIcon.classList.toggle("bi-eye");
                confirmIcon.classList.toggle("bi-eye-slash");
            }
        });
    }

    /* -------------------------------
       Safety Logging for Debug
    -------------------------------- */
    if (!specialtyGroup || !otherSpecialtyGroup || !specialtySelect) {
        console.log("⚠️ Register page: Some specialty elements not found. Check your template IDs.");
    }
    if (!togglePassword || !passwordField) {
        console.log("⚠️ Register page: Toggle for password field missing.");
    }
    if (!toggleConfirm || !confirmField) {
        console.log("⚠️ Register page: Toggle for confirm password field missing.");
    }
});
