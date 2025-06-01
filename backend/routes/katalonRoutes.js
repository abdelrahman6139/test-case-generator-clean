const express = require('express');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');

const router = express.Router();

// ✅ المسارات حسب مشروعك
const projectPath = 'C:\\Users\\GIGABYTE\\Katalon Studio\\AutoTestProject\\AutoTestProject.prj';
const testSuitePath = 'Test Suites/MySuite1';
const katalonCliPath = 'C:\\Users\\GIGABYTE\\Katalon_Studio_Engine_Windows_64-10.1.1\\katalonc';

router.post('/execute-katalon', async (req, res) => {
  const katalonCommand = `"${katalonCliPath}" -noSplash -runMode=console -projectPath="${projectPath}" -testSuitePath="${testSuitePath}" -executionProfile="default" -browserType="Chrome"`;

  exec(katalonCommand, (error, stdout, stderr) => {
    if (error) {
      console.error(stderr);
      return res.status(500).json({ message: 'Katalon execution failed', error: stderr });
    }

    const reportsDir = path.join(path.dirname(projectPath), 'Reports');
    const latestRun = fs.readdirSync(reportsDir)
      .map(f => path.join(reportsDir, f))
      .filter(f => fs.statSync(f).isDirectory())
      .sort((a, b) => fs.statSync(b).mtime - fs.statSync(a).mtime)[0];

    const reportPath = path.join(latestRun, 'report.html');
    if (fs.existsSync(reportPath)) {
      const content = fs.readFileSync(reportPath, 'utf-8');
      return res.send(content);
    } else {
      return res.status(404).json({ message: 'Report not found' });
    }
  });
});

module.exports = router;
