const requirementsList = document.querySelector('.requirements-list');
const requirementsElement = document.querySelector('.requirments-el');
const addRequirementButton = document.querySelector('.add-requirement-btn');

const addNewRequirement = () => {
    const requirementBlock = document.createElement('div');
    requirementBlock.innerHTML = `
        <div class="requirements-el">
            <label>
                Название ресурса:<br>
                <input type="text" class="requirement-name" placeholder="Введите название">
                </label>
                
                <label>
                Цена ресурса:<br>
                <input type="number" class="requirement-price" placeholder="Введите цену">
            </label>
        </div>
    `; 
    
    requirementsList.appendChild(requirementBlock);
}

addRequirementButton.addEventListener('click', addNewRequirement)