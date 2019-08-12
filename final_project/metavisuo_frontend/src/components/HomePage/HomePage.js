import React from 'react';
import Navigation from '../Navigation/Navigation'
import bloom from '../../images/bloom.jpg'
import { Col } from "shards-react";

const background ={
    backgroundColor: "#abb4fe",

}

const bgImg = {
    backgroundImage: `url(${bloom})`,
    height: "100vh",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
}

const font ={
    color: "white",
    textAlign: "center"
}

const homePage = () => {
    return (
        <div style={background}>
            <Navigation/>
            
            <div style={bgImg}>

                <h1 style={font}>Welcome to Metavisuo!</h1>
            
            </div>
        </div> 
    );
}

export default homePage