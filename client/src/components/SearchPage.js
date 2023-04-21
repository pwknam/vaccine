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
    <div>
      <Home className="home" setSearch={setSearch}/>
        {/* <div className="separator" /> */}
     
      <div className="searchContainer">

      

        <form className="searchForm" onSubmit={handleSubmit}>
        <h2>Or Enter License Number</h2>
          <input
            type="text"
            className="bar"
            placeholder="Drivers License Number"
            value={dl}
            onChange={(e) => setSearch(e.target.value)}
          ></input>
          <button className="button-47">Search</button>
        </form>
      </div>



      </div>
  );
}

export default SearchPage;