import React, { useState } from 'react'
import './homeStyles.css'
import { WebcamCapture} from '../Webcam/Webcam'


const Home = () => {
    const [image, setImage] = useState('');

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
          })
          .catch(error => {
            console.log(error);
          });
            // if (response.ok) {
            //   console.log(response);
            // } else {
            //   console.log('Failed to upload data.');
            // }
          
        //   .catch(error => {
        //     console.log(error);
        //   });
        
      
    }
        // setName('');
        // setEmail('');
        // setImage()
    // const handleSubmit = (event) => {
    //     event.preventDefault();
    //     console.log('hi')

        // Specify variables for use in script below
        // const apiKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNjkxNDc5MTMzMjAzMDMzOTY2OSIsImVtYWlsIjoibWNob2k0MTk0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpYXQiOjE2ODE2NjkwNzU5OTZ9.zYaCZMVgMnUWurL7CGa0JGrR29CIolKRlSvgqDZjTTU'
        // const queueId = '93c11f04-c119-4f78-a7b5-036b617fda49'

        // // Specify the path to the file you would like to process
        // const fileLocation = '...../uploads/ocr';

        // // Create client
        // const client = new Butler(apiKey)

        // const file = fs.createReadStream(fileLocation);
        // client.extractDocument(queueId, file).then((x) => {
        // console.log(x);
        // });
        // send the image to the server using fetch or axios
    // };


    return (
        <div className="home-container">
            <div className="container">
                <div className="text">
                    <h1>Upload or capture a picture of your ID</h1>
                    <form className="form">
                        <WebcamCapture image={image} handleSubmit={handleSubmit} setImage = {setImage} />
                        {/* <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
                        <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} /> */}
                        <button type="submit" id="login-button" onClick={(e) => handleSubmit(e)}>Submit</button>
                    </form>
                </div>
            </div>
        </div>
    )
}
export default Home
