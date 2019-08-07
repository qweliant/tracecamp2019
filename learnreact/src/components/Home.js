import React, {useState} from "react";
import rbr from '../rbr.jpg'

var sectionStyle = {
    width: "100%",
    height: "1000px",
    top: "px",
    backgroundImage: `url(${rbr} )`
  };

function HomeView(){
    return (
        <div>
        <body style={sectionStyle}>
          <h1>Welcome, my name is Qwelian Tanner</h1>
          <p>
              some fun facts about me: I enjoy manga, listening to audibooks, walking my dog, and America
          </p>
        </body>  
        </div>
    );
}

export default HomeView;