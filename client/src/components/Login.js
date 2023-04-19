import React, { useState } from "react";
import "../App.css";
import { useNavigate } from "react-router-dom";

function Login({ setNewUser }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  // function handleInstitutionDashboardPage() {
  //   navigate({ pathname: "/institutionDashboard" });
  // }

  function handleLogin(e) {
    e.preventDefault();
    fetch(`http://127.0.0.1:5555/login`, {
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
        console.log(data);
        setNewUser(data);
        // navigate(
        //   `${data.role === "Issuer" ? "/institutionDashboard" : "/searchPage"}`
        // );
        if (data.role === "Issuer") {
          navigate({ pathname: "/institutionDashboard" });
        } else if (data.role === "Validator") {
          navigate({ pathname: "/searchPage" });
        } else if (data.role === "Patient") {
          navigate({ pathname: "/PatientVaccineSummary" });
        }
      });
  }

  return (
    <div className="setupInstitution">
      <h1>Login</h1>
      <form className="createAccountForm" onSubmit={handleLogin}>
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
          <label className="formLabel">Password</label>
          <input
            type="password"
            className="formInput"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
          ></input>
        </div>

        <button className="createAccountButton">Login</button>
      </form>
    </div>
  );
}

export default Login;
