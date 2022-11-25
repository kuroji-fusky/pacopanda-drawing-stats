import Head from "next/head";
import { LayoutProps } from "./Layout";

interface PageContainerProps extends LayoutProps {
  title: string;
  description: string;
  img: string;
}

export function PageContainer(props: Partial<PageContainerProps>) {
  const defaults = {
    title: "Boilerplate app",
    description: "Boilerplate app",
  };

  return (
    <>
      <Head>
        <title>{props.title ?? defaults.title}</title>
        <meta
          name="description"
          content={props.description ?? defaults.description}
        />

        <meta property="og:title" content={props.title ?? defaults.title} />
        <meta
          property="og:description"
          content={props.description ?? defaults.description}
        />

        <meta name="twitter:title" content={props.title ?? defaults.title} />
        <meta
          name="twitter:description"
          content={props.description ?? defaults.description}
        />
      </Head>
      <main>{props.children}</main>
    </>
  );
}
