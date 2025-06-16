import React, { useState } from 'react';
import api from '../api';

const Register = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
  });
  const [success, setSuccess] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    try {
      const response = await api.post('/register', formData);
      setSuccess(response.data.message);

      // حفظ بيانات المستخدم
      localStorage.setItem("user", JSON.stringify({
        name: formData.name,
        email: formData.email
      }));

      // تفريغ الحقول بعد التسجيل
      setFormData({ name: '', email: '', password: '' });
    } catch (err) {
      setError(err.response?.data?.message || 'Something went wrong');
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #1f1c2c, #928dab)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px'
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
        <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>📝 Register</h2>

        {success && (
          <div style={{ backgroundColor: '#d4edda', padding: '10px', borderRadius: '8px', color: '#155724', marginBottom: '10px' }}>
            ✅ {success}
          </div>
        )}
        {error && (
          <div style={{ backgroundColor: '#f8d7da', padding: '10px', borderRadius: '8px', color: '#721c24', marginBottom: '10px' }}>
            ❌ {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <label>Name</label>
          <input
            type="text"
            name="name"
            className="form-control mb-3"
            value={formData.name}
            onChange={handleChange}
            required
          />

          <label>Email</label>
          <input
            type="email"
            name="email"
            className="form-control mb-3"
            value={formData.email}
            onChange={handleChange}
            required
          />

          <label>Password</label>
          <input
            type="password"
            name="password"
            className="form-control mb-4"
            value={formData.password}
            onChange={handleChange}
            required
          />

          <button
            type="submit"
            style={{
              backgroundColor: '#0066ff',
              color: '#fff',
              border: 'none',
              width: '100%',
              padding: '10px',
              borderRadius: '8px',
              fontWeight: 'bold'
            }}
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
