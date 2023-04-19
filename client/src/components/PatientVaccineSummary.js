import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import PatientVaccineSummaryCard from "./PatientVaccineSummaryCard";

function PatientVaccineSummary() {
  return (
    <div>
      <div className="vaccineSummaryTitleDiv">
        <h1>Patient Name</h1>
        <h3>Vaccine Summary</h3>
        <div>
          <PatientVaccineSummaryCard />
        </div>
      </div>
    </div>
  );
}

export default PatientVaccineSummary;
