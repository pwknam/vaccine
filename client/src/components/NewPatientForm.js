import React from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function NewPatientForm() {
  const navigate = useNavigate();

  function handleInstitutionDashboardPage() {
    navigate({ pathname: "/institutionDashboard" });
  }

  return (
    <div className="setupInstitution">
      <h1>New Patient Form</h1>
      <form className="createAccountForm">
        <div className="formDiv">
          <label className="formLabel">Name of Patient</label>
          <input type="text" className="formInput"></input>
        </div>
        <div className="formDiv">
          <label className="formLabel">DL #</label>
          <input type="text" className="formInput"></input>
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
