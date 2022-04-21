interface IContainerProps {
  children: React.ReactNode;
  mainClassName?: string;
}

export default function Container({children, mainClassName}: IContainerProps) {
  return (
    <paco-app-container className={mainClassName}>
      {children}
    </paco-app-container>
  )
};
