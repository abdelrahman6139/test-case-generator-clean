import React, { useState } from 'react';
import { Container, Form, Button, Alert, Card } from 'react-bootstrap';
import axios from 'axios';
import * as XLSX from 'xlsx';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [requirements, setRequirements] = useState([]);
  const [testCases, setTestCases] = useState({});
  const [scripts, setScripts] = useState({});
  const [newReq, setNewReq] = useState('');
  const [isUploading, setIsUploading] = useState(false);
  const [uploadError, setUploadError] = useState(null);
  const [uploadSuccess, setUploadSuccess] = useState(false);
  const [lastLogs, setLastLogs] = useState({});
  const [runStatus, setRunStatus] = useState({});

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setUploadError(null);
      setUploadSuccess(false);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setIsUploading(true);
    setUploadError(null);
    setUploadSuccess(false);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/api/upload', formData);
      setRequirements(response.data.requirements || []);
      setTestCases({});
      setScripts({});
      setUploadSuccess(true);
    } catch (error) {
      setUploadError('Upload failed');
    } finally {
      setIsUploading(false);
    }
  };

  const handleGenerateTestCase = async (index) => {
    try {
      const response = await axios.post('http://localhost:5001/generate_test_case', {
        requirement: requirements[index].sentence || requirements[index],
      });

      const parsedCases = response.data.test_cases || [];
      const updatedCases = { ...testCases, [index]: parsedCases };
      const scriptList = parsedCases.map(tc => tc.selenium_script);
      const updatedScripts = { ...scripts, [index]: scriptList };

      setTestCases(updatedCases);
      setScripts(updatedScripts);
    } catch (error) {
      const updated = { ...testCases };
      updated[index] = 'Failed to generate test case: ' + error.message;
      setTestCases(updated);
    }
  };

  const handleScriptChange = (reqIndex, scriptIndex, newValue) => {
    const updatedScripts = { ...scripts };
    if (updatedScripts[reqIndex]) {
      updatedScripts[reqIndex][scriptIndex] = newValue;
    }
    setScripts(updatedScripts);
  };

  const handleRunScript = async (code, reqIndex, scriptIndex) => {
    const key = `${reqIndex}_${scriptIndex}`;
    try {
      const response = await axios.post('http://localhost:5001/run_custom_script', {
        script: code,
        index: key
      });

      const result = response.data?.result || "failed";
      const stdout = response.data?.stdout || "";

      setRunStatus(prev => ({ ...prev, [key]: result }));

      if (!stdout.trim()) {
        alert("⚠️ Script executed but response incomplete.");
      }

    } catch (error) {
      console.error("Script run error:", error);
      setRunStatus(prev => ({ ...prev, [key]: "failed" }));
      alert('⚠️ Script execution failed.');
    }
  };

  const handleViewLastResult = async (reqIndex, scriptIndex) => {
    const key = `${reqIndex}_${scriptIndex}`;
    try {
      const response = await axios.get(`http://localhost:5001/test_result_log?index=${key}`);
      setLastLogs(prev => ({ ...prev, [key]: response.data.log }));
    } catch (error) {
      alert('Failed to load test result log.');
    }
  };

  const handleDeleteRequirement = (index) => {
    const updated = [...requirements];
    updated.splice(index, 1);
    setRequirements(updated);
    const testCopy = { ...testCases };
    delete testCopy[index];
    setTestCases(testCopy);
    const scriptCopy = { ...scripts };
    delete scriptCopy[index];
    setScripts(scriptCopy);
    const logsCopy = { ...lastLogs };
    const statusCopy = { ...runStatus };
    Object.keys(logsCopy).forEach(key => {
      if (key.startsWith(`${index}_`)) delete logsCopy[key];
    });
    Object.keys(statusCopy).forEach(key => {
      if (key.startsWith(`${index}_`)) delete statusCopy[key];
    });
    setLastLogs(logsCopy);
    setRunStatus(statusCopy);
  };

  const handleAddRequirement = () => {
    if (!newReq.trim()) return;
    setRequirements([...requirements, newReq.trim()]);
    setNewReq('');
  };

  const handleDownloadExcel = () => {
    const allTestCases = Object.values(testCases).flat();
    const worksheet = XLSX.utils.json_to_sheet(allTestCases);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'TestCases');
    XLSX.writeFile(workbook, 'test_cases.xlsx');
  };

  const handleOpenAllureReport = () => {
    window.open("http://localhost:5001/show_report", "_blank");
  };

  return (
    <Container className="py-4">
      <h2>Upload SRS Document</h2>

      {uploadError && <Alert variant="danger">{uploadError}</Alert>}
      {uploadSuccess && <Alert variant="success">File uploaded successfully!</Alert>}

      <Form.Group className="mb-3">
        <Form.Control type="file" onChange={handleFileChange} />
        <Button onClick={handleUpload} className="mt-2" disabled={isUploading || !file}>
          {isUploading ? 'Uploading...' : 'Upload'}
        </Button>
      </Form.Group>

      <div className="mb-4">
        <Button variant="dark" onClick={handleOpenAllureReport}>
          Open Allure Report
        </Button>
      </div>

      <h4>Add Requirement Manually</h4>
      <Form.Group className="mb-4 d-flex">
        <Form.Control
          type="text"
          placeholder="Enter requirement"
          value={newReq}
          onChange={(e) => setNewReq(e.target.value)}
        />
        <Button variant="secondary" onClick={handleAddRequirement} className="ms-2">
          Add
        </Button>
      </Form.Group>

      <h3>Extracted Requirements</h3>
      {requirements.length === 0 && <Alert variant="info">No requirements to show.</Alert>}

      {requirements.map((req, index) => (
        <Card key={index} className="mb-3">
          <Card.Header>
            Requirement #{index + 1}
            <Button
              variant="danger"
              size="sm"
              className="float-end"
              onClick={() => handleDeleteRequirement(index)}
            >
              Delete
            </Button>
          </Card.Header>
          <Card.Body>
            <Card.Text>{req.sentence || req}</Card.Text>
            <Button
              onClick={() => handleGenerateTestCase(index)}
              variant="primary"
              className="mb-2"
            >
              Generate Test Cases
            </Button>

            {testCases[index] && Array.isArray(testCases[index]) && (
              <div className="border p-2 bg-light">
                {testCases[index].map((tc, i) => {
                  const logKey = `${index}_${i}`;
                  return (
                    <div key={i} className="mb-4">
                      <strong>ID:</strong> {tc.id}<br />
                      <strong>Test Case ID:</strong> {tc.test_case_id}<br />
                      <strong>Topic:</strong> {tc.topic}<br />
                      <strong>Scenario:</strong> {tc.test_scenario}<br />
                      <strong>Expected:</strong> {tc.expected_intended_result}<br />
                      <strong>Criteria:</strong> {tc.pass_fail_criteria}<br />
                      <strong>Steps:</strong>
                      <ul>
                        {tc.test_steps?.map((step, si) => (
                          <li key={si}>{step}</li>
                        ))}
                      </ul>
                      <strong>Python Script:</strong>
                      <Form.Control
                        as="textarea"
                        rows={10}
                        value={scripts[index]?.[i] || ''}
                        onChange={(e) => handleScriptChange(index, i, e.target.value)}
                      />
                      <Button className="mt-2 me-2" variant="success" onClick={() => handleRunScript(scripts[index][i], index, i)}>
                        Run This Script
                      </Button>
                      <Button className="mt-2" variant="info" onClick={() => handleViewLastResult(index, i)}>
                        View Last Result
                      </Button>

                      {runStatus[logKey] && (
                        <Alert
                          variant={
                            runStatus[logKey] === 'passed' ? 'success' :
                            runStatus[logKey] === 'failed' ? 'danger' : 'secondary'
                          }
                          className="mt-2"
                        >
                          Test Status: <strong>{runStatus[logKey]}</strong>
                        </Alert>
                      )}

                      {lastLogs[logKey] && (
                        <Alert variant="secondary" className="mt-3" style={{ whiteSpace: 'pre-wrap' }}>
                          {lastLogs[logKey]}
                        </Alert>
                      )}
                    </div>
                  );
                })}
              </div>
            )}
          </Card.Body>
        </Card>
      ))}

      {Object.keys(testCases).length > 0 && (
        <div className="text-center mt-4">
          <Button variant="success" onClick={handleDownloadExcel}>Download All Test Cases as Excel</Button>
        </div>
      )}
    </Container>
  );
};

export default FileUpload;
