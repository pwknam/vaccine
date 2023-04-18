import "../App.css";
import { useNavigate } from "react-router-dom";

function SearchPage() {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate({ pathname: "/validatorDashboard" });
  };

  return (
    <div className="searchContainer">
      <h1>Search Patient</h1>
      <form className="searchForm" onSubmit={handleSubmit}>
        <input
          type="text"
          className="searchBar"
          placeholder="Drivers License Number"
        ></input>
        <button className="createAccountButton">Search</button>
      </form>
    </div>
  );
}

export default SearchPage;
