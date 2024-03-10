// pages/login.js
import React from 'react';
import Link from 'next/link';
import styles from '../styles/Login.module.css';

export default function Cadastro() {
  return (
    <div className={styles.loginContainer}>
      <form className={styles.form}>
        <h1>Login</h1>
        <input type="email" placeholder="Email" className={styles.inputField} />
        <input type="password" placeholder="Senha" className={styles.inputField} />
        <button type="submit">Entrar</button>
        <a href="/login">
          <p>Já tem uma conta? Login</p>
        </a>
      </form>
    </div>
  );
}
