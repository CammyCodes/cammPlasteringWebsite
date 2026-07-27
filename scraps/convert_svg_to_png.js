const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const assetsDir = path.resolve(__dirname, '..', 'assets');
const clientsDir = path.resolve(assetsDir, 'clients');

const filesToConvert = [
  { svg: 'camm-logo.svg', png: 'camm-logo.png', width: 1040, height: 360, dir: assetsDir },
  { svg: 'hero.svg', png: 'hero.jpg', width: 1200, height: 800, dir: assetsDir },
  { svg: 'svc-plastering.svg', png: 'svc-plastering.jpg', width: 800, height: 600, dir: assetsDir },
  { svg: 'svc-drylining.svg', png: 'svc-drylining.jpg', width: 800, height: 600, dir: assetsDir },
  { svg: 'svc-rendering.svg', png: 'svc-rendering.jpg', width: 800, height: 600, dir: assetsDir },
  { svg: 'harron-homes.svg', png: 'harron-homes.png', width: 400, height: 160, dir: clientsDir, bg: '#122e54' },
  { svg: 'avant-homes.svg', png: 'avant-homes.png', width: 400, height: 160, dir: clientsDir, bg: '#ffffff' }
];

filesToConvert.forEach(item => {
  const svgPath = path.join(item.dir, item.svg);
  const outPath = path.join(item.dir, item.png);
  
  const bgStyle = item.bg ? `background: ${item.bg};` : 'background: transparent;';
  const htmlContent = `<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; padding: 20px; ${bgStyle} overflow: hidden; display: flex; align-items: center; justify-content: center; height: 100vh; box-sizing: border-box; }
  img { max-width: 100%; max-height: 100%; object-fit: contain; }
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
  try {
    execSync(cmd);
  } catch (err) {
    console.error(`Error converting ${item.svg}:`, err.message);
  }

  if (fs.existsSync(htmlPath)) fs.unlinkSync(htmlPath);
});

console.log('Client logo conversion finished!');
