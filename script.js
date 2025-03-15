function showSection(sectionId) {
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.add('hidden');
    });
    document.getElementById(sectionId).classList.remove('hidden');
}

function showSubOptions() {
    document.getElementById('sub-options').classList.toggle('hidden');
}
