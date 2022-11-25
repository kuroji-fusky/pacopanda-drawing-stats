import { PageContainer } from "@/components/Base"
import Image from "next/image"

export default function Home() {
  return (
    <PageContainer title="Home page">
      <section id="hero">Sort stuff</section>
      <section id="gather-data" className="h-[50%] w-full">
        <div className="max-w-screen-2xl mx-auto flex gap-10 px-6 items-center">
          <article className="flex flex-col gap-y-1.5">
            <h2 className="text-4xl font-bold">How I gather data</h2>
            <p className="text-lg">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat
              iusto impedit fuga, dolorum mollitia, eligendi nihil voluptates
              numquam ut odit laboriosam?
            </p>
          </article>
        </div>
      </section>
    </PageContainer>
  )
}
