export default function Footer() {
  return (
    <div className="py-5">
      <footer className="px-10 flex justify-between">
        <div>
          <p>
            <strong>Paco Drawing Stats</strong> is a data viz and an open-source
            project created by Kuroji Fusky. I do not own or claim any of the
            third-party content to this site whatsoever.
          </p>
          <p>
            <strong>NOTE:</strong> Prior to 2019, most the artwork presented on
            this website is primarily for analytical purposes. He has stopped
            licensing his work under Creative Commons on DeviantArt.
          </p>
          <p className="text-sm">{`© ${new Date().getFullYear()} Kuroji Fusky`}</p>
        </div>
        <div>source code and other links</div>
      </footer>
    </div>
  )
}
