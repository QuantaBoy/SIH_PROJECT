// Toggle between Signup and Login pages with smooth transitions
document.addEventListener('DOMContentLoaded', function() {
    const signupPage = document.querySelector('.signup-page');
    const loginPage = document.querySelector('.login-page');
    const toggleLoginButton = document.querySelector('.toggle-login-button');
    const toggleSignupButton = document.querySelector('.toggle-signup-button');

    function showLoginPage() {
        if (signupPage && loginPage) {
            // Hide signup page with transition
            signupPage.classList.add('hidden');
            
            // Show login page with transition
            setTimeout(() => {
                loginPage.classList.add('active');
                document.title = 'Login - miru';
            }, 50);
        }
    }

    function showSignupPage() {
        if (signupPage && loginPage) {
            // Hide login page with transition
            loginPage.classList.remove('active');
            
            // Show signup page with transition
            setTimeout(() => {
                signupPage.classList.remove('hidden');
                document.title = 'Sign Up - miru';
            }, 50);
        }
    }

    if (toggleLoginButton) {
        toggleLoginButton.addEventListener('click', function(e) {
            e.preventDefault();
            showLoginPage();
        });
    }

    if (toggleSignupButton) {
        toggleSignupButton.addEventListener('click', function(e) {
            e.preventDefault();
            showSignupPage();
        });
    }
});

