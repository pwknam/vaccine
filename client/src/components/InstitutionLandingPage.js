import React from "react";
import "../App.css";
import { Route, Routes, useNavigate } from "react-router-dom";
import InstitutionSignupLogin from "./InstitutionSignupLogin";

function InstitutionLandingPage() {
  const navigate = useNavigate();

  function handleCreateAccount() {
    navigate({ pathname: "/institutionCreateAccount" });
  }

  return (
    <div>
      <div className="landingPage">
        <h1>Vaccine Verification</h1>
        <h2 id="selection">Please Select</h2>
        <div className="landingPageButtonsDiv">
          <button className="mainButton" onClick={handleCreateAccount}>
            Create Account
          </button>
          <p>or</p>
          <button className="mainButton">Login</button>
        </div>
      </div>
    </div>
  );
}

export default InstitutionLandingPage;
