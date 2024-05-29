// pages/login.js
import React, {useState} from 'react';
import Link from 'next/link';
import styles from '../styles/Login.module.css';

export default function Cadastro() {
  const [data, setData] = useState({
    username :'',
    email: '',
    password:''
  });

  const handleChange = (e) =>{
    const {name, value} = e.target;
    setData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

 const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/usuario/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      const result = await response.json();
      console.log('Success:', result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          value={data.username}
          onChange={handleChange}
          placeholder="Username"
        />
        <input
          type="email"
          name="email"
          value={data.email}
          onChange={handleChange}
          placeholder="Email"
        /> 
         <input
        type="password"
        name="password"
        value={data.password}
        onChange={handleChange}
        placeholder="Password"
      />
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
}
