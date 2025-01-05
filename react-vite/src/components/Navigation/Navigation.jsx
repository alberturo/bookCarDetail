import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import BooksButton from "./BooksButton";
import SearchBar from "./SearchBar";

function Navigation() {
  return (
    <nav>
      <ul className="navbar">
        <li className="home-logo">
          <NavLink to="/">
            <img
              src="https://i.ibb.co/DDMLnDb/Disen-o-sin-ti-tulo-3.png"
              alt="Disen-o-sin-ti-tulo-3"
              border="0"
            ></img>
          </NavLink>
        </li>

        <li>
          <span className="middle-links">
            <div>
              <BooksButton />
            </div>
            <button>
              <h3>Reading club</h3>
            </button>
            <div>
              <ProfileButton />
            </div>
          </span>
        </li>

        <li>
          <SearchBar />
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
