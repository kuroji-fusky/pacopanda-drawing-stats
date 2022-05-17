import Head from 'next/head';
import styles from '../styles/Layout.module.scss';

interface IContainerProps {
  children: any;
  title: string;
  description: string;
  mainClassName?: string;
}

export default function Container({
  children,
  title,
  description,
  mainClassName = `${styles['content-wrapper']}`
}: IContainerProps) {
  const siteTitle = "Paco Drawing Stats";
  return (
    <>
      <Head>
        <meta name="description" content={description} />
        <meta property="og:site_name" content={siteTitle} />
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description} />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={title} />
        <meta name="twitter:description" content={description} />
        <title>{title} • {siteTitle}</title>
      </Head>
      <div className={mainClassName}>{children}</div>
    </>
  );
};
