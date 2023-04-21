import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import vaccineImage from "../images/CV.svg";

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
      <h1 className="landingPageTitle">
        Welcome to Haiti's Vaccination Portal
      </h1>
      <h2 style={{ color: "#2F2E41" }}>
        Our current vaccination rate is at 50%. Please help us work towards a
        healthier future
      </h2>
      <div className="landingPageImage">
        <img
          src={vaccineImage}
          alt="Coronavirus Vaccine"
          style={{ width: 600, height: 600 }}
        />
      </div>
      <div className="landingPageButtonsDiv">
        <button className="button-46" onClick={handleClickPatient}>
          Patient
        </button>
        <h3 className="or">or</h3>
        <button className="button-46" onClick={handleClickInstitution}>
          Institution
        </button>

      </div>
    </div>
  );
}

export default LandingPage;
