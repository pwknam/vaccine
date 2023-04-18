import React from "react";
import "../App.css";

import { useNavigate } from "react-router-dom";

function CreateAccount() {
  const navigate = useNavigate();

  function handleInstitutionDashboardPage() {
    navigate({ pathname: "/institutionDashboard" });
  }

  return (
    <div className="setupInstitution">
      <h1>Setup Institution</h1>
      <form className="createAccountForm">
        <div className="formDiv">
          <label className="formLabel">Name of Institution</label>
          <input type="text" className="formInput"></input>
        </div>
        <div className="formDiv">
          <label className="formLabel">Type of Institution</label>
          <select className="formInput">
            <option></option>
            <option>Medical Institution</option>
            <option>Event Host</option>
            <option>Transporation</option>
          </select>
        </div>
        <div className="formDiv">
          <label className="formLabel">Set Password</label>
          <input type="text" className="formInput"></input>
        </div>

        <button
          className="createAccountButton"
          onClick={handleInstitutionDashboardPage}
        >
          Create Account
        </button>
      </form>
    </div>
  );
}

export default CreateAccount;
