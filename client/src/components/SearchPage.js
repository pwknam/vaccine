import "../App.css";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import Search from "../images/search.svg";
import Home from "./Home/Home";

function SearchPage({ setSearch, dl }) {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate({ pathname: "/validatorDashboard" });
  };

  return (
    <div className="searchContainer">
      <h1>Search Patient</h1>
      {/* <div className="landingPageImage">
        <img src={Search} alt="Search" style={{ width: 400, height: 400 }} />
      </div> */}
      <form className="searchForm" onSubmit={handleSubmit}>
        <input
          type="text"
          className="bar"
          placeholder="Drivers License Number"
          value={dl}
          onChange={(e) => setSearch(e.target.value)}
        ></input>
        {/* IF YOU WANT TO GET RID OF THE UGLY OCR THEN COMMENT OUT THE HOME COMPONENT - I NEED TO RENAME ANYWAYS */}
        {/* <Home/> */}
        <button className="button-47">Search</button>
        <Home setSearch={setSearch} />
      </form>
    </div>
  );
}

export default SearchPage;
