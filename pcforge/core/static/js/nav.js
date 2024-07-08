document.addEventListener('DOMContentLoaded', function () {
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.querySelector('[aria-labelledby="user-menu-button"]');

    userMenuButton.addEventListener('click', function () {
      const expanded = userMenuButton.getAttribute('aria-expanded') === 'true' || false;
      userMenuButton.setAttribute('aria-expanded', !expanded);
      userMenu.classList.toggle('hidden');
    });

    userMenu.classList.add('hidden');

    const mobileMenuButton = document.querySelector('[aria-controls="mobile-menu"]');
        const mobileMenu = document.getElementById('mobile-menu');
        
        mobileMenuButton.addEventListener('click', function () {
            const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
            mobileMenuButton.setAttribute('aria-expanded', !expanded);
            mobileMenu.classList.toggle('hidden');
        });

        mobileMenu.classList.add('hidden');
  });