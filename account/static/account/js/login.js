document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('makeupLoginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            const usernameInput = document.getElementById('username').value.trim();
            const passwordInput = document.getElementById('password').value.trim();

            if (usernameInput === '' || passwordInput === '') {
                event.preventDefault();
                alert('يرجى إدخال اسم المستخدم وكلمة المرور للإكمال!');
            }
        });
    }
});