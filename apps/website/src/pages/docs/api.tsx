import Container from "@/components/Base/Container"
import { NoticeCard } from "@/components/UI"

export default function ApiDocs() {
  return (
    <Container t="API docs" d="PDS API docs" wrap>
      <div className="px-10">
        <NoticeCard state="info" heading="Under construction">
          <p>Documentation is still incomplete and missing!</p>
        </NoticeCard>
        This page is a documentation for REST and GraphQL APIs including its
        standalone JavaScript and Python SDKs.
      </div>
    </Container>
  )
}
