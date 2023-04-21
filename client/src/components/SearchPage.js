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
    <>
    <Home setSearch={setSearch}/>

    <div className="searchContainer">
      <h2>Or Search for License</h2>
      {/* <div className="landingPageImage">
        <img src={Search} alt="Search" style={{ width: 400, height: 400 }} />
      </div> */}
      <form onSubmit={handleSubmit}>
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
    </>
  );
}

export default SearchPage;
