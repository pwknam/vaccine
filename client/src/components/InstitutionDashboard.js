import React, { useState, useEffect } from "react";
import "../App.css";
import PatientCard from "./PatientCard";
import { useNavigate } from "react-router-dom";

function InstitutionDashboard({ userInfo, DL, setPatient, patients }) {
  // console.log(userInfo.patients[0].patients.dl_number);
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  function handleNewPatientForm() {
    navigate({ pathname: "/newPatientForm" });
  }
  console.log(userInfo);
  // console.log(typeof patients[0].dl_number);
  const patientsToDisplay = patients?.filter((patient) =>
    patient.name.includes(search) ||
    patient.dl_number.toString().includes(search)
      ? patient
      : null
  );
  const renderPatientCards = userInfo.patients
    ? patientsToDisplay.map((patient) => {
        return (
          <div className="cardItem">
            <PatientCard
              key={patient.dl_number}
              patientData={patient}
              patientDL={DL}
              setPatient={setPatient}
            />
          </div>
        );
      })
    : null;

  return (
    <div className="institutionDashboardPage">
      <div className="topBar">
        <h1>{userInfo.username}</h1>
        <button onClick={handleNewPatientForm}>New Patient</button>
      </div>
      <div className="searchBarDiv">
        <input
          type="text"
          placeholder="Search Patient"
          className="searchBar"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        ></input>
      </div>
      <div className="patientCardGrid">{renderPatientCards}</div>
    </div>
  );
}

export default InstitutionDashboard;
