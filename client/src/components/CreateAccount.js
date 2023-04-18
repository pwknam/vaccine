import React from "react";
import "../App.css";

function CreateAccount() {
  return (
    <div className="setupInstitution">
      <h1>Setup Institution</h1>
      <form className="createAccountForm">
        <div className="formDiv">
          <label className="formLabel">Name of Institution</label>
          <input className="formInput"></input>
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
          <input className="formInput"></input>
        </div>

        <button className="createAccountButton">Create Account</button>
      </form>
    </div>
  );
}

export default CreateAccount;
