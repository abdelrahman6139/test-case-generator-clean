import React, { useEffect, useState } from 'react';
import api from '../api';

const Protected = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get('/protected');
        setMessage(response.data.message);
      } catch (error) {
        alert(error.response.data.message);
      }
    };

    fetchData();
  }, []);

  return <h1>{message}</h1>;
};

export default Protected;
