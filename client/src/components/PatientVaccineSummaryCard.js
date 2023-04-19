import React, { useState } from "react";
import "../App.css";

function PatientVaccineSummaryCard() {
  const [isToggled, setIsToggled] = useState(false);

  const handleToggle = () => {
    setIsToggled(!isToggled);
  };

  return (
    <div className="cardContainer">
      <div className="cardTitle">
        <h3>Vaccine Name</h3>
      </div>

      <div className="cardDetails">
        <div className="cardDetail">
          <p className="cardDetailTitle">Issuer</p>
          <p>Hospital Name</p>
        </div>
        <div className="cardDetail">
          <p className="cardDetailTitle">Valid Through</p>
          <p>Date</p>
        </div>
        <div className="cardDetail">
          <p className="cardDetailTitle">Privacy</p>
          <button
            className={`toggle-button ${isToggled ? "toggled" : ""}`}
            onClick={handleToggle}
          >
            {isToggled ? "On" : "Off"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default PatientVaccineSummaryCard;
