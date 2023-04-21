import React, { useState } from 'react'
import { WebcamCapture} from '../Webcam/Webcam'
import { useNavigate } from "react-router-dom";
import './homeStyles.css'


const Home = ({ setSearch }) => {
    const [image, setImage] = useState('');
    const [loading, setLoading] = useState(false);
    const [driverslicense, setDriverslicense] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault()
        setLoading(true);
        fetch('/upload', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image })
          })
          .then(res => {
            setLoading(false);
            if (!res.ok) {
              throw new Error('Network response was not ok');
            }
            return res.json();
          })
          .then(data => {        
            setSearch(data.license)
            navigate({ pathname: "/validatorDashboard" });
          })
          .catch(error => {
            setLoading(false);
            console.log(error);
          });
    }

    return (
        <form className="form">
            
            {loading ? (
              <div class="la-ball-atom">
              <div></div>
              <div></div>
              <div></div>
              <div></div>
            </div>
            
            ) : (<>
              <WebcamCapture image={image} setImage={setImage} />
              <button className="button-47" type="submit" id="login-button" onClick={(e) => handleSubmit(e)}>Submit</button>
              </>
            )}
            {driverslicense && <h1>{driverslicense}</h1>}
        </form>
    )
}

export default Home;
