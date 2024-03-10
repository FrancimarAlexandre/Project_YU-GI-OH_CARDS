// pages/login.js
import React from 'react';
import Link from 'next/link';
import styles from '../styles/Login.module.css';

export default function Login() {
  return (
    <div className={styles.loginContainer}>
      <form className={styles.form}>
        <h1>Login</h1>
        <input type="email" placeholder="Email" className={styles.inputField} />
        <input type="password" placeholder="Senha" className={styles.inputField} />
        <button type="submit" className="buttonSubmit">Entrar</button>
        <a href="/cadastro" className="aLink">
          <p>Não tem uma conta? Cadastre-se</p>
        </a>
      </form>
    </div>
  );
}
