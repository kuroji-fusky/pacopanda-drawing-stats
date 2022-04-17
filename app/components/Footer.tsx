import styles from '../styles/Base.module.scss';

export default function Footer() {
  return(
    <footer>
      <div id={styles.wrapper}>
        <div id="footer-content">
        <p>&copy; 2021-{new Date().getFullYear()}</p>
        </div>
      </div>
    </footer>
  );
};