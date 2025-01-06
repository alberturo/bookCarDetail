import { useNavigate } from "react-router-dom";

const LANGUAGES = { English: "eng", Spanish: "sp", Japanese: "jp" };

function LanguageSlide({ slideInfo }) {
  const navigate = useNavigate();
  return (
    <div className="img-slide-container">
      <h2 id="slide-title" style={{ color: "#98d4e1", fontFamily: "Delius" }}>
        {slideInfo.lang}
      </h2>
      <img
        onClick={() => navigate(`/books/${LANGUAGES[slideInfo.lang]}`)}
        src={`${slideInfo.url}`}
        style={{ width: "300px" }}
      />
    </div>
  );
}

export default LanguageSlide;
