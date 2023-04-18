import React, { useState, useEffect } from "react";
import "../App.css";
import PatientCard from "./PatientCard";
import { useNavigate } from "react-router-dom";

function InstitutionDashboard({ userInfo }) {
  const navigate = useNavigate();

  function handleNewPatientForm() {
    navigate({ pathname: "/newPatientForm" });
  }

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
      <div className="patientCardGrid">
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
        <div className="cardItem">
          <PatientCard />
        </div>
      </div>
    </div>
  );
}

export default InstitutionDashboard;
