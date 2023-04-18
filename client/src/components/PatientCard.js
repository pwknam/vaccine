import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function PatientCard() {
  const navigate = useNavigate();

  function handlePatientDashboard() {
    navigate({ pathname: "/patientDashboard" });
  }

  return (
    <div className="patientCard" onClick={handlePatientDashboard}>
      <p>Patient Name</p>
      <p>DL# 12345678</p>
    </div>
  );
}

export default PatientCard;
