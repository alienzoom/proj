const jsonData = JSON.parse('{{ application_json|safe }}'); 
console.log(jsonData + 1);
console.log('test');

const filterInputJs = document.getElementById('filter-skills-js');
    const applyFilterBtnJs = document.getElementById('apply-filter-js');
    const resetFilterBtnJs = document.getElementById('reset-filter-js');
    const applicationsListContainerJs = document.querySelector('.profile-second-request-list');

    let allApplicationsData = []; 
    let currentRenderedApplications = [];

    function getAllApplicationsFromDOM() {
        const applicationElements = applicationsListContainerJs.querySelectorAll('.profile-second-request-el');
        const applicationsData = [];

        applicationElements.forEach(el => {
            const idElement = el.querySelector('h3');
            const id = idElement ? idElement.textContent.replace('Заявка № ', '').trim() : 'N/A';
            
            let organizationName = '';
            let solutionName = '';
            const skillListElement = el.querySelector('.skillList');
            const skillListText = skillListElement ? skillListElement.textContent.trim() : '';

            const nonSkillParagraphs = Array.from(el.querySelectorAll('p')).filter(p => !p.classList.contains('skillList'));
            
            if (nonSkillParagraphs.length > 0) {
                organizationName = nonSkillParagraphs[0].textContent.trim();
            }
            if (nonSkillParagraphs.length > 1) {
                solutionName = nonSkillParagraphs[1].textContent.trim();
            }

            applicationsData.push({
                id: id,
                organization_name: organizationName,
                solution_name: solutionName,
                skill_list_text: skillListText 
            });
        });
        return applicationsData;
    }

    function renderApplicationsJs(applicationsToRender) {
        if (!applicationsListContainerJs) {
            console.error('Контейнер ".profile-second-request-list" не найден!');
            return;
        }
        applicationsListContainerJs.innerHTML = '';

        if (applicationsToRender.length === 0) {
            applicationsListContainerJs.innerHTML = '<p>Нет заявок, соответствующих вашим критериям.</p>';
            return;
        }

        applicationsToRender.forEach(app => {
            const appElement = document.createElement('div');
            appElement.classList.add('profile-second-request-el');
            
            const skillsString = app.skill_list_text;

            appElement.innerHTML = `
                <h3>Заявка № ${app.id}</h3>
                <p>${app.organization_name}</p>
                <p>${app.solution_name}</p>
                <p class="skillList">${skillsString}</p>
            `;
            applicationsListContainerJs.appendChild(appElement);
        });
        currentRenderedApplications = applicationsToRender; 
    }

    function parseSkillsString(skillsString) {
        if (!skillsString || typeof skillsString !== 'string') {
            return [];
        }
        return skillsString.split(/,\s*/)
                           .map(s => s.trim().toLowerCase())
                           .filter(s => s);
    }

    function applyFilterJs() {
        const filterText = filterInputJs.value.trim().toLowerCase();
        
        const requiredSkills = parseSkillsString(filterText);

        let filteredApplications = [];

        if (requiredSkills.length === 0) {
            filteredApplications = allApplicationsData;
        } else {
            filteredApplications = allApplicationsData.filter(app => {
                const appSkills = parseSkillsString(app.skill_list_text);
                return requiredSkills.some(reqSkill => appSkills.includes(reqSkill));
            });
        }
        renderApplicationsJs(filteredApplications);
    }

    if (applyFilterBtnJs) {
        applyFilterBtnJs.addEventListener('click', applyFilterJs);
    }
    if (resetFilterBtnJs) {
        resetFilterBtnJs.addEventListener('click', () => {
            filterInputJs.value = '';
            applyFilterJs();
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        if (applicationsListContainerJs) {
            allApplicationsData = getAllApplicationsFromDOM();
            renderApplicationsJs(allApplicationsData);
        } else {
            console.error("Контейнер '.profile-second-request-list' не найден.");
        }
    });