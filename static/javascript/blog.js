const leftBtn = document.getElementById('leftBtn');
const rightBtn = document.getElementById('rightBtn');
let currentSet = 0;

// Update the blog posts displayed
function updateBlogs() {
    const blogPosts = document.querySelectorAll('.blog-post');
    blogPosts.forEach((post, index) => {
        post.style.display = (index >= currentSet * 3 && index < (currentSet + 1) * 3) ? 'block' : 'none';
    });
}

// Show the next 3 blogs
rightBtn.addEventListener('click', () => {
    if ((currentSet + 1) * 3 < document.querySelectorAll('.blog-post').length) {
        currentSet++;
        updateBlogs();
    }
});

// Show the previous 3 blogs
leftBtn.addEventListener('click', () => {
    if (currentSet > 0) {
        currentSet--;
        updateBlogs();
    }
});

// Initial load
updateBlogs();
