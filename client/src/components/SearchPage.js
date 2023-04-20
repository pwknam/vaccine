import "../App.css";
import { useNavigate } from "react-router-dom";
import React, { useState } from 'react'
import Home from "./Home/Home";

function SearchPage({setSearch, dl}) {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate({ pathname: "/validatorDashboard" });
  };

  return (
    <div className="searchContainer">
      <h1>Search Patient or Upload License Photo</h1>
      <form className="searchForm" onSubmit={handleSubmit}>
        <input
          type="text"
          className="searchBar"
          placeholder="Drivers License Number"
          value={dl}
          onChange={(e) => setSearch(e.target.value)}
        ></input>
        {/* IF YOU WANT TO GET RID OF THE UGLY OCR THEN COMMENT OUT THE HOME COMPONENT - I NEED TO RENAME ANYWAYS */}
        <Home setSearch={setSearch}/>
        <button className="createAccountButton">Search</button>
      </form>
    </div>
  );
}

export default SearchPage;
