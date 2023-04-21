import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function ActivateAccount({ setUser }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [DL, setDL] = useState("");
  const [password, setPassword] = useState("");

  function onFormSubmit(e) {
    e.preventDefault();
    fetch(`/signup_patient/${DL}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    })
    .then((r) => {
      if (!r.ok) {
        throw new Error("Invalid Drivers License Number")
      }
      r.json()
    })
    .then((data) => {
      setUser(data);
      navigate({ pathname: "/patientVaccineSummary" });
    })
    .catch(error => alert(error.message))
  }

  return (
    <div className="setupInstitution">
      <h1>Setup Institution</h1>
      <form className="createAccountForm" onSubmit={onFormSubmit}>
        <div className="formDiv">
          <label className="formLabel">Username</label>
          <input
            type="text"
            className="formInput"
            onChange={(e) => setUsername(e.target.value)}
            value={username}
          ></input>
        </div>
        <div className="formDiv">
          <label className="formLabel">DL #</label>
          <input
            type="text"
            className="formInput"
            onChange={(e) => setDL(e.target.value)}
            value={DL}
          ></input>
        </div>

        <div className="formDiv">
          <label className="formLabel">Set Password</label>
          <input
            type="password"
            className="formInput"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          ></input>
        </div>

        <button className="createAccountButton">Activate Account</button>
      </form>
    </div>
  );
}

export default ActivateAccount;
