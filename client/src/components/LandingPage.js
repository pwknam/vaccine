import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();

  function handleClickInstitution() {
    navigate({ pathname: "/institutionLandingPage" });
  }

  function handleClickPatient() {
    navigate({ pathname: "/patientLandingPage" });
  }

  return (
    <div className="landingPage">
      <h1>Vaccine Verification</h1>
      <h2 id="selection">Please Select</h2>
      <div className="landingPageButtonsDiv">
        <button className="mainButton" onClick={handleClickPatient}>
          Patient
        </button>
        <p>or</p>
        <button className="mainButton" onClick={handleClickInstitution}>
          Institution
        </button>
      </div>
    </div>
  );
}

export default LandingPage;
