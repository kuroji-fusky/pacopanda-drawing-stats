import BaseHead from "../components/BaseHead"
import Container from "../components/Container"

export default function PageNotFound() {
  return(
    <>
      <BaseHead title="Page not found" description="The page you are looking for does not exist... Sorry about that!" />
      <Container mainClassName="grid place-items-center">
        <h1>Page not found stupid</h1>
      </Container>
    </>
  )
};
