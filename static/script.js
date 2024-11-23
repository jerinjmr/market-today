document.addEventListener('DOMContentLoaded', function() {
    const aiContent = document.getElementById('ai-content');
    
    fetch('/get-ai-insight')
        .then(response => {
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            
            // Remove loading message
            aiContent.innerHTML = '';
            
            function readStream() {
                reader.read().then(({done, value}) => {
                    if (done) {
                        return;
                    }
                    
                    const text = decoder.decode(value);
                    // Split the text into characters and add them one by one
                    const chars = text.split('');
                    
                    let i = 0;
                    function addChar() {
                        if (i < chars.length) {
                            aiContent.innerHTML += chars[i];
                            i++;
                            // Adjust this timeout value to control the speed (currently 50ms per character)
                            setTimeout(addChar, 30);
                        } else {
                            readStream();
                        }
                    }
                    
                    addChar();
                });
            }
            
            readStream();
        })
        .catch(error => {
            aiContent.innerHTML = `<div class="error">Error loading AI insights: ${error.message}</div>`;
        });
});
