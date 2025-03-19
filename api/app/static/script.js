// Add drag and drop functionality for upload area
const uploadArea = document.getElementById('uploadArea');
        
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    uploadArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    uploadArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    uploadArea.addEventListener(eventName, unhighlight, false);
});

function highlight() {
    uploadArea.classList.add('border-primary');
}

function unhighlight() {
    uploadArea.classList.remove('border-primary');
}

uploadArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    handleFiles(files);
}

function handleFiles(files) {
    if (files.length > 0) {
        const file = files[0];
        document.getElementById('imageUpload').files = files;
        updateFilePreview(file);
    }
}

// Get model info when page loads
window.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/info');
        const data = await response.json();
        document.getElementById('modelInfo').innerHTML = `
            <div class="col-md-6">
                <p class="mb-1"><strong>Model Version:</strong> <span class="badge bg-primary">${data.model_version}</span></p>
            </div>
            <div class="col-md-6">
                <p class="mb-1"><strong>Description:</strong> ${data.description}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error fetching model info:', error);
        document.getElementById('modelInfo').innerHTML = `
            <div class="col-12">
                <div class="alert alert-warning" role="alert">
                    <i class="bi bi-exclamation-triangle me-2"></i>
                    Unable to load model information
                </div>
            </div>
        `;
    }
});

// Handle file selection
document.getElementById('imageUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        updateFilePreview(file);
    }
});

function updateFilePreview(file) {
    document.getElementById('fileName').textContent = file.name;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = function(e) {
        const preview = document.getElementById('imagePreview');
        preview.src = e.target.result;
        document.getElementById('previewSection').style.display = 'block';
    };
    reader.readAsDataURL(file);
}

// Handle form submission
document.getElementById('submitBtn').addEventListener('click', async function() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image first');
        return;
    }

    // Show loading indicator
    document.getElementById('loadingIndicator').style.display = 'block';
    document.getElementById('noResultsPlaceholder').style.display = 'none';
    document.getElementById('resultsContent').style.display = 'none';
    
    // Create form data
    const formData = new FormData();
    formData.append('image', file);
    
    try {
        // Send request to the API
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // Get the response as blob
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        
        // Display result
        document.getElementById('resultImage').src = imageUrl;
        document.getElementById('resultsContent').style.display = 'block';
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('resultsContent').innerHTML = `
            <div class="alert alert-danger" role="alert">
                <i class="bi bi-exclamation-circle-fill me-2"></i>
                An error occurred while processing the image
            </div>
        `;
        document.getElementById('resultsContent').style.display = 'block';
    } finally {
        // Hide loading indicator
        document.getElementById('loadingIndicator').style.display = 'none';
    }
});