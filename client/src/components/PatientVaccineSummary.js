import React, { useState, useEffect } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import PatientVaccineSummaryCard from "./PatientVaccineSummaryCard";

function PatientVaccineSummary({user}) {
  const [vaccinations, setVaccinations] = useState([])

  useEffect(() => {
    fetch(`/patients/${user.dl_number}/${user.role}`)
    .then(r => r.json())
    .then(data => {
      console.log(data.vaccinations)
      setVaccinations(data.vaccinations)
    })
  },[user])

  const displayVaccinations = vaccinations ? vaccinations.map((vaccination) => {
    return <PatientVaccineSummaryCard vaccination={vaccination}/>
  }) : null;

  return (
    <div>
      <div className="vaccineSummaryTitleDiv">
        <h1>{user.name}</h1>
        <h3>Vaccine Summary</h3>
        <div>
          {/* <PatientVaccineSummaryCard /> */}
          {displayVaccinations}
        </div>
      </div>
    </div>
  );
}

export default PatientVaccineSummary;
