import React from 'react';
import Link from 'next/link';
import styles from '../styles/Home.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <h1>Bem-vindo ao nosso site!</h1>
      <div className={styles.buttonContainer}>
        <a href="/login" className={styles.Link}>
          <button className={styles.button}>Login</button>
        </a>
        <a href="/cadastro" className={styles.Link}>
          <button className={styles.button}>Cadastro</button>
        </a>
      </div>
    </div>
  );
}

