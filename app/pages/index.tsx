import Link from "next/link";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDeviantart } from "@fortawesome/free-brands-svg-icons";
import Container from "../components/Container";

export default function Home() {
  return (
    <Container title="Home" description="Stats for latest drawings">
      <div>
        <h2>Browse the art lol</h2>
        <Link href="deviantart.com" passHref>
          <a>
            <FontAwesomeIcon icon={faDeviantart} />
          </a>
        </Link>
      </div>
    </Container>
  );
}
