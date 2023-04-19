import React, { useState } from 'react'
import './homeStyles.css'
import { WebcamCapture} from '../Webcam/Webcam'


const Home = () => {
    const [image, setImage] = useState('');
    const[driverslicense, setDriverslicense] = useState('');

    const handleSubmit= (e) => {
        // alert("Form submitted");
        e.preventDefault()
        fetch('http://127.0.0.1:5555/upload', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image })
          })
          .then(res => {
            if (!res.ok) {
              throw new Error('Network response was not ok');
            }
            return res.json();
          })
          .then(data => {        
            console.log(data);
            setDriverslicense(data.license)
          })
          .catch(error => {
            console.log(error);
          });

        
      
    }



    return (
        <div className="home-container">
            <div className="container">
                <div className="text">
                    {/* <h1>Upload or capture a picture of your ID</h1> */}
                    <form className="form">
                        <WebcamCapture image={image} handleSubmit={handleSubmit} setImage = {setImage} />
                        {/* <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
                        <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} /> */}
                        <button type="submit" id="login-button" onClick={(e) => handleSubmit(e)}>Submit</button>
                    </form>
                    {driverslicense && <h1>{driverslicense}</h1>}    
                </div>
                 
            </div>
        </div>
    )
}
export default Home