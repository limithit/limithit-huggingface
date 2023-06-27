const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const imageUpload = document.getElementById('imageUpload');

let img = new Image();
let offsetX, offsetY, startX, startY, scale = 1;
let dragging = false;

// Resize the canvas to fill the parent element
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
//   canvas.width = 1024;
//   canvas.height = 1024;
  drawImage();
}

// Draw the image on the canvas
function drawImage() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, offsetX, offsetY, img.width * scale, img.height * scale);
}

// Handle image upload
imageUpload.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    img.src = e.target.result;
    img.onload = () => {
      offsetX = (canvas.width - img.width) / 2;
      offsetY = (canvas.height - img.height) / 2;
      drawImage();
    };
  };
  reader.readAsDataURL(file);
});

// Handle mouse events
canvas.addEventListener('mousedown', (event) => {
  startX = event.clientX - offsetX;
  startY = event.clientY - offsetY;
  dragging = true;
});

canvas.addEventListener('mousemove', (event) => {
  if (dragging) {
    offsetX = event.clientX - startX;
    offsetY = event.clientY - startY;
    drawImage();
  }
});

canvas.addEventListener('mouseup', () => {
  dragging = false;
});

canvas.addEventListener('wheel', (event) => {
  event.preventDefault();
  const delta = event.deltaY < 0 ? 1.1 : 0.9;
  scale *= delta;
  drawImage();
});

// Initialize the canvas
resizeCanvas();
window.addEventListener('resize', resizeCanvas);