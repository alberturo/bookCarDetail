import "./LandingPage.css";
import LanguageSlide from "./LanguageSlide";
import { FaArrowLeft, FaArrowRight } from "react-icons/fa";
import { useState } from "react";
import { useEffect } from "react";

const LANGUAGE_IMAGES = {
  0: {
    url: "https://i.ibb.co/nMRhT5w/american-literature-history-of-the-genre-feature.webp",
    lang: "English",
  },
  1: {
    url: "https://i.ibb.co/GJYYZfw/spanish-literature-prisma-archivo.jpg",
    lang: "Spanish",
  },
  2: {
    url: "https://i.ibb.co/DbMT9Yd/unnamed.jpg",
    lang: "Japanese",
  },
};

function LandingPage() {
  const [currentSlide, setCurrentSlide] = useState(0);
  useEffect(() => {}, []);
  return (
    <div className="landing-page">
      <div className="title-about-us">
        <h1 className="title">Hello Reader👋📚</h1>
        <p>
          Do you want to improves your vocabulary? Do you want to enhance
          critical thinking and analytical skills?, How about expant creativity
          and imagination? Yes! This place is for you
        </p>
      </div>
      <div className="slides-container">
        <FaArrowLeft
          id="left-arrow"
          onClick={() =>
            setCurrentSlide((curr) => (curr > 0 ? curr - 1 : curr))
          }
        />
        <LanguageSlide slideInfo={LANGUAGE_IMAGES[currentSlide]} />
        <FaArrowRight
          id="right-arrow"
          onClick={() =>
            setCurrentSlide((curr) => (curr <= 1 ? curr + 1 : curr))
          }
        />
      </div>
    </div>
  );
}

export default LandingPage;
