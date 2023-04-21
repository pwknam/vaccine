import React, { useState } from "react";
import "../App.css";

function PatientVaccineSummaryCard({ vaccination }) {
  const [vaccinationVisibility, setVaccinationVisibility] = useState(
    vaccination.visibility
  );
  console.log(vaccination);

  const handleToggle = () => {
    fetch(`/vaccinations/${vaccination.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        visibility: !vaccinationVisibility,
      }),
    })
      .then((r) => r.json())
      .then((data) => setVaccinationVisibility(data.visibility));
  };

  return (
    <div className="cardContainer">
      <div className="cardTitle">
        {/* <h3>Vaccine Name</h3> */}
        <h3>{vaccination.name}</h3>
      </div>

      <div className="cardDetails">
        <div className="cardDetail">
          <p className="cardDetailTitle">Issuer</p>
          <p>{vaccination.issuer_name}</p>
        </div>
        <div className="cardDetail">
          <p className="cardDetailTitle">Valid Through</p>
          <p>{vaccination.expiration_date}</p>
        </div>
        <div className="cardDetail">
          <p className="cardDetailTitle">Privacy</p>
          <button
            className={`toggle-button ${
              vaccinationVisibility ? "" : "toggled"
            }`}
            onClick={handleToggle}
          >
            {vaccinationVisibility ? "Off" : "On"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default PatientVaccineSummaryCard;
