document.addEventListener("DOMContentLoaded", function() {
    var dropdownBtns = document.querySelectorAll(".dropdown-btn");
    
    dropdownBtns.forEach(function(btn) {
        btn.addEventListener("click", function(event) {
            event.stopPropagation(); 
            var dropdownContent = this.nextElementSibling;
            
            dropdownContent.classList.toggle("show");

            document.querySelectorAll(".dropdown-content").forEach(function(content) {
                if (content !== dropdownContent) {
                    content.classList.remove("show");
                }
            });
        });
    });

    
    window.addEventListener("click", function(event) {
        if (!event.target.matches('.dropdown-btn')) {
            document.querySelectorAll(".dropdown-content").forEach(function(content) {
                if (content.classList.contains('show')) {
                    content.classList.remove('show');
                }
            });
        }
    });
});