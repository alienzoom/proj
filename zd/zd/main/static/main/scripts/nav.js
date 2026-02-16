hiddenNavBtn.addEventListener("click", (e) => {
    e.preventDefault();

    mobileNavList.classList.toggle("visible");

    if (mobileNavList.classList.contains("visible")) {
        mobileNavList.style.display = "grid"
    } else {
        mobileNavList.style.display = "none"
    }
});

const forOrganizations = document.querySelector(".org-btn");
const forPersons = document.querySelector(".pers-btn");
const navLinks = document.querySelectorAll(".nav-link");

const orgsArr = ["Организации", "ОНОИО", "Проекты", "Обучение и карьера", "Новости", "Форум"];
const persArr = ["Лидеры цифровой информации", "Академия иноваторов", "Новатор Москвы", "Обучение и карьера"];


const chooseFor = (option) => {
    option.addEventListener("click", e => {
        e.preventDefault();
            if (option === forPersons) {
                navLinks.forEach((el, i) => {
                    const link = el.querySelector("h1")
                    link.textContent = persArr[i];
                })
            } else {
                navLinks.forEach((el, i) => {
                    const link = el.querySelector("h1")
                    link.textContent = orgsArr[i];
                })
            }
    })
}

chooseFor(forPersons);
chooseFor(forOrganizations);