import React from "react";
import "../App.css";
import { Route, Routes, useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();
  function handleInstitutionDashboardPage() {
    navigate({ pathname: "/institutionDashboard" });
  }
  return (
    <div className="setupInstitution">
      <h1>Login</h1>
      <form className="createAccountForm">
        <div className="formDiv">
          <label className="formLabel">Name of Institution</label>
          <input type="text" className="formInput"></input>
        </div>
        <div className="formDiv">
          <label className="formLabel">Password</label>
          <input type="text" className="formInput"></input>
        </div>

        <button
          className="createAccountButton"
          onClick={handleInstitutionDashboardPage}
        >
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;
