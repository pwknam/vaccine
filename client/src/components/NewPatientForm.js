import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function NewPatientForm({ setNewPatient }) {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [dl_number, setDL_Number] = useState("");

  function handleInstitutionDashboardPage(e) {
    e.preventDefault();
    fetch(`/patients`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        dl_number: dl_number,
      }),
    })
      .then((r) => r.json())
      .then((data) => setNewPatient(data));
    navigate({ pathname: "/institutionDashboard" });
  }

  return (
    <div className="setupInstitution">
      <h1>New Patient Form</h1>
      <form className="createAccountForm">
        <div className="formDiv">
          <label className="formLabel">Name of Patient</label>
          <input
            type="text"
            value={name}
            className="formInput"
            onChange={(e) => setName(e.target.value)}
          ></input>
        </div>
        <div className="formDiv">
          <label className="formLabel">DL #</label>
          <input
            type="text"
            className="formInput"
            onChange={(e) => setDL_Number(e.target.value)}
            value={dl_number}
          ></input>
        </div>

        <button
          className="createAccountButton"
          onClick={handleInstitutionDashboardPage}
        >
          Add New Patient
        </button>
      </form>
    </div>
  );
}

export default NewPatientForm;
