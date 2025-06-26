import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import { Navbar, Nav, Container, Button } from 'react-bootstrap';
import Homepage from './components/home';
import Login from './components/login';
import Register from './components/register';
import FileUpload from './components/FileUpload';
import ProtectedRoute from './components/ProtectedRoute';
import History from './components/History'; // ✅ Added

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  let user = {};
  try {
    user = JSON.parse(localStorage.getItem('user') || '{}');
  } catch (error) {
    console.error("Invalid user JSON in localStorage", error);
    user = {};
  }

  return (
    <Router>
      <NavigationBar />
      <Container className="mt-4">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/upload"
            element={
              <ProtectedRoute>
                <FileUpload />
              </ProtectedRoute>
            }
          />
          <Route
            path="/history"
            element={
              <ProtectedRoute>
                <History userId={user?._id} />
              </ProtectedRoute>
            }
          />
        </Routes>
      </Container>
    </Router>
  );
}

const NavigationBar = () => {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');
  let user = {};
  try {
    user = JSON.parse(localStorage.getItem('user') || '{}');
  } catch (error) {
    console.error("Invalid user JSON in localStorage", error);
    user = {};
  }

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/login');
  };

  return (
    <Navbar bg="dark" variant="dark" expand="lg" sticky="top">
      <Container>
        <Navbar.Brand as={Link} to="/">reshooooo</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/upload">Upload SRS</Nav.Link>
            {token && (
              <Nav.Link as={Link} to="/history">📜 History</Nav.Link> // ✅ Added
            )}
            {token ? (
              <>
                <Nav.Link disabled style={{ color: '#0f0' }}>
                  👋 Welcome {user?.email?.split('@')[0]}
                </Nav.Link>
                <Button variant="outline-danger" size="sm" onClick={handleLogout}>
                  Logout
                </Button>
              </>
            ) : (
              <>
                <Nav.Link as={Link} to="/login">Login</Nav.Link>
                <Nav.Link as={Link} to="/register">Register</Nav.Link>
              </>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default App;
