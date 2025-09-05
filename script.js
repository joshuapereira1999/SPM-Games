// Educational Learning Platform JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Get button elements
    const ngoolgabBtn = document.getElementById('ngoolgab-btn');
    const miljibBtn = document.getElementById('miljib-btn');
    
    // Add click event listeners with visual feedback only
    ngoolgabBtn.addEventListener('click', function() {
        // Add visual feedback
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
    });
    
    miljibBtn.addEventListener('click', function() {
        // Add visual feedback
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
    });
    
    
    // Add subtle animations to buttons on page load
    setTimeout(() => {
        ngoolgabBtn.style.opacity = '0';
        miljibBtn.style.opacity = '0';
        
        ngoolgabBtn.style.transition = 'opacity 0.6s ease';
        miljibBtn.style.transition = 'opacity 0.6s ease';
        
        setTimeout(() => {
            ngoolgabBtn.style.opacity = '1';
        }, 200);
        
        setTimeout(() => {
            miljibBtn.style.opacity = '1';
        }, 400);
    }, 100);
    
});
