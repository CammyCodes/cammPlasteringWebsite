const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const assetsDir = path.resolve(__dirname, '..', 'assets');

const filesToConvert = [
  { svg: 'camm-logo.svg', png: 'camm-logo.png', width: 1040, height: 360 },
  { svg: 'hero.svg', png: 'hero.jpg', width: 1200, height: 800 },
  { svg: 'svc-plastering.svg', png: 'svc-plastering.jpg', width: 800, height: 600 },
  { svg: 'svc-drylining.svg', png: 'svc-drylining.jpg', width: 800, height: 600 },
  { svg: 'svc-rendering.svg', png: 'svc-rendering.jpg', width: 800, height: 600 },
];

filesToConvert.forEach(item => {
  const svgPath = path.join(assetsDir, item.svg);
  const outPath = path.join(assetsDir, item.png);
  
  // Create a minimal HTML wrapper for high-dpi rendering
  const htmlContent = `<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; padding: 0; background: transparent; overflow: hidden; }
  img { width: ${item.width}px; height: ${item.height}px; display: block; }
</style>
</head>
<body>
  <img src="file:///${svgPath.replace(/\\/g, '/')}">
</body>
</html>`;

  const htmlPath = path.join(__dirname, `temp_${item.svg}.html`);
  fs.writeFileSync(htmlPath, htmlContent);

  const cmd = `"${edgePath}" --headless --disable-gpu --screenshot="${outPath}" --window-size=${item.width},${item.height} "file:///${htmlPath.replace(/\\/g, '/')}"`;
  console.log(`Converting ${item.svg} to ${item.png}...`);
  execSync(cmd);

  fs.unlinkSync(htmlPath);
});

console.log('Conversion finished successfully!');
