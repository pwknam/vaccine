import React, { useState, useEffect } from "react";
import "../App.css";
import PatientCard from "./PatientCard";
import { useNavigate } from "react-router-dom";

function InstitutionDashboard({ userInfo, DL }) {
  // console.log(userInfo.patients[0].patients.dl_number);
  const navigate = useNavigate();

  function handleNewPatientForm() {
    navigate({ pathname: "/newPatientForm" });
  }

  const renderPatientCards = userInfo.patients.map((patient) => {
    return (
      <div className="cardItem">
        <PatientCard
          key={patient.dl_number}
          patientData={patient}
          patientDL={DL}
        />
      </div>
    );
  });

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
        ></input>
      </div>
      <div className="patientCardGrid">{renderPatientCards}</div>
    </div>
  );
}

export default InstitutionDashboard;
