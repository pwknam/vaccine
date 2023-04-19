import React, { useState } from 'react';
import Webcam from "react-webcam";
import { Butler } from 'butler-sdk';
// import fs from 'fs';


// const WebcamComponent = (image, setImage) => <Webcam />;

const videoConstraints = {
    width: 400,
    height: 400,
    facingMode: "user"
};

export const WebcamCapture = ({image, setImage}) => {


    const webcamRef = React.useRef(null);
    
    const capture = React.useCallback(
        () => {
        const imageSrc = webcamRef.current.getScreenshot();
        setImage(imageSrc)


    });


    return (
        <div className="webcam-container">
            <div className="webcam-img">

                {image == '' ? <Webcam
                    audio={false}
                    height={400}
                    ref={webcamRef}
                    screenshotFormat="image/jpeg"
                    width={420}
                    videoConstraints={videoConstraints}
                /> : <img src={image} />}
            </div>
            <div>
                {image!='' ?
                    <button onClick={(e) => {
                        e.preventDefault();
                        setImage('')
                    }}
                        className="webcam-btn">
                        Retake Image</button> :
                    <button onClick={(e) => {
                        e.preventDefault();
                        capture();
                    }}
                        className="webcam-btn">Capture</button>
                }
            </div>
        </div>
    );
};
