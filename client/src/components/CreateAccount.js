import React, { useState } from "react";
import "../App.css";
import CA from "../images/CA.svg";

import { useNavigate } from "react-router-dom";

function CreateAccount({ setNewUser }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [option, setOption] = useState("Choose an option");

  const navigate = useNavigate();
  console.log(setNewUser);
  // function handleInstitutionDashboardPage() {
  //   navigate({ pathname: "/institutionDashboard" });
  // }

  function handleCreateAccountSubmit(e) {
    e.preventDefault();
    fetch(`/signup_${option === "Issuer" ? "issuer" : "validator"}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: name,
        password: password,
      }),
    })
      .then((r) => r.json())
      .then((data) => {
        console.log(setNewUser, data);
        setNewUser(data);
        navigate({
          pathname: `${
            option === "Issuer" ? "/institutionDashboard" : "/searchPage"
          }`,
        });
      });
  }

  return (
    <div className="container">
      <div className="left">
        <img src={CA} alt="CA" className="imageClass" />
      </div>
      <div className="right">
        <div className="setupInstitution">
          <h1>Setup Institution</h1>
          <form
            className="createAccountForm"
            onSubmit={handleCreateAccountSubmit}
          >
            <div className="formDiv">
              <label className="formLabel">Name of Institution</label>
              <input
                type="text"
                className="formInput"
                onChange={(e) => setName(e.target.value)}
                value={name}
              ></input>
            </div>
            <div className="formDiv">
              <label className="formLabel">Type of Institution</label>
              <select
                className="formInput"
                onChange={(e) => setOption(e.target.value)}
                value={option}
              >
                <option>Choose an option</option>
                <option>Issuer</option>
                <option>Validator</option>
              </select>
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

            <button className="button-47">Create Account</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default CreateAccount;
