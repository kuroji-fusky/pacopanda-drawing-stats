
import Link from 'next/link';
import styles from '../styles/Base.module.scss';

export default function Header() {
  return (
    <header>
      <div id={styles.wrapper}>
        {/* <img src="/static/images/logo.png" alt="logo" /> */}
        <nav className="flex gap-x-6">
          <Link href="/" passHref>Home</Link>
          <Link href="/data" passHref>Browse data</Link>
          <Link href="/about" passHref>About this project</Link>
        </nav>
      </div>
    </header>
  );
};