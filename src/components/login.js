import React, { useState } from 'react';
import api from '../api';

const Login = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setSuccessMessage('');

    try {
      const response = await api.post('/login', formData);

      // حفظ التوكن وكامل بيانات المستخدم
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('user', JSON.stringify(response.data.user));
      window.location.href = "/upload";

      setSuccessMessage('✅ Login successful');
      setFormData({ email: '', password: '' });
    } catch (error) {
      setErrorMessage(error.response?.data?.message || 'Something went wrong');
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #000428, #004e92)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
      }}
    >
      <div
        style={{
          background: '#fff',
          padding: '30px',
          borderRadius: '16px',
          boxShadow: '0 8px 24px rgba(0,0,0,0.3)',
          maxWidth: '400px',
          width: '100%',
        }}
      >
        <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>🔐 Login</h2>

        {successMessage && (
          <div style={{ backgroundColor: '#d4edda', padding: '10px', borderRadius: '8px', color: '#155724', marginBottom: '10px' }}>
            {successMessage}
          </div>
        )}
        {errorMessage && (
          <div style={{ backgroundColor: '#f8d7da', padding: '10px', borderRadius: '8px', color: '#721c24', marginBottom: '10px' }}>
            ❌ {errorMessage}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <label>Email</label>
          <input
            type="email"
            name="email"
            className="form-control mb-3"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <label>Password</label>
          <input
            type="password"
            name="password"
            className="form-control mb-4"
            placeholder="Enter your password"
            value={formData.password}
            onChange={handleChange}
            required
          />

          <button
            type="submit"
            style={{
              backgroundColor: '#28a745',
              color: '#fff',
              border: 'none',
              width: '100%',
              padding: '10px',
              borderRadius: '8px',
              fontWeight: 'bold',
            }}
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
