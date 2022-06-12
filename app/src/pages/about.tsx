import BaseHead from "@/components/base/BaseHead"

export default function About() {
  return (
    <>
      <BaseHead title="About" description="About page" />
      <article>
        <h1>About this project</h1>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque ea
          nemo in nostrum perspiciatis dolor blanditiis tempore. Voluptates,
          quae odit vel vero aperiam laudantium in sit officiis provident esse
          aliquid dignissimos beatae, explicabo culpa ratione. Repudiandae
          officia totam odio sit possimus exercitationem alias quas placeat
          doloremque deleniti. Reprehenderit dolorem itaque consequuntur
          deleniti quos optio rerum? Commodi laborum unde corrupti, minima
          aperiam perferendis exercitationem. Iure dicta hic ea voluptas
          exercitationem! Magni!
        </p>

        <h2>How I Gather Data</h2>
        <p>
          I use an automated Python scripts to extract data from his gallery
          page from FurAffinity, it gathers the title, description, tags, and
          date in each artwork. Then it creates a JSON file with all the data
          for development testing and for adding and updating it to the database
          for the production build.
        </p>
        <p>
          Initially, I was manually adding all the data by hand on a Google
          Sheet, and it was tedious to add all 1,700+ artworks. I decided to use
          a database instead, and it was much easier to add new artworks to the
          database with the use of automated Python scripts.
        </p>
      </article>
    </>
  )
}
