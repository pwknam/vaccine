import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import Person from "../images/person.svg";

function PatientCard({ patientData, patientDL, setPatient, setNewPatient }) {
  const navigate = useNavigate();

  function handlePatientDashboard() {
    patientDL(patientData.dl_number);
    setPatient(patientData);
    navigate({ pathname: "/patientDashboard" });
  }
  return (
    <div className="patientCard" onClick={handlePatientDashboard}>
      <img src={Person} alt="person" style={{ width: 70, height: 70 }}></img>
      <p className="nameCard">{patientData.name}</p>
      <p>DL#: {patientData.dl_number}</p>
    </div>
  );
}

export default PatientCard;
