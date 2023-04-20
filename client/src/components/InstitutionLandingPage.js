import React from "react";
import "../App.css";
import { Route, Routes, useNavigate } from "react-router-dom";
import InstitutionSignupLogin from "./InstitutionSignupLogin";

function InstitutionLandingPage() {
  const navigate = useNavigate();

  function handleCreateAccount() {
    navigate({ pathname: "/institutionCreateAccount" });
  }

  function handleLoginPage() {
    navigate({ pathname: "/institutionLogin" });
  }

  return (
    <div>
      <div className="landingPage">
        <h1>Institution Portal</h1>
        {/* <h2 id="selection">Help us make Haiti a healthier place :)</h2> */}
        <div className="landingPageButtonsDiv">
          <div className="createContainer">
            <button className="button-46" onClick={handleCreateAccount}>
              Create Account
            </button>
          </div>
          {/* <p className="or">or</p> */}
          <div className="loginContainer">
            <button className="button-46" onClick={handleLoginPage}>
              Login
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default InstitutionLandingPage;
