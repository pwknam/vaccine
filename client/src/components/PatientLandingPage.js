import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function PatientLandingPage() {
  const navigate = useNavigate();

  function handleClickActivatePage() {
    navigate({ pathname: "/activateAccount" });
  }

  function handleClickLoginPage() {
    navigate({ pathname: "/institutionLogin" });
  }

  return (
    <div>
      <div className="landingPage">
        <h1>Patient Portal</h1>
        {/* <h2 id="selection">Please Select</h2> */}
        <div className="landingPageButtonsDiv">
          <button className="button-46" onClick={handleClickActivatePage}>
            Activate Account
          </button>
          <p className="or"></p>
          <button className="button-46" onClick={handleClickLoginPage}>
            Login
          </button>
        </div>
      </div>
    </div>
  );
}

export default PatientLandingPage;
