import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";
import People from "../images/People.svg";

function Login({ setNewUser }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  function handleLogin(e) {
    e.preventDefault();
    fetch(`/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: name,
        password: password,
      }),
    })
    .then((r) => {
      if (!r.ok) {
        throw new Error("Invalid Username or Password")
      } else {
        return r.json()
      }
    })
    .then((data) => {
      setNewUser(data);
      if (data.role === "Issuer") {
        navigate({ pathname: "/institutionDashboard" });
      } else if (data.role === "Validator") {
        navigate({ pathname: "/searchPage" });
      } else if (data.role === "Patient") {
        navigate({ pathname: "/PatientVaccineSummary" });
      }
    })
    .catch(error => alert(error.message))
  }

  return (
    <div className="container">
      <div className="left">
        <img src={People} alt="People" style={{ width: 700, height: 700 }} />
      </div>
      <div className="right">
        <div className="formContainer">
          <h1>Login</h1>
          <form className="createAccountForm" onSubmit={handleLogin}>
            <div className="formDiv">
              <label className="formLabel">Username</label>
              <input
                type="text"
                className="formInput"
                onChange={(e) => setName(e.target.value)}
                value={name}
              ></input>
            </div>
            <div className="formDiv">
              <label className="formLabel">Password</label>
              <input
                type="password"
                className="formInput"
                onChange={(e) => setPassword(e.target.value)}
                value={password}
              ></input>
            </div>
            <button className="button-46">Login</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
