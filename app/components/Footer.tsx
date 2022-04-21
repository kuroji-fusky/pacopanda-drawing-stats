import { faGithub, faInstagram, faTwitter, faYoutube } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

export default function Footer() {
  return (
    <footer>
      <div className="max-w-screen-xl my-0 mx-auto px-4 flex gap-8">
        <div className="text-sm flex flex-col gap-y-2">
          <span>
            <h4 className="font-bold">DISCLAIMER</h4>
            <p>
              Most the artwork presented on this website is primarily for
              informational purposes. Prior to late-2019, he has stopped
              licensing his work for Creative Commons - but despite this, all
              the content is licensed under CC-BY-SA.
            </p>
          </span>
          <p>
            &copy; 2021-{new Date().getFullYear()} skepfusky, some rights
            reserved.
          </p>
        </div>
        <div id="social" className="flex gap-x-3">
          <FontAwesomeIcon icon={faYoutube} />
          <FontAwesomeIcon icon={faTwitter} />
          <FontAwesomeIcon icon={faGithub} />
          <FontAwesomeIcon icon={faInstagram} />
        </div>
      </div>
    </footer>
  );
}
