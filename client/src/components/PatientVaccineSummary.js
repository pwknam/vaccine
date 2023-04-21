import React, { useState, useEffect } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import PatientVaccineSummaryCard from "./PatientVaccineSummaryCard";
import phone from "../images/phone.svg";

function PatientVaccineSummary({ user }) {
  const [vaccinations, setVaccinations] = useState([]);

  useEffect(() => {
    fetch(`/patients/${user.dl_number}`)
      .then((r) => r.json())
      .then((data) => {
        console.log(data.vaccinations);
        setVaccinations(data.vaccinations);
      });
  }, [user]);

  const displayVaccinations = vaccinations
    ? vaccinations.map((vaccination) => {
        return <PatientVaccineSummaryCard vaccination={vaccination} />;
      })
    : null;

  return (
    <div>
      <div className="vaccineSummaryTitleDiv">
        <h1 className="patientName">{user.name}</h1>
        <img src={phone} alt="phone" className="phone" />
        <h2>Vaccine Summary</h2>
        <div>
          {/* <PatientVaccineSummaryCard /> */}
          {displayVaccinations}
        </div>
      </div>
    </div>
  );
}

export default PatientVaccineSummary;
