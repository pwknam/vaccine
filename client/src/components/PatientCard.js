import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function PatientCard({ patientData, patientDL, setPatient, setNewPatient }) {
  const navigate = useNavigate();

  function handlePatientDashboard() {
    patientDL(patientData.dl_number);
    setPatient(patientData);
    navigate({ pathname: "/patientDashboard" });
  }
  return (
    <div className="patientCard" onClick={handlePatientDashboard}>
      <p>{patientData.name}</p>
      <p>{patientData.dl_number}</p>
    </div>
  );
}

export default PatientCard;
