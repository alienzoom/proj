if (profilePage) {
    const chooseRequestList = document.querySelectorAll('.choose-request-el');
    const yourTeamContainer = document.querySelector('.your-team');
    
    chooseRequestList.forEach((requestElement) => {
        const addButton = requestElement.querySelector('.choose-request-add-btn');
    
        addButton.addEventListener('click', (e) => {
            e.preventDefault();
            
            const detailsBlock = requestElement.querySelector('details');
            let budgetText = 'Сумма не указана';
    
            if (detailsBlock) {
                const budgetSpan = detailsBlock.querySelector('span');
                if (budgetSpan) {
                    budgetText = budgetSpan.textContent.trim(); 
                }
            }
            
            const clonedRequest = requestElement.cloneNode(true);
            
            clonedRequest.querySelector('.choose-request-add-btn')?.remove();
            clonedRequest.querySelector('details')?.remove();
            clonedRequest.querySelector('.separator')?.remove();
    
            
            clonedRequest.classList.remove('choose-request-el');
            clonedRequest.classList.add('added-request-item');
    
            const budgetDisplay = document.createElement('h2');
            budgetDisplay.classList.add('team-budget-display');
            budgetDisplay.innerHTML = `Бюджет: <strong>${budgetText}₽</strong>`;
            budgetDisplay.style.marginTop = '12px'
            
            const removeButton = document.createElement('button');
            removeButton.textContent = 'Удалить';
            removeButton.type = 'button';
            removeButton.classList.add('remove-team-btn');
    
            removeButton.addEventListener('click', function() {
                clonedRequest.remove(); 
            
                addButton.style.border = "2px solid";
                addButton.style.color = "#000";
                addButton.style.background = "#727272";
                
                addButton.disabled = false;
                addButton.textContent = '+';
            });
            
            clonedRequest.appendChild(budgetDisplay);
            clonedRequest.appendChild(removeButton);
    
            yourTeamContainer.appendChild(clonedRequest);
            
            addButton.style.border = "none";
            addButton.style.color = "#0a8a35ff";
            addButton.style.background = "none";
            
            addButton.disabled = true;
            addButton.textContent = '✓ В команде';
        });
    });
    
    
    /// СОЗДАНИЕ КОМАНДЫ
    const createFinalTeamBtn = document.querySelector('.create-final-team-btn');
    
    createFinalTeamBtn.addEventListener('click', (e) => {
        e.preventDefault();
    
        const teamName = prompt("Введите название вашей новой команды:");
    
        if (!teamName) {
            alert("Создание команды отменено или имя не введено.");
            return;
        }
    
        const addedItems = yourTeamContainer.querySelectorAll('.added-request-item');
    
        if (addedItems.length === 0) {
            alert("Не выбрано ни одной заявки для формирования команды.");
            return;
        }
    
        const finalTeamBlock = document.createElement('div');
        finalTeamBlock.classList.add('final-team-container');
        
        const header = document.createElement('h1');
        header.textContent = `Команда: ${teamName}`;
        finalTeamBlock.appendChild(header);
    
        const membersList = document.createElement('div');
        membersList.classList.add('team-members-section');
    
        addedItems.forEach(item => {
            const memberCard = item.cloneNode(true);
            
            memberCard.querySelector('.remove-team-btn')?.remove();
            
            memberCard.classList.remove('added-request-item');
            memberCard.classList.add('final-team-member-card');
            
            membersList.appendChild(memberCard);
        });
    
        const finalTeamHTML = finalTeamBlock.outerHTML;
    
        sessionStorage.setItem('newTeamData', finalTeamHTML);
        
        alert(`Команда "${teamName}" успешно сформирована.`);
    
        location.href = '/profile/';
    });
}