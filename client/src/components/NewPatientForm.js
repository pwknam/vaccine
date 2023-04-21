import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import New from "../images/new.svg";

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
    <div className="container">
      <div className="left">
        <div className="landingPageImage">
          <img src={New} alt="Coronavirus Vaccine" className="imageClass" />
        </div>
      </div>
      <div className="right">
        <div className="setupInstitution2">
          <h1>New Patient Form</h1>
          <form className="createAccountForm2">
            <div className="formDiv1">
              <label className="formLabel1">Name of Patient</label>
              <input
                type="text"
                value={name}
                className="formInput1"
                onChange={(e) => setName(e.target.value)}
              ></input>
            </div>
            <div className="formDiv1">
              <label className="formLabel1">DL #</label>
              <input
                type="text"
                className="formInput1"
                onChange={(e) => setDL_Number(e.target.value)}
                value={dl_number}
              ></input>
            </div>

            <button
              className="button-47"
              onClick={handleInstitutionDashboardPage}
            >
              Add New Patient
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default NewPatientForm;
